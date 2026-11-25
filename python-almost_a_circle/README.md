#!/usr/bin/python3

# Python Almost a Circle

The models package defines Base, Rectangle, and Square. The exercises cover
shared identifiers, validated dimensions, display offsets, positional and
keyword updates, and JSON serialization.

Run the tests from this directory.

```sh
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base.py
```

Each shape saves to a JSON file named after its class in the current
working directory.
