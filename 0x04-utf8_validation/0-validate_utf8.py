#!/usr/bin/python3
"""Module for UTF-8 data validation."""


def validUTF8(data):
    """Validates whether a list of integers represent valid UTF-8 encoded data.
    For reference, see: <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip_count = 0
    length = len(data)

    for index in range(length):
        if skip_count > 0:
            skip_count -= 1
            continue

        # Check if data item is a valid integer within the UTF-8 range
        if not isinstance(data[index], int) or data[index] < 0 or data[index] > 0x10ffff:
            return False
        elif data[index] <= 0x7f:
            skip_count = 0
        elif data[index] & 0b11111000 == 0b11110000:
            # Check for a 4-byte UTF-8 encoding
            span = 4
            if length - index >= span:
                if not all((byte & 0b11000000) == 0b10000000 for byte in data[index + 1: index + span]):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[index] & 0b11110000 == 0b11100000:
            # Check for a 3-byte UTF-8 encoding
            span = 3
            if length - index >= span:
                if not all((byte & 0b11000000) == 0b10000000 for byte in data[index + 1: index + span]):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[index] & 0b11100000 == 0b11000000:
            # Check for a 2-byte UTF-8 encoding
            span = 2
            if length - index >= span:
                if not all((byte & 0b11000000) == 0b10000000 for byte in data[index + 1: index + span]):
                    return False
                skip_count = span - 1
            else:
                return False
        else:
            return False

    return True
