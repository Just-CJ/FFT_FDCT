# -*- coding: utf-8 -*-
__author__ = 'Just_CJ'

from PIL import Image
import numpy as np
from myDct import *
import matplotlib
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

if __name__ == '__main__':

    img = Image.open('test/mysample.jpg')

    test_arr = np.asarray(img.convert('L'))
    res = myDct2(test_arr)
    data = np.log(np.abs(res))
    X = np.arange(0, 512, 1)
    Y = np.arange(512, 0, -1)

    plt.pcolor(data)
    plt.colorbar()
    plt.show()


