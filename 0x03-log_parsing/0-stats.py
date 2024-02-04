#!/usr/bin/python3
"""Implement Log parsing Algorithm"""

import re
import sys
from re import Match
from typing import Dict


def print_stats(status_codes, total_size):
    print(f'File size: {total_size}')
    for key in sorted(status_codes.keys()):
        if status_codes[key] == 0:
            continue
        print(f'{key}: {status_codes[key]}')


def main():
    pattern: str = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET \/projects\/260 HTTP\/1.1" (\d{3}) (\d+)$'
    line_count: int = 0

    status_codes: Dict[int, int] = {
        200: 0,
        301: 0,
        400: 0,
        403: 0,
        405: 0,
        500: 0
    }
    total_size: int = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line_match: Match[str] = re.match(pattern, line)
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
