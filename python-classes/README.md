# Python Classes

This directory contains exercises that introduce object-oriented programming
in Python through a sequence of square classes.

## Exercises

- `0-square.py`: an empty `Square` class.
- `1-square.py`: a square with an unvalidated private size.
- `2-square.py`: a square with validated size initialization.
- `3-square.py`: adds area calculation.
- `4-square.py`: adds a validated `size` property.
- `5-square.py`: adds text rendering with `#` characters.
- `6-square.py`: adds validated position and indentation when rendering.

Each numbered module can be imported independently. For example:

```python
Square = __import__("6-square").Square
square = Square(3, (1, 2))
print(square.area())
square.my_print()
```
