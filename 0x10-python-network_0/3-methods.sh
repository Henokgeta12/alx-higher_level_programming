#!/bin/bash

url=$1

methods=$(curl -sI -X OPTIONS "$url" | grep "Allow:" | cut -d' ' -f2-)

echo "HTTP Methods:"
echo "$methods"
