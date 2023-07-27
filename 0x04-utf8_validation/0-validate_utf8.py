#!/usr/bin/python3
"""Method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Method that determines if a given data set represents a valid UTF-8"""
    expected_continuation_bytes = 0

    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        leading_one_mask = 1 << 7
        if expected_continuation_bytes == 0:
            # Count the number of leading 1s in the byte
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1
            if expected_continuation_bytes == 0:
                continue
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False

        # If we are expecting continuation bytes
        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        expected_continuation_bytes -= 1
    if expected_continuation_bytes == 0:
        return True
    else:
        return False
