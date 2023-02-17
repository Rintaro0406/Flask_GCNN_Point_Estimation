import numpy as np
from scipy import integrate
from scipy import interpolate
#prevent the calcualtion of same function
def comoving_distance(LambdaCDM,z):
    return LambdaCDM.angular_distance(z)*(1.+z)

def P_NL(LambdaCDM,k, z):
    kmax = 30.#from the error of class
    # we do not compute matter power spectrum at scales smaller than the limit set by kmax
    if k > kmax: 
        return 0
    else:
        return LambdaCDM.pk(k, z) 

def redshift_distribution(gz,g_interp,z,zmin,zmax):
    #Don't repeat that np.zeros
    if zmin<=z and z<=zmax:
        return g_interp(z)
    else: 
        return 0
    
def lensing_kernel_bin_100(LambdaCDM,gz,g_interp,z,zmin,zmax):
    x=np.linspace(z,zmax,100)
    w=np.zeros(len(x))
    n=np.zeros(len(x))
    #Don't repeat that np.zeros
    for i in range(len(w)):
        w[i]=comoving_distance(LambdaCDM,x[i])
        n[i]=redshift_distribution(gz,g_interp,x[i],zmin,zmax)
    W=np.trapz(n*(w-comoving_distance(LambdaCDM,z))/w,x)
    if np.isnan(W)==True:
        return 0
    else:
        return W

def Pk_2D_integral_bin_100(LambdaCDM,gz,g_interp,l,zmin,zmax):
    z=np.linspace(0,zmax,100)
    W=np.zeros(len(z))
    w=np.zeros(len(z))
    H=np.zeros(len(z))
    P=np.zeros(len(z))
    for i in range(len(w)):
        w[i]=comoving_distance(LambdaCDM,z[i])
        W[i]=lensing_kernel_bin_100(LambdaCDM,gz,g_interp,z[i],zmin,zmax)
        H[i]=LambdaCDM.Hubble(z[i])
        P[i]=P_NL(LambdaCDM,l/w[i], z[i])
    Pk_2D_realistic = np.trapz((1/H) * (9./4.) * (LambdaCDM.Hubble(0.0))**4 * LambdaCDM.Omega0_m()**2 *(1+z)**2 * P*W**2,z)
    return Pk_2D_realistic

#vectorize

