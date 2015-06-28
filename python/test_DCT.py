__author__ = 'Just_CJ'

from myDct import *
from myfft import *
import numpy as np
import time

if __name__ == '__main__':


    length = 2
    for i in range(50):
        f = np.random.randint(0, 255, (1, length))
        start = time.clock()
        for j in range(100):
            F = myDct(f)
        stop = time.clock()
        print i
        length*=2
        f1 = open('test/test_mydct_n.txt', 'a')
        f2 = open('test/test_mydct_time.txt', 'a')
        f2.write(str(stop-start)+' ')
        f1.write(str(length)+' ')
        f1.close()
        f2.close()


    # print F2


