# author: abhishekg785@gmail.com

# required packages
import numpy as np
import argparse
import cv2

# parse the arguments here
aparser = argparse.ArgumentParser()
aparser.add_argument('-i', '--image', help = 'path to the image')
args = vars(aparser.parse_args())

# get the image here
image = cv2.imread(args['image'])

# let us define the colors here
# the range of the colors in the order BGR ( Blue, Green, Red ) , opencv has opposite of RGB
# lower range arr to higher range arr of a color
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

for (l, u) in boundaries:
    lower = np.array()