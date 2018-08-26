#!/usr/bim/env python
"""
Usage:
  LogParse.py apache_log_file

  This script takes a apache log file as an argument and then generates a
  report  with hostname, bytes transaferred ad status.

  Apache Access Log file format

  LogFormat "%h %l %u %t \"%r\" %>s %b"
  where

    %h – The IP address of the client.
    %l – The identity of the client determined by identd on the client’s machine. Will return a hyphen (-) if this information is not available.
    %u – The userid of the client if the request was authenticated.
    %t – The time that the request was received.
    \"%r\" – The request line that includes the HTTP method used, the requested resource path, and the HTTP protocol that the client used.
    %>s – The status code that the server sends back to the client.
    %b – The size of the object requested.

    E.g. 127.0.0.1 - peter [9/Feb/2017:10:34:12 -0700] "GET /sample-image.png HTTP/2" 200 1479


"""
import sys


def apache_output(line):
    """

    :rtype: object
    """
    split_line = line.split()
    return {'remote_host': split_line[0],
            'apache_status': split_line[8],
            'data_transfer': split_line[9]
            }


def create_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
        print(line_dict)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)

    infile_name = sys.argv[1]
    try:
        input_file = open(infile_name,'r')
    except IOError:
        print ("You must specify a valid file to parse")
        print(__doc__)
        sys.exit(1)
    create_report(input_file)
    input_file.close()
