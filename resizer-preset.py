#! /usr/bin/env python3
'''
This script calls the resizer base script with preset arguments.

This script is implemented with argparse.
usage: resizer-preset.py [-h] -f SOURCE_FILE -t TYPE [-o OUTPUT_DIRECTORY] [-n NEW_NAME]

Created on 2015.05.
@author: Soma Erdelyi (info@somaerdelyi.net)
'''

import subprocess
import argparse
import os,sys

# Argument parser initialization
parser = argparse.ArgumentParser();
parser.add_argument("-f", "--source_file", help="Location of the source image file.", type=str, required=True)
parser.add_argument("-t", "--type", help="Name of the conversion type. Types are specified in the source file.", type=str, required=True)
parser.add_argument("-o", "--output_directory", help="Location of the output directory.", type=str, required=False)
parser.add_argument("-n", "--new_name", help="If set the postfix list will append this name, original if not.", type=str, required=False)
args = parser.parse_args();

# Dictionary with all the preset sizes
types = {
    'iOS_Tab-bar-icon' : ('25x25,50x50,75x75', '@1x,@2x,@3x'),
    'iOS_App-icon' : ('180x180,120x120,120x120,152x152,76x76', 'iPhone6Plus,iPhone6andiPhone5,iPhone4s,iPadandiPadmini,iPad2andiPadmini', 'AppIcon_')
    }

# Argument checks
if not os.path.isfile(args.source_file):
    raise FileNotFoundError("Source image not found.")

if not args.output_directory is None and not os.path.isdir(args.output_directory):
    raise NotADirectoryError("Output directory not found.")

if not args.type in types:
    raise ValueError("The given type parameter was not found in the directory.")

# SETTINGS
resizer = "./resizer-base.py"
output_directory = "." if args.output_directory is None else args.output_directory

# Merge given arguments with preset ones
resizer_process = ["python3"]
resizer_process.append(resizer)
resizer_process.append("-s")
resizer_process.append(types[args.type][0])
resizer_process.append("-p")
resizer_process.append(types[args.type][1])
resizer_process.append("-o")
resizer_process.append(output_directory)
resizer_process.append("-f")
resizer_process.append(args.source_file)

if not args.new_name is None:
    resizer_process.append("-n")
    resizer_process.append(args.new_name)

if len(types[args.type]) == 3 and args.new_name is None:
    resizer_process.append("-n")
    resizer_process.append(types[args.type][2])

# Call the resizer.py file to do the actual work
subprocess.call(resizer_process)