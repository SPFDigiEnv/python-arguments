# Python Arguments
A template for writing Python scripts that have command line parameters. The template is used for writing scripts for example to process lots of files in a given folder.

## Project
This project is to develop a template for Python3 programme scripts to handle named command line parameters. Using parameters makes the script far more flexible, and is infinitely preferable to hard coding settings in the script itself - however the script template also allows for default values which can be useful.

The project uses argparse to manage the parameters passed to the script - this means they can be named. Once parameters are named, then the order they are put in doesn't matter.

usage: python-arguments.py [-h] [-d DIRECTORY] [-f FILENAME] [-v]

Arguments:
  -h, --help            show this help message and exit

  -d DIRECTORY, --directory DIRECTORY
                        directory path to location of files (e.g. --directory ./data/).

  -f FILENAME, --file FILENAME
                        file name or wildcard (e.g. --file *.csv).

  -v, --version         displays the version number

  Example: ./python-arguments.py -d .. -f *.csv
