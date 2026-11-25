#!/bin/bash
# Send a DELETE request and print its response body.
curl -s -X DELETE -- "$1"
