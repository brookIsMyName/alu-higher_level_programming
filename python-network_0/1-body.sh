#!/bin/bash
# Follow redirects and print the response body only for HTTP 200.
body=$(mktemp) || exit 1; trap 'rm -f -- "$body"' EXIT; status=$(curl -sL -o "$body" -w '%{http_code}' -- "$1") || exit "$?"; if [[ $status == 200 ]]; then cat -- "$body"; fi
