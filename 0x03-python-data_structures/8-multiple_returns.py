#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None

    x = len(sentence)
    b = sentence[0]
    return x, b
