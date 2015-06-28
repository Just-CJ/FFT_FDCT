__author__ = 'Just_CJ'

import numpy as np


def W(nk, N):
    '''
    ' twiddle factor
    '''
    return np.exp(-(2.0 * np.pi * 1j * nk) / N)

def myfft(X):
    if len(X.shape) == 1:
        M = 1
        N = X.shape[0]
    else:
        M, N = X.shape

    X2 = X.reshape((M, N))

    if N == 1:
      return X
    else:
        G = np.zeros((M, N/2), dtype=np.complex)
        H = np.zeros((M, N/2), dtype=np.complex)

        for i in xrange(N/2):
            G[:, i] = X2[:, i] + X2[:, i+N/2]
            H[:, i] = (X2[:, i] - X2[:, i+N/2])*W(i, N)

        Feven = myfft(G)
        Fodd = myfft(H)

        combined = np.zeros((M, N), dtype=np.complex)

        for m in xrange(0, N, 2):
            combined[:, m] = Feven[:, m/2]
        for m in xrange(1, N, 2):
            combined[:, m] = Fodd[:, m/2]
        return combined