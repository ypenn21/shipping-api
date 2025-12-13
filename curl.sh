#!/bin/bash

echo "--- Testing /discovery ---"
curl -s http://127.0.0.1:8000/discovery
echo "\n"

echo "--- Creating a new package ---"
curl -s -X POST -H "Content-Type: application/json" \
     -d '{"product_id": "100", "height": 10, "width": 10, "depth": 10, "weight": 5, "special_handling_instructions": "Test Package"}' \
     http://127.0.0.1:8000/packages
echo "\n"

echo "--- Retrieving package with product_id 100 ---"
curl -s http://127.0.0.1:8000/packages/100
echo "\n"

echo "--- Updating package with ID 1 ---"
curl -s -X PUT -H "Content-Type: application/json" \
     -d '{"height": 15, "width": 15, "depth": 15, "weight": 10, "special_handling_instructions": "Updated Instructions"}' \
     http://127.0.0.1:8000/packages/1
echo "\n"

echo "--- Deleting package with ID 1 ---"
curl -s -X DELETE http://127.0.0.1:8000/packages/1
echo "\n"

echo "--- Verifying deletion of package with product_id 100 (expecting 404) ---"
curl -s -w "%{http_code}" http://127.0.0.1:8000/packages/100
echo "\n"
