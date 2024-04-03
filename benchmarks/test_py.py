from pyet.fitting import general_energy_transfer
import numpy as np
import json
import matplotlib.pyplot as plt
with open(f'singlecross_10_5_QQ_50000.json') as json_file:
        dict = json.load(json_file)
        radial = np.asarray(dict['r_components'])
const_dict1  = {'a': 1 , 'b': 490, 'c' : 0.144, 'd':0}

time = np.arange(0,2,0.001)
time_rs = time.tolist()
radial_rs = radial.tolist

a = 1
b = 490
c = 0.144
d = 0
y = general_energy_transfer(time,radial,const_dict1)
