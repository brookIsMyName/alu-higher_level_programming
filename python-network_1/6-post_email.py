#!/usr/bin/python3
"""Send an email field in a POST request using Requests."""
import sys

import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
