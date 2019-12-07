
import numpy as np

def Kompozycja (n,m,A,k=1):
    if k > 0:
        if k < m:
            for i in range(n-(m-k)):
                A[k-1] = (i+1)
                Kompozycja(n-(i+1),m,A,k+1)
        else:
            A[k-1]=n
            print(A)

Kompozycja(5,3,np.zeros(3))


