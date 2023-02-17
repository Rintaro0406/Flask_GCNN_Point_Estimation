#memory is dead also 1000GB request
#separate program. First downgrading map using multipleprocessing
#then save to .npz with this

import numpy as np
import healpy as hp
import time
print('start')
startTime = time.time()
nside=128
npix = hp.nside2npix(nside)

####Training data sets
n_samples=1000
map_length=npix
temporary_file = np.zeros((n_samples,map_length))
path_to_train='/project/ls-gruen/users/r.kanaki/LHS_result/train1000'
LHS_data = np.load(path_to_train+'/training_rintaro_LHS_parameter_file.npz')
Omega_M = LHS_data['omega_matter']
Sigma_8=  LHS_data['sigma_8']
print('starting training datasets')
for i in range(1000):
    map_name=str(i+1)
    path=path_to_train+"/NSIDE128_masked/map"+str(map_name)+".fits"
    temporary_file[i]   = hp.read_map(path)
params = {'lognormal_map': temporary_file,
         'Omega_M': Omega_M,
         'sigma_8': Sigma_8}
np.savez('/project/ls-gruen/users/r.kanaki/DeepSphere_data/Versuch1/training_data_NSIDE128_masked.npz', **params)
print('training datasets are finished')

####Test data sets

n_samples=200
map_length=npix
temporary_file = np.zeros((n_samples,map_length))
path_to_test='/project/ls-gruen/users/r.kanaki/LHS_result/test200'
LHS_data = np.load(path_to_test+'/test_rintaro_LHS_parameter_file.npz')
Omega_M = LHS_data['omega_matter']
Sigma_8=  LHS_data['sigma_8']
print('starting test datasets')
for i in range(200):
    map_name=str(i+1)
    path=path_to_test+"/NSIDE128_masked/map"+str(map_name)+".fits"
    temporary_file[i]   = hp.read_map(path)
params = {'lognormal_map': temporary_file,
         'Omega_M': Omega_M,
         'sigma_8': Sigma_8}
np.savez('/project/ls-gruen/users/r.kanaki/DeepSphere_data/Versuch1/test_data_NSIDE128_masked.npz', **params)
print('test datasets are finished')

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
print('finish')