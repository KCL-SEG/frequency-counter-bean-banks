"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if not frequencies.get(item, None):
            frequencies.update({item: 1})
        else:
            frequencies.update({item: frequencies.get(item)+1})
    # Your code goes here
    return frequencies
