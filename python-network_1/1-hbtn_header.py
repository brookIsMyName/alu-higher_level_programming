#!/usr/bin/python3
"""Print the X-Request-Id header from a URL using urllib."""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
