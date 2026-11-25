#!/usr/bin/python3
"""Fetch and display the ALU intranet status using urllib."""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as page:
        body = page.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
