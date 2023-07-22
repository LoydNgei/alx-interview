#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys


# store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
lines_no = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code receive exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # update total size
            total_size += file_size

            # update count of lines
            lines_no += 1

        if lines_no == 10:
            lines_no = 0  # reset count
            print('File size: {}'.format(total_size))

            # print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
