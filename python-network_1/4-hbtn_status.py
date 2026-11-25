#!/usr/bin/python3
"""Fetch and display the ALU intranet status using Requests."""
import requests


if __name__ == "__main__":
    body = requests.get("https://alu-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
