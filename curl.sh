#!/bin/bash

echo "--- Testing /discovery ---"
curl -s http://127.0.0.1:8000/discovery
echo "\n"

echo "--- Creating a new package ---"
curl -s -X POST -H "Content-Type: application/json" \
     -d '{"package_id": "100", "height": 10, "width": 10, "depth": 10, "weight": 5, "special_handling_instructions": "Test Package100"}' \
     http://127.0.0.1:8000/packages
echo "\n"

curl -s -X POST -H "Content-Type: application/json" \
     -d '{"package_id": "1", "height": 10, "width": 10, "depth": 10, "weight": 5, "special_handling_instructions": "Test Package1"}' \
     http://127.0.0.1:8000/packages
echo "\n"

echo "--- Retrieving package with package_id 100 ---"
curl -s http://127.0.0.1:8000/packages/100
echo "\n"
