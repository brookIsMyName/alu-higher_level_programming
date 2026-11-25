#!/bin/bash
# Send a GET request with the Holberton School user ID header.
curl -s -H 'X-HolbertonSchool-User-Id: 98' -- "$1"
