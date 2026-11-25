#!/usr/bin/python3
"""Search for a user by letter and display the result of the JSON API."""
import sys

import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
    try:
        user = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not user:
            print("No result")
        else:
            print("[{}] {}".format(user.get("id"), user.get("name")))
