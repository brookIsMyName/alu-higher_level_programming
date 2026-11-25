#!/usr/bin/python3
"""Print a URL's response body or HTTP error code using Requests."""
import sys

import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
