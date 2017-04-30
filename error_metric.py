import io
import os
import re
import sys
import bz2
import glob
import math
import time
import pickle
import random
import argparse
import itertools
import threading
import collections

# Scientific & Imaging Libraries
import numpy as np
import scipy.ndimage, scipy.misc, PIL.Image
import skimage
from skimage import data, img_as_float
from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_psnr as psnr
# Numeric Computing (GPU)
import theano, theano.tensor as T
T.nnet.softminus = lambda x: x - T.nnet.softplus(x)

if __name__ == "__main__":

    pred_file = os.path.join(sys.argv[1], "*.jpg")
    true_file = os.path.join(sys.argv[2], "*.jpg")
    output_f = open(sys.argv[3], 'w')

    pred_file = sorted(glob.glob(pred_file))
    true_file = sorted(glob.glob(true_file))

    assert len(pred_file) == len(true_file), "pred_file and true_file should have same number." \
    "pred = %s, true = %s" % (str(len(pred_file)),str(len(true_file)))
    s = []
    p = []
    for i in range(0, len(pred_file)):
        pred_image = skimage.io.imread(pred_file[i])  
        true_image = skimage.io.imread(true_file[i])
        s.extend([ssim(pred_image, true_image, multichannel=True)])
        p.extend([psnr(pred_image, true_image)])


    output_f.write("SSIM: %s\n", str(np.mean(s)))
    output_f.write("PSNR: %s\n", str(np.mean(p)))    

