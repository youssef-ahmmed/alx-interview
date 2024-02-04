#!/usr/bin/python3
"""Implement Log parsing Algorithm"""

import re
import sys


def print_stats(status_codes, total_size):
    """Print All statistics"""
    print(f'File size: {total_size}')
    for key in sorted(status_codes.keys()):
        if status_codes[key] == 0:
            continue
        print(f'{key}: {status_codes[key]}')


def main():
    """Entry point of implementation"""
    pattern = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
               r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET '
               r'\/projects\/260 HTTP\/1.1" (\d{3}) (\d+)$')
    line_count = 0

    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    total_size = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line_match = re.match(pattern, line)
            if not line_match:
                continue

            status_code = int(line_match.group(3))
            file_size = int(line_match.group(4))

            if status_code in status_codes.keys():
                status_codes[status_code] += 1

            total_size += file_size

            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

        print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise


if __name__ == '__main__':
    main()
