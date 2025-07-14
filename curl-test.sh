#!/usr/bin/env bash

set -euo pipefail

BASE=http://localhost:5001/api/timeline_post
RAND=$RANDOM

echo "Testing Timeline API with random ID: $RAND"
echo "======================================="

# POST a new timeline entry
echo "Creating new timeline post..."
POST_RESP=$(curl -s -X POST $BASE \
    -d "name=TestUser$RAND" \
    -d "email=test$RAND@example.com" \
    -d "content=Automated test post $RAND")

echo "POST Response:"
if command -v jq >/dev/null 2>&1; then
    echo "$POST_RESP" | jq .
    # Extract the ID for DELETE test
    POST_ID=$(echo "$POST_RESP" | jq -r '.id')
else
    echo "$POST_RESP"
    # Extract ID without jq (fallback)
    POST_ID=$(echo "$POST_RESP" | sed -n 's/.*"id":\([0-9]*\).*/\1/p')
fi

echo ""
echo "Getting all timeline posts..."

# GET all timeline posts
GET_RESP=$(curl -s $BASE)

echo "GET Response:"
if command -v jq >/dev/null 2>&1; then
    echo "$GET_RESP" | jq .
else
    echo "$GET_RESP"
fi

echo ""
echo "Testing DELETE endpoint for post ID: $POST_ID"

# DELETE the post we just created
DELETE_RESP=$(curl -s -X DELETE "$BASE/$POST_ID")

echo "DELETE Response:"
if command -v jq >/dev/null 2>&1; then
    echo "$DELETE_RESP" | jq .
else
    echo "$DELETE_RESP"
fi

echo ""
echo "Verifying deletion - Getting all posts again..."

# GET all timeline posts again to verify deletion
FINAL_GET_RESP=$(curl -s $BASE)

echo "Final GET Response:"
if command -v jq >/dev/null 2>&1; then
    echo "$FINAL_GET_RESP" | jq .
else
    echo "$FINAL_GET_RESP"
fi 