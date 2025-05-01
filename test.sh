#!/bin/bash

echo "Testing API endpoint scenarios..."

# Test 1: Missing API Key
echo -e "\nTest 1: Missing API Key"
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"data": [[14.23,1.71,2.43,15.6,127,2.80,3.06,0.28,2.29,5.64,1.04,3.92,1065]]}'

# Test 2: Wrong API Key
echo -e "\nTest 2: Wrong API Key"
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -H "X-API-Key: abid11111" \
     -d '{"data": [[14.23,1.71,2.43,15.6,127,2.80,3.06,0.28,2.29,5.64,1.04,3.92,1065]]}'

# Test 3: Happy Path (Correct API Key)
echo -e "\nTest 3: Happy Path"
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -H "X-API-Key: abid1234" \
     -d '{"data": [[14.23,1.71,2.43,15.6,127,2.80,3.06,0.28,2.29,5.64,1.04,3.92,1065]]}'