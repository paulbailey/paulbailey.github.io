#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("_pelican/"):
    category = os.path.basename(root)       
    for file in files:
        print category, file