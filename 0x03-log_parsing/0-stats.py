#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
from sys import stdin


def print_status_codes(status_counts, total_file_size):
    """Prints the status code with its count.
    Format:
        <status>: <count>
    """
    print("Total file size: {}".format(total_file_size))
    for status, count in status_counts.items():
        print("{}: {}".format(status, count))

status_counts = {}
total_file_size = 0

try:
    for line in stdin:
        parts = line.split()
        file_size = int(parts[-1])
        total_file_size += file_size
        status = int(parts[-2])

        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status] = status_counts.get(status, 0) + 1

        if len(status_counts) % 10 == 0:
            print_status_codes(status_counts, total_file_size)

except KeyboardInterrupt:
    print_status_codes(status_counts, total_file_size)