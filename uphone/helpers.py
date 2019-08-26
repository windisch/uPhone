"""
Some required helpers that are available in Python3, but not in Micropython.
"""


def zfill(s, width):
    """
    """
    if len(s) < width:
        return ("0" * (width - len(s))) + s
    else:
        return s
