import sys
import os
import csv
import argparse

"""
Usage:

Splits a csv file into multiple files based on the command line arguments
    
    Arguments:
    
    `-h`: help on usage
    `-i`: csv imput file name
    `-o`: output file name
    `-r`: row number to split from
    
    Default settings:
    
    `output path is the current directory
    headers are displayed on each file
    the default delimiter is the comma
       
"""

def parse_arguments():
    """Grab user supplied arguments using the argparse library"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_file",required=True,
                        help="csv input file name (without extension)",type=str)