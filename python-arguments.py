#!/usr/bin/env python3
# This python code demonstrates processing of command line parameters for file location.
# Use as basis for file processing projects
# python-arguments.py

import sys
import os
import glob
import argparse

DEFAULT_DIRECTORY = '.'
DEFAULT_FILES = '*.csv'

if sys.version_info[0] < 3:
    sys.exit("This app requires Python 3.")

###########################################
# _file_processor
# Process individual file and write results out to outfile
def _file_processor(file):
    print('Processing', file)
    try:
        print('File processing code goes here')
    except:
        pass

###########################################
# _make_argument_parser
# Create a command-line argument parser object
# See https://www.experts-exchange.com/questions/26881841/Accepting-folder-filename-or-wildcard-for-python-argument.html
def _make_argument_parser():
    parser = argparse.ArgumentParser(description='Process data files with parameters for specifying directory and files.')
    parser.add_argument(
        '-d', '--directory',
        type=str,
        action='store',
        dest='directory',
        default=None,
        help='directory path to location of files (e.g. --directory ./data/).'
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        action='store',
        dest='filename',
        default='*.csv',
        help='file name or wildcard (e.g. --file *.csv).'
    )
    parser.add_argument(
        '-v', '--version',
        action="store_true",
        dest='show_version',
        default=False,
        help='displays the version number'
    )
    return parser

###########################################
# main
def main(args=None):
    parser = _make_argument_parser()
    options = parser.parse_args()

    if options.show_version:
        prog = os.path.basename(sys.argv[0])
        version_str = "1.0"
        print ("Version number of %s is v%s" % (prog, version_str))
        sys.exit(0)

    filenames_or_wildcards = []
    if options.directory is not None and options.filename is None:
        print ("Invalid combination of command line arguments")
        sys.exit(0)

    if (options.filename is None):
         options.filename = DEFAULT_FILES

    if (options.directory is None):
        options.directory = DEFAULT_DIRECTORY

    if options.directory is not None:
        filenames_or_wildcards.append( os.path.join(options.directory, options.filename) )

    all_files = []
    for filename_or_wildcard in filenames_or_wildcards:
        all_files.extend( glob.glob(filename_or_wildcard) )

    try:
        for filename in all_files:
            if os.path.exists(filename):
                _file_processor(filename)
            else:
                print("Check if file exists: %s" % (filename))
    except Exception as e:
        raise e

###########################################
if __name__ == "__main__":
    main()
