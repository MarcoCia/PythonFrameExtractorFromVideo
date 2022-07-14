import py2exe
from distutils.core import setup
import sys
import os
from os import walk
import os.path as osp
import argparse
import cv2
import math
from tqdm import tqdm
from multiprocessing import Pool

sys.argv.append('py2exe')

setup(options={"py2exe": {
                "includes": ["numpy","cv2"]
                }},
      console = [{'script': "extract.py"}],
       );