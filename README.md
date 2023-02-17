# Flask_GCNN_Point_Estimation
My intermediate step of my master thesis. Those codes gives you the point estimation of cosmological parameter from weak lensing mass maps.

1. Using LHS_DES_Y1_Prior.ipynb, you can get the sets of cosmological paramters which is drawn with latin-hyper-cube sampling from given prior cosmology(using the code from https://arxiv.org/abs/2106.03846).

2. Codes in Flask_simulation generates weak lensing convergence maps from given cosmology via just running main.py.
   2.1. Power_Spectrum_3D.py generates the matter power spectrum from the given cosmology using CLASS(https://arxiv.org/abs/1408.4788).
   2.2  Limber_Integration.py generates the convergence power spectrum from matter power spectrum using DES Y3 all combination redshift dirtribution.
   2.3 Shift_Parameter.py generates the log_normal shift parameter from given cosmological parameter using CosMomentum(https://arxiv.org/abs/1710.05162 and https://arxiv.org/abs/1710.05045).
   2.4 Flask_Map.py generats the log normal convergence field from the convergence power spectrum and shift parameter using FLASK (https://arxiv.org/abs/1602.08503).

3. The generated data from Flask_simulation is too big (1200 cosmologies with NSIDE=4096), therefore we should downgrade the mass maps and suitable format for machine learning. There you can use the codes from Downgrading_data.

4. Finally, you can train those mass maps using GCNN layers from DeepSphere(https://arxiv.org/abs/1810.12186 and https://arxiv.org/abs/1810.12186) in order to infer the cosmological parameters.
