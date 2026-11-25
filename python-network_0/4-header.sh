#!/bin/bash
# Send a GET request with user ID 98 under both course header names.
curl -s -H 'X-HolbertonSchool-User-Id: 98' -H 'X-School-User-Id: 98' -- "$1"
