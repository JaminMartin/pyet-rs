import json 
import pyet_rs
import matplotlib.pyplot as plt
from pyet.fitting import general_energy_transfer
import numpy as np 
import json
import random
from timeit import default_timer as timer

with open(f'singlecross_20_2pt5_DQ_50000_intrinsic_False.json') as json_file:
    dict = json.load(json_file)
    interact1 = dict['r_components']

with open(f'singlecross_20_5_DQ_50000_intrinsic_False.json') as json_file:
    dict = json.load(json_file)
    interact2 = dict['r_components']

const_dict1  = {'a': 1 , 'b': 490, 'c' : 0.144, 'd':0}
const_dict2  = {'a': 1 , 'b': 490, 'c' : 0.144, 'd': 0}

start = timer()

x = np.arange(0, 21, 0.002).tolist()
x2 = np.arange(0, 21, 0.002).tolist()

start = timer()
y1 = pyet_rs.general_energy_transfer(x, radial_data = interact1, amp =  const_dict1['a'], rad = const_dict1['c'], cr = const_dict1['b'], offset = const_dict1['d'])
y2 = pyet_rs.general_energy_transfer(x, radial_data = interact2, amp = const_dict2['a'], rad = const_dict2['c'], cr = const_dict2['b'], offset = const_dict2['d'])

dt = timer() - start
print (f"Datageneration of {2* len(x)} points using pyet-rs ran in {dt} s using 130 Mb of system memory")

rng = random.Random()

y_noise = [0.01 * rng.normalvariate(0, 1) for _ in range(len(x))]
y2_noise = [0.01 * rng.normalvariate(0, 1) for _ in range(len(x2))]

ydata1 = [y + noise for y, noise in zip(y1, y_noise)]
ydata2 = [y + noise for y, noise in zip(y2, y2_noise)]

plt.plot(x, ydata1)
plt.plot(x2,ydata2)
plt.show(block = False)


# testing 

with open('singlecross_20_2pt5_DQ_50000_intrinsic_False.json') as json_file:
    dict = json.load(json_file)
    interact1 = np.asarray(dict['r_components'])
with open('singlecross_20_5_DQ_50000_intrinsic_False.json') as json_file:
    dict = json.load(json_file)
    interact2 = np.asarray(dict['r_components'])    
const_dict1  = {'a': 1 , 'b': 490, 'c' : 0.144, 'd':0}
const_dict2  = {'a': 1 , 'b': 490, 'c' : 0.144, 'd': 0}
start = timer()
#res = dict_opt(chi, guess, tol = 1e-12)
x = np.arange(0,21,0.002)
x2 = np.arange(0,21,0.002)
start = timer()
y1 = general_energy_transfer(x, interact1, const_dict1)
y2 = general_energy_transfer(x2, interact2, const_dict2)
dt = timer() - start
print (f"Datageneration of {2* len(x)} points using pyet(numpy) ran in {dt} s using >4Gb system memory") 
rng = np.random.default_rng()
y_noise = 0.01 * rng.normal(size=x.size)
y2_noise = 0.01 * rng.normal(size=x2.size)
ydata1 = y1 + y_noise
ydata2 = y2 + y2_noise
 
plt.plot(x, ydata1)
plt.plot(x2,ydata2)
plt.show(block = True)

#Plotting
