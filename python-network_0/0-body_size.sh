#!/bin/bash
# Print the response body size in bytes.
curl -s -o /dev/null -w '%{size_download}\n' -- "$1"
