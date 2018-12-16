#!/usr/bin/env python

import os

# Keith Murray
# From stackoverflow... Somewhere

def les(filePath):
    fileList = []
    if os.path.isfile(filePath):
        fileList.append(filePath)
    else:
        for dirname, dirnames, filenames in os.walk(filePath):
            for filename in filenames:
                fileList.append(os.path.join(dirname, filename))
    return fileList
    
