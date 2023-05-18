#!/usr/bin/python3
"""UTF-8 Validation Module
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    k_bytes = 0

    for num in data:
        byte = num & 0xff
        if k_bytes == 0:
            mask1 = 1 << 7
            mask2 = 1 << 6
            while mask1 & byte:
                n_bytes += 1
                mask1 = mask1 >> 1
                mask2 = mask2 >> 1
            if k_bytes == 0:
                continue
            if k_bytes == 1 or k_bytes > 4:
                return False
        else:
            mask1 = 1 << 7
            mask2 = 1 << 6
            if not (byte & mask1 and not (byte & mask2)):
                return False
        k_bytes -= 1
    return k_bytes == 0
