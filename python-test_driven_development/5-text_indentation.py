#!/usr/bin/python3
"""Format printed text by adding line breaks after punctuation."""


def text_indentation(text):
    """Trim line edges and print two newlines after periods, ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for index, character in enumerate(text):
        if character in ".?:":
            print(text[start:index + 1].strip(), end="\n\n")
        elif character == "\n":
            print(text[start:index].strip())
        else:
            continue
        start = index + 1
    print(text[start:].strip(), end="")
