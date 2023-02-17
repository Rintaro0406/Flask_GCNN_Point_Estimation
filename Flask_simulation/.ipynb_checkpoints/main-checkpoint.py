import time
start = time.time()
import numpy as np
from scipy import interpolate
import multiprocessing as mp
from Limber_Integration import Pk_2D_integral_bin_100
from Power_Spectrum_3D import matter_powrspectrum
import Shift_Parameter
from Flask_Map import lognormal
import matplotlib.pyplot as plt
import healpy as hp
import os 


NSIDE=4096
# using the Quijote cosmology and variating the OmegaM and Sigma8
LHS_data = np.load('/project/ls-gruen/users/r.kanaki/LHS_result/train1000/training_rintaro_LHS_parameter_file.npz')
#LHS_data = np.load('/project/ls-gruen/users/r.kanaki/LHS_result/test200/test_rintaro_LHS_parameter_file.npz')

# using the Quijote cosmology and variating the OmegaM and Sigma8
# Cosmology of Quijote sims
Omfid = LHS_data['omega_matter']
Obfid = 0.047
hfid = 0.7
nsfid =0.96
sig8fid = LHS_data['sigma_8']

#Loading the redshift distribution
gz=np.loadtxt("../DeepSphereTest1/nofz_DESY3_source_BIN1234.tab", usecols=(0,1),unpack=True)
zs=gz[0,np.where(gz[1]==np.max(gz[1]))]
g=gz[1]
z=gz[0]
dz=z[1]-z[0]
g=g/np.sum(g*dz)
g_interp = interpolate.interp1d(z,g)
zmax=np.max(z)
zmin=np.min(z)
#first column redshift, second column redshift distribution
#Loading l
l = np.loadtxt("./data/ell_array_9000.txt", usecols=(0))

for i in range (1):
    seed=12
    map_name=str(i+1)
    rn_seed=1.0
    print(Omfid[i],sig8fid[i])
    #Getting the power spectrum from class for given cosmology
    LambdaCDM=matter_powrspectrum(Omfid[i],Obfid,hfid,nsfid,sig8fid[i])
    Pk2D_bin_20 = np.zeros((len(l), 1+1))
    Pk2D_bin_20[:,0] = l
    #Integrating line of sight, getting convergence powerspectrum
    def Pk_2D_integral_parallelisation_bin_100(p):
        return Pk_2D_integral_bin_100(LambdaCDM,gz,g_interp,p[0],zmin,zmax)
    for i in range(1, 1+1):
        #the local laptop has 16 CPU in total, the number of processes can be adapted according to need
        pool = mp.Pool(processes=8)
        result = pool.map(Pk_2D_integral_parallelisation_bin_100, [[l[j], zs] for j in range(len(l))])
        Pk2D_bin_20[:,i] = np.array(result)
    np.savetxt("./data/convergence_powerspectrum-f1z1f1z1.dat",np.c_[l,result])
    np.savetxt("/project/ls-gruen/users/r.kanaki/LHS_result/2Dconvergence_powerspectrum_result/convergence_powerspectrum-"+map_name+"-f1z1f1z1.dat",np.c_[l,result])
    
    #calculating the shift parameter by cosmomentum
    shift_for_sources=Shift_Parameter.CosMomentum(Omfid[i],Obfid,hfid,nsfid,sig8fid[i])
    
    #generating log-normal map by flask
    #generating the 2D-map by Healpy
    lognormal(shift_for_sources, seed)
    os.chdir("/project/ls-gruen/users/r.kanaki/LHS_result")
    os.rename("map-f1z1.fits", "map_"+map_name+"-f1z1.fits")
    os.chdir("/home/r/R.Kanaki/SuperMukhanov")
    i=i+1
    seed=seed+1
end = time.time()
print('Time taken for execution (seconds): ', end - start)