import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time
import pdb
import collections
import pandas as pd
import imageio
from PIL import Image
import glob


class VideoLoop:




    def find_duplicates(self,myPath,data_path,res=32):

        frameCounter = len(glob.glob1(myPath, "*.tif"))
        # we'll store the info on repeated frames here
        seen_frames = {}
        duplicate_frames = {}

        for frame in range(frameCounter):
            # get frame x
            frame = frame.get_data(x)

            if x % 1000 == 0:
                print("frame count: ", x, "\t", round(x * 1.0 / all_frames, 3) * 100, '%')

            # hash our frame
            hashed = self.ahash(frame, res)

            if seen_frames.get(hashed, None):
                # if we've seen this frame before, add it to the list of frames
                # that all have the same hashed value in duplicate_frames
                duplicate_frames[hashed].append(x)
            else:
                # if it's the first time seeing a frame, put it in seen_frames
                seen_frames[hashed] = x
                duplicate_frames[hashed] = [x]

        # return a list of lists of duplicate frames
        return [duplicate_frames[x] for x in duplicate_frames if len(duplicate_frames[x]) > 1]


    def ahash(self,frame, res=64):
        i = Image.fromarray(frame)
        i = i.resize((res, res), Image.ANTIALIAS).convert('L')
        pixels = list(i.getdata())
        avg = sum(pixels) / len(pixels)
        bits = "".join(map(lambda pixel: '1' if pixel < avg else '0', pixels))
        hexadecimal = int(bits, 2).__format__('016x').upper()
        return hexadecimal
