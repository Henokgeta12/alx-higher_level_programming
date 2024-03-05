#!/bin/bash

url=$1

response=$(curl -sSL -H "X-School-User-Id: 98" "$url")
echo "Response body:"
echo "$response"
