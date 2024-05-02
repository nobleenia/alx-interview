#!/usr/bin/python3
"""
This script reads from stdin log entries with a specific
format and prints statistics every 10 lines or upon receiving
a keyboard interruption about total file size and HTTP status codes.
"""

import sys
import signal

# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


def print_stats():
    """Prints the collected statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) < 7 or '"' not in line:
            continue
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
        total_size += file_size

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
finally:
    print_stats()  # Ensure stats are printed when the loop exits naturally
