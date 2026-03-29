# Implementation Plan - Unit Tests with Mocks for Shipping API

## 1. 🔍 Analysis & Context
*   **Objective:** Create a comprehensive suite of unit tests for the REST API endpoints in `main.py`. The tests must isolate the API logic by mocking database interactions (reads & writes) handled by `SQLAlchemy`.
*   **Affected Files:**
    *   `tests/test_main_mock.py` (New file)
    *   `tests/test.py` (Optional: clean up or deprecate if redundant, but for now we focus on adding the new suite)
*   **Key Dependencies:**
    *   `unittest` (Standard Python library)
    *   `unittest.mock` (Standard Python library for creating mocks)
    *   `flask` (For `app.test_client()`)
*   **Risks/Unknowns:**
    *   Ensuring `SessionMaker` is mocked correctly in the context of `main.py` (namespacing).
    *   Mocking chained SQLAlchemy calls (`query().filter().first()`) requires careful setup of return values.

## 2. 📋 Checklist
- [x] Create `tests/test_main_mock.py`.
- [x] Implement setup/teardown for Flask test client.
- [x] Implement tests for "Metadata" endpoints (`/discovery`, `/liveness`, `/readiness`).
- [x] Implement tests for `POST /packages` (Success & Validation Error).
- [x] Implement tests for `GET /packages/<id>` (Found & Not Found).
- [x] Implement tests for `PUT /packages/<id>` (Success & Not Found).
- [x] Implement tests for `DELETE /packages/<id>` (Success & Not Found).
- [x] Verify all tests pass.

## 3. 📝 Step-by-Step Implementation Details

### Step 1: Test Setup & Metadata Endpoints
*   **Goal:** Establish the testing scaffold and verify simple endpoints that don't need DB mocking.
*   **Action:**
    *   Create `tests/test_main_mock.py`.
    *   Define `TestShippingApp` class inheriting from `unittest.TestCase`.
    *   In `setUp`, initialize `self.app = app.test_client()`.
    *   Add tests:
        *   `test_discovery`: GET `/discovery`, assert 200 and JSON structure.
        *   `test_liveness`: GET `/liveness`, assert 200.
        *   `test_readiness`: GET `/readiness`, assert 200.
*   **Status:** ✅ Implemented in `tests/test_main_mock.py`.

### Step 2: Test `POST /packages` (Create)
*   **Goal:** Verify package creation logic and error handling.
*   **Action:**
    *   Import `patch` from `unittest.mock`.
    *   Decorate test methods with `@patch('main.SessionMaker')`.
    *   **Test Case: `test_create_package_success`**
        *   Mock payload: `{'product_id': 123, 'height': 10, ...}`
        *   Setup `mock_session_maker` to return a `mock_session`.
        *   Call `self.app.post('/packages', json=...)`.
        *   Assert status code 201.
        *   Assert `mock_session.add` and `mock_session.commit` were called.
    *   **Test Case: `test_create_package_missing_fields`**
        *   Payload missing `product_id`.
        *   Call `self.app.post(...)`.
        *   Assert status code 400.
        *   Assert DB methods were **not** called.
*   **Status:** ✅ Implemented in `tests/test_main_mock.py`.

### Step 3: Test `GET /packages/<id>` (Read)
*   **Goal:** Verify fetching logic.
*   **Action:**
    *   **Test Case: `test_get_package_success`**
        *   `@patch('main.SessionMaker')`
        *   Setup `mock_session.query(Package).filter(...).first.return_value` to return a `Package` object.
        *   Call `self.app.get('/packages/123')`.
        *   Assert status 200 and correct JSON body.
    *   **Test Case: `test_get_package_not_found`**
        *   Setup mock chain to return `None`.
        *   Call `self.app.get(...)`.
        *   Assert status 404.
*   **Status:** ✅ Implemented in `tests/test_main_mock.py`.

### Step 4: Test `PUT /packages/<id>` (Update)
*   **Goal:** Verify update logic.
*   **Action:**
    *   **Test Case: `test_update_package_success`**
        *   Mock existing package object.
        *   Send PUT request with new `weight`.
        *   Assert package object attributes were updated.
        *   Assert `mock_session.commit()` called.
        *   Assert status 200.
    *   **Test Case: `test_update_package_not_found`**
        *   Mock return `None`.
        *   Assert 404.
*   **Status:** ✅ Implemented in `tests/test_main_mock.py`.

### Step 5: Test `DELETE /packages/<id>` (Delete)
*   **Goal:** Verify deletion logic.
*   **Action:**
    *   **Test Case: `test_delete_package_success`**
        *   Mock existing package.
        *   Call DELETE.
        *   Assert `mock_session.delete(package)` and `commit()` called.
        *   Assert status 204.
    *   **Test Case: `test_delete_package_not_found`**
        *   Mock return `None`.
        *   Assert 404.
*   **Status:** ✅ Implemented in `tests/test_main_mock.py`.

## 4. 🧪 Testing Strategy
*   **Unit Tests:** Run `python3 -m unittest tests/test_main_mock.py`.
*   **Manual Verification:** Ensure the output shows "OK" and the number of tests matches expectation (approx 9-10 tests).

## 5. ✅ Success Criteria
*   A new file `tests/test_main_mock.py` exists.
*   All endpoints in `main.py` are covered by at least one positive and one negative (where applicable) test case.
*   Tests run successfully without requiring a running database (validated by the use of mocks).
