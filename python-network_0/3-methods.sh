#!/bin/bash
# Print the HTTP methods listed in the response's Allow header.
curl -sI -- "$1" | awk 'tolower($0) ~ /^allow:/ { sub(/^[^:]+:[[:blank:]]*/, ""); sub(/\r$/, ""); print }'
