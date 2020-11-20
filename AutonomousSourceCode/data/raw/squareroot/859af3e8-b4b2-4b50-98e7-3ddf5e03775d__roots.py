import scipy as sp
from handlerBlocchi import *
# get eigenvalue returns  an eigenvalue with imaginary part > 0

def gev(matrix):
    x = (matrix[0,0]+matrix[1,1])/2
    y = sp.sqrt(-sp.square(matrix[0,0]-matrix[1,1])-4*matrix[1,0]*matrix[0,1])/2
    return complex(x,y)


def csr0(complex_n):
    s = sp.sqrt(sp.square(complex_n.real)+sp.square(complex_n.imag)) # np.absolute()
    angle = sp.angle(complex_n)
    return sp.sqrt(s)*(complex((sp.cos(angle*0.5)), (sp.sin(angle*0.5))))


def csr1(complex_n):
    CMP0 = (sp.sqrt(sp.square(complex_n.real)+sp.square(complex_n.imag)))/2 #np.absolute()/2
    CMP1 = (complex_n.real/2)
    return complex(sp.sqrt(CMP0+CMP1),sp.sign(complex_n.imag)*(sp.sqrt(CMP0-CMP1)))


# From the book

def csr2(complex_n):
    t = sp.sqrt((sp.absolute(complex_n.real)+(sp.sqrt(sp.square(complex_n.real)+sp.square(complex_n.imag))))/2)
    if(complex_n.real >= 0):
        return complex(t,(complex_n.imag/(2*t)))
    else:
        return complex((complex_n.imag/(2*t)),t)

# De Moivre
    # -- square roots of a complex number are 2; n-roots of a square number are n
    # -- s^(1/n)* [cos((ang/2)+(2pi*k)/n) +i sin((ang/2)+(2pi*k)/n)] with k = [0...n-1]
    # http://www-thphys.physics.ox.ac.uk/people/FrancescoHautmann/Cp4/sl_clx_11_4_cls.pdf

def csr3(complex_n):
    ang = sp.angle(complex_n) # sp.arctan(a.imag/a.real) why it does not work?!?!
    r = sp.sqrt(sp.square(complex_n.real)+sp.square(complex_n.imag))
    if (sp.sin(ang/2)>=0): #sin>0
        return sp.sqrt(r)*(complex(sp.cos(ang/2),sp.sin(ang/2)))
    else:
        return sp.sqrt(r)*(complex(sp.cos((ang/2)+sp.pi),sp.sin((ang/2)+sp.pi)))

    #r1 = sp.sqrt(r)*(complex(sp.cos(ang/2),sp.sin(ang/2)))
    #r2 = sp.sqrt(r)*(complex(sp.cos((ang/2)+sp.pi),sp.sin((ang/2)+sp.pi)))
    #return r1,r2


def blockRoot(matrix):
    if (matrix.shape[0]==2):
        a = csr3(gev(matrix)).real
        ris=sp.ndarray(shape=(2,2))
        ris[0,0] = a + (1/(4*a))*(matrix[0,0] - matrix[1,1])
        ris[1,1] = a - (1/(4*a))*(matrix[0,0] - matrix[1,1])
        ris[0,1] = (1/(2*a))*matrix[0,1]
        ris[1,0] = (1/(2*a))*matrix[1,0]
    else:
        #print(sp.sqrt(matrix))
        return sp.sqrt(matrix)
    return ris

def diagRoots(matrix):
    ris = sp.zeros(shape=matrix.shape)
    bb,eb,dims,wb,i,j = findBlocks0(matrix)
    k=0
    for i in range (0,j):
        ris[k:k+dims[i],k:k+dims[i]] = blockRoot(matrix[k:k+dims[i],k:k+dims[i]])
        #print(matrix[k:k+dims[i],k:k+dims[i]])
        k += dims[i]
        #print k
        #print dims[i]; print '<--Dims'
    return ris
