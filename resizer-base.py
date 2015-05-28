#! /usr/bin/env python3
'''
This script resizes the given image to multiple sizes and saves them to a dictionary

This script is implemented with argparse.
Usage: resizer-base.py [-h] -f SOURCE FILE -o OUTPUT DIRECTORY -s SIZE LIST -p POSTFIX [-n NEW NAME]

Arguments
SOURCE FILE must be a valid image file in a format pillow can handle
OUTPUT DIRECTORY must be an existing directory
SIZE LIST must be comma separated where every item is formatted as WIDTHxHEIGHT, for example "25x25,50x50,75x75"
POSTFIX must contain unique elements
SIZE LIST and POSTFIX lists must have the same number if elements

Dependencies
This script uses pillow to manipulate images. http://python-pillow.github.io/

Created on 2015.05.
@author: Soma Erdelyi (info@somaerdelyi.net)
'''

import argparse
import os,sys
from PIL import Image

# Argument parser initialization
parser = argparse.ArgumentParser();
parser.add_argument("-f", "--source_file", help="Location of the source image file.", type=str, required=True)
parser.add_argument("-o", "--output_directory", help="Location of the output directory.", type=str, required=True)
parser.add_argument("-s", "--size_list", help="Comma separated list of the desired image's size in WIDTHxHEIGHT format.", type=str, required=True)
parser.add_argument("-p", "--postfix", help="Comma separated list of the postfix to put after every image.", type=str, required=True)
parser.add_argument("-n", "--new_name", help="If set the postfix list will append this name, original if not.", type=str, required=False)
args = parser.parse_args();

# Argument checks
if not os.path.isfile(args.source_file):
    raise FileNotFoundError("Source image not found.")

if not os.path.isdir(args.output_directory):
    raise NotADirectoryError("Output directory not found.")

if not len(args.size_list.split(',')) == len(args.postfix.split(',')):
    raise ValueError("Size list and prefix list has different length")

for size in args.size_list.split(','):
    split_size = size.split('x')
    if len(split_size) != 2 or split_size[0].isdigit() == False or split_size[1].isdigit() == False:
        raise ValueError("Size list elements must contain two integers separated with character 'x'")

if len(args.postfix.split(',')) != len(set(args.postfix.split(','))):
    raise ValueError("Every postfix list item must be unique")

# Convert the size list
sizes = []
for size in args.size_list.split(','):
    split_size = size.split('x')
    dict_size = {}
    dict_size['width'] = int(split_size[0])
    dict_size['height'] = int(split_size[1])
    sizes.append(dict_size)

# Convert the postfix list
postfixes = []
for postfix in args.postfix.split(','):
    postfixes.append(postfix)

# Read the source image file and create file name
original_image = Image.open(args.source_file).convert('RGBA')
dpi = original_image.info['dpi']
original_filename = os.path.splitext(os.path.basename(args.source_file))
if args.new_name is not None:
    filename_base = args.new_name
else:
    filename_base = original_filename[0]

# Go through the size list and do the resizeing
for (size,postfix) in zip(sizes,postfixes):
    new_filename =  filename_base + postfix + original_filename[1]
    new_image = original_image.resize((size['width'],size['height']), Image.ANTIALIAS)
    new_image.save(os.path.join(args.output_directory,new_filename), quality = 90, dpi = dpi)