import numpy as np
import os 
def lognormal(shift_for_sources, rn_seed):
    gz=np.loadtxt("/project/ls-gruen/users/r.kanaki/LHS_result//DeepSphereTest1/nofz_DESY3_source_BIN1234.tab", usecols=(0,1),unpack=True)
    foj=open("/home/r/R.Kanaki/Masterarbeit/Feburuar_2023_Masterarbeit/Point_Estimation_From_Flask_Maps/Flask_simulation/data/lognormal-info.dat","w")
    foj.writelines("# Field number, z bin number, mean, shift, field type, zmin, zmax""\n")
    foj.writelines("# Types: 1-galaxies 2-shear""\n")
    foj.writelines("     {FieldNumber:01d}      {zBinNumber:01d}   {mean:03f}   {shift:03f}      {FieldType:01d}   {zmin:06f}   {zmax:06f}".format(FieldNumber=1, zBinNumber=1, mean=0, shift=shift_for_sources, FieldType=2,zmin=np.min(gz[0]),zmax=np.max(gz[0])))
    foj.close()
    os.chdir("/home/r/R.Kanaki/Packages/flask")
    from pyFlask import flask
    #print(os.path.abspath(os.getcwd()))
    #print(os.path.abspath(os.getcwd()))
    #pyFlask.flask(["flask","../SuperMukhanov/Lognormal.config"])
    #pyFlask.flask(["flask","../SuperMukhanov/SuperMukhanov.config"])
    flask(["flask","./data/lognormal.config","RNDSEED:",str(rn_seed)])
    os.chdir("../..//Masterarbeit/Feburuar_2023_Masterarbeit/Point_Estimation_From_Flask_Maps/Flask_simulation")
    
#if __name__ == '__main__':
    #flask(shift_for_sources,rn_seed)
    