from classy import Class

#more realistic redshift distribution
def matter_powrspectrum(Omfid,Obfid,hfid,nsfid,sig8fid):
    LambdaCDM = Class()
    h2=hfid*hfid
    LambdaCDM.set({'omega_b':Obfid*h2,'omega_cdm':(Omfid-Obfid)*h2,'h':hfid,'n_s':nsfid,
                    'tau_reio':0.05430842,'N_ur':3.046,'z_max_pk':3.0,'sigma8':sig8fid,'non linear':'HALOFIT'})
    LambdaCDM.set({'output':'mPk','P_k_max_1/Mpc':200.})
    # run class
    LambdaCDM.compute()
    return LambdaCDM
    