import unittest
from unittest.mock import patch, MagicMock
from main import app
from data_model import Package

class TestShippingApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_discovery(self):
        response = self.app.get('/discovery')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'shipping')
        self.assertEqual(data['version'], '1.0')

    def test_liveness(self):
        response = self.app.get('/liveness')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'live')

    def test_readiness(self):
        response = self.app.get('/readiness')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ready')

    @patch('main.SessionMaker')
    def test_create_package_success(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        
        payload = {
            'product_id': 123,
            'height': 10.0,
            'width': 10.0,
            'depth': 10.0,
            'weight': 5.0,
            'special_handling_instructions': 'Fragile'
        }
        
        response = self.app.post('/packages', json=payload)
        self.assertEqual(response.status_code, 201)
        
        data = response.get_json()
        self.assertIn('package_id', data)
        
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_create_package_missing_fields(self, mock_session_maker):
        payload = {
            'height': 10.0,
            # missing product_id
        }
        
        response = self.app.post('/packages', json=payload)
        self.assertEqual(response.status_code, 400)
        
        mock_session_maker.assert_not_called()

    @patch('main.SessionMaker')
    def test_get_package_success(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        
        # Setup mock package
        mock_package = Package(
            product_id="123",
            height=10.0,
            width=20.0,
            depth=30.0,
            weight=5.0,
            special_handling_instructions="None"
        )
        
        # Configure the query chain: session.query(Package).filter(...).first()
        mock_session.query.return_value.filter.return_value.first.return_value = mock_package
        
        response = self.app.get('/packages/123')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertEqual(data['product_id'], "123")
        self.assertEqual(data['height'], 10.0)
        
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_get_package_not_found(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        
        # Configure the query chain to return None
        mock_session.query.return_value.filter.return_value.first.return_value = None
        
        response = self.app.get('/packages/999')
        self.assertEqual(response.status_code, 404)
        
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_update_package_success(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        
        # Mock existing package
        mock_package = Package(
            id=1,
            product_id="123",
            height=10.0,
            width=20.0,
            depth=30.0,
            weight=5.0,
            special_handling_instructions="None"
        )
        mock_session.query.return_value.filter.return_value.first.return_value = mock_package
        
        payload = {'weight': 10.0}
        response = self.app.put('/packages/1', json=payload)
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertEqual(data['weight'], 10.0)
        self.assertEqual(mock_package.weight, 10.0)
        
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_update_package_not_found(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        mock_session.query.return_value.filter.return_value.first.return_value = None
        
        response = self.app.put('/packages/999', json={'weight': 10.0})
        self.assertEqual(response.status_code, 404)
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_delete_package_success(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        
        mock_package = Package(id=1)
        mock_session.query.return_value.filter.return_value.first.return_value = mock_package
        
        response = self.app.delete('/packages/1')
        self.assertEqual(response.status_code, 204)
        
        mock_session.delete.assert_called_once_with(mock_package)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('main.SessionMaker')
    def test_delete_package_not_found(self, mock_session_maker):
        mock_session = MagicMock()
        mock_session_maker.return_value = mock_session
        mock_session.query.return_value.filter.return_value.first.return_value = None
        
        response = self.app.delete('/packages/999')
        self.assertEqual(response.status_code, 404)
        mock_session.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
