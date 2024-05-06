#!/usr/bin/python3
"""Log parsing"""


import sys
import signal


def print_status(status_count, tot_file_size):
    """Print status

    Print the total file size and the number of requests for each
    status code. The status codes are sorted by their numerical
    value.

    Arguments:
        status_count (dict): A dictionary with the number of
            requests for each status code.
        tot_file_size (int): The total file size.
    """
    print("File size: {:d}".format(tot_file_size))
    for k, v in sorted(status_count.items()):
        if v:
            print("{}: {:d}".format(k, v))


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
        parts = line.split()

        if len(parts) > 2:
            total_line += 1
            status_code = (int(parts[-2]))
            file_size = (int(parts[-1]))
            if status_code in status_count:
                status_count[status_code] += 1

            tot_file_size += file_size
        if total_line % 10 == 0:
            print_status(status_count, tot_file_size)

except KeyboardInterrupt:
   pass
