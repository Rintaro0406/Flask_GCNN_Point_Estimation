from concurrent.futures import ProcessPoolExecutor
import time
import healpy as hp
import numpy as np
import tensorflow as tf

def downgrade_map_train(map_name):
    path='/project/ls-gruen/users/r.kanaki/LHS_result/train1000'
    MassMap_filename    = path+'/map_'+str(map_name)+'-f1z1.fits'
    MassMap             = hp.read_map(MassMap_filename)
    MassMap  = hp.ud_grade(MassMap,nside_out=128, order_in="RING", order_out="NEST")
    hp.write_map(path+"/NSIDE128_NEST/map"+str(map_name)+".fits", MassMap, overwrite=True)
    return Massmap
    
def downgrade_map_test(map_name):
    path='/project/ls-gruen/users/r.kanaki/LHS_result/test200'
    MassMap_filename    = path+'/map_'+str(map_name)+'-f1z1.fits'
    MassMap             = hp.read_map(MassMap_filename)
    MassMap  = hp.ud_grade(MassMap,nside_out=128, order_in="RING", order_out="NEST")
    hp.write_map(path+"/NSIDE128_NEST/map"+str(map_name)+".fits", MassMap, overwrite=True)
    return Massmap
    
def main():
    print('start')
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    startTime = time.time()
    #arg=np.linspace(1,1000,1000,dtype = int)
    #with ProcessPoolExecutor(max_workers=40) as executor:
        #Srets=executor.map(downgrade_map_train, arg)
    #counter=1
    #for result in rets:
        #counter+=1
        #print(counter)
    arg=np.linspace(1,200,200,dtype = int)
    with ProcessPoolExecutor(max_workers=40) as executor:
        rets=executor.map(downgrade_map_test, arg)
    for result in rets:
        counter+=1
        print(counter)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    print('finish')

if __name__=='__main__':
    main()