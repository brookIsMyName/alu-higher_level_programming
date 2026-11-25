#!/usr/bin/python3
"""Print the X-Request-Id header from a URL using Requests."""
import sys

import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
