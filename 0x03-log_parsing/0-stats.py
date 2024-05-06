#!/usr/bin/env python3
"""Log parsing"""


import sys
import signal

try:
    total_line = 0
    tot_file_size = 0
    status_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        ip_address, _, _, status_code, file_size = parts

        if len(line) != 7:
            continue

        status_code = int(status_code)
        if status_code in status_count:
            status_count[status_code] += 1

        tot_file_size += int(file_size)
        total_line += 1
        if total_line % 10 == 0:
            print("File size: {}".format(tot_file_size))
            for status_code, count in sorted(status_count.items()):
                if count > 0:
                    print("{}: {}".format(status_code, count))

except KeyboardInterrupt:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(0)
