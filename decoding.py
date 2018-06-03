#!/usr/bin/python3

import base64


def decode_base64(some):
    return base64.b64decode(some).decode("utf-8")

some = "VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg=="
print(decode_base64(some))
