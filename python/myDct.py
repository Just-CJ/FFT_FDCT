__author__ = 'Just_CJ'

import numpy as np
from myfft import myfft

def myFDct(f):
    '''
    :param f: M-by-N array
    :return: F: M-by-N array
    '''

    if len(f.shape) == 1:
        M = 1
        N = f.shape[0]
    else:
        M, N = f.shape

    X = np.zeros((M, N), dtype=np.complex)
    for i in xrange(N/2):
        X[:, i] = f[:, 2*i]
        X[:, i+N/2] = f[:, N-1-2*i]

    Y = myfft(X)
    # F = np.zeros((M, N), dtype=np.complex)
    # for i in xrange(N):
    #     F[:, i] = Y[:, 2*i+1]

    ww_1 = (np.exp(-1j*np.arange(N)*np.pi/(2*N))/np.sqrt(2*N))
    ww_1[0] /= np.sqrt(2)
    ww = np.array(M*[ww_1])
    #
    # A = np.ones((M, N), dtype=np.complex)
    # A[:, 0] = 1/np.sqrt(2)
    #
    # A2 = np.ones((M, 2*N), dtype=np.complex)
    # A2[:, 0] = 1/np.sqrt(2)

    # F = np.sqrt(2.0/N)*A*F
    Y = 2*ww*Y

    return Y.real
    #
    # f2 = f.reshape((M, N))
    # A = np.ones((M, N), dtype=np.float64)
    # A[:, 0] = 1/np.sqrt(2)
    # F = np.zeros((M, N), dtype=np.float64)
    # for u in range(N):
    #     B = (np.cos((2*np.arange(N)+1)*np.pi*u/(2*N))).reshape(1, N)
    #     # print B
    #     F[:, u] = (np.sqrt(2.0/N)*np.dot(A[:, u].reshape(M, 1), B)*f2).sum(axis=1)
        # print np.sqrt(2.0/N)*np.dot(A[:, u].reshape(M, 1), B)
    # return F

def myDct(f):
    if len(f.shape) == 1:
        M = 1
        N = f.shape[0]
    else:
        M, N = f.shape

    f2 = f.reshape((M, N))
    A = np.ones((M, N), dtype=np.float64)
    A[:, 0] = 1/np.sqrt(2)
    F = np.zeros((M, N), dtype=np.float64)
    for u in range(N):
        B = (np.cos((2*np.arange(N)+1)*np.pi*u/(2*N))).reshape(1, N)
        # print B
        F[:, u] = (np.sqrt(2.0/N)*np.dot(A[:, u].reshape(M, 1), B)*f2).sum(axis=1)
        # print np.sqrt(2.0/N)*np.dot(A[:, u].reshape(M, 1), B)
    return F

def myDct2(f):
    '''
    :param f: M-by-N array
    :return: F: M-by-N array
    '''
    F = myFDct(myFDct(f).transpose()).transpose()
    return F