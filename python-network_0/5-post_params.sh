#!/bin/bash
# POST the required email and subject and print the response body.
curl -s --data-urlencode 'email=test@gmail.com' --data-urlencode 'subject=I will always be here for PLD' -- "$1"
