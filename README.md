Resizer
====================

This script can be used to resize an image file to different sizes and save them to a directory with different postfixes at the end of each file name. Some preset file sizes and names are alredy stored to help you speed up the conversion process. For more details please read the header comments in the source files.

## Examples

### Example 1
Resize image.png to 25 by 25 pixels and save it with the new name of resize.png.
```
python3 resizer-base.py -f image.png -o . -s 25x25 -p "" -n resize
```

### Example 2
Resize image.png to 25 by 25 pixels and 50 by 50 pixels and save them with the prefixes _25 and _50 to the directory called results.
```
python3 resizer-base.py -f image.png -o ./results -s 25x25,50x50 -p _25,_50
```

### Example 3
Resize image.png to be used as an iOS UITabBarItem image. Rename the new files to start with "tab-bar-icon".
```
python3 resizer-preset.py -f image.png -t iOS_Tab-bar-icon -n tab-bar-icon
```

## Dependencies

* This script uses pillow to manipulate images. http://python-pillow.github.io/
* Made and tested with Python 3 only

## License

The MIT License (MIT)
Copyright (c) 2015 Soma Erdélyi (info@somaerdelyi.net)