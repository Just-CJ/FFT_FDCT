__author__ = 'Just_CJ'

from myDct import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    img = Image.open('test/mysample.jpg')
    test_arr = np.asarray(img.convert('L'))
    test_arr_blk = test_arr.reshape((8,8, test_arr.size/64))
    # res_blk = np.zeros((8,8,test_arr.size/64), dtype=np.float64)
    res = np.zeros((512,512), dtype=np.float64)

    # print myDct2(test_arr)

    for i in range(512/8):
        for j in range(512/8):
            res[8*i:(8*i+8), 8*j:(8*j+8)] = myDct2(test_arr[8*i:(8*i+8), 8*j:(8*j+8)])
            # print res[i:(i+8), j:(j+8)]

    # for i in range(test_arr.size/64):
    #     res_blk[:,:,i] = myDct2(test_arr_blk[:,:,i])


    # res = res_blk.reshape(512,512)
    # print res


    f = open('blk_dct_res.txt','w')
    for i in range(512):
        for j in range(512):
            f.write(str(res[i, j])+' ')
        f.write('\n')

    f.close()


