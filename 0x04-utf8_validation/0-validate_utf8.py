#!/usr/bin/python3
"""
This module contains a function to validate if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): The list of integers, each representing one byte.
    
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0
    
    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Mask to get the 8 least significant bits
        mask = 1 << 8
        num = num % mask
        
        if num_bytes == 0:
            # Determine how many bytes the current character requires
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                # If the byte starts with '10' or '0', it's a 1-byte character
                # or continuation byte incorrectly placed.
                return False
        else:
            # Check continuation bytes: must start with '10'
            if not (num >> 6) == 0b10:
                return False
            num_bytes -= 1
    
    # All continuation bytes should have been consumed in a valid sequence
    return num_bytes == 0

# Testing code (not included in the script file for deployment)
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
