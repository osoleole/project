# This is the test program.
# It is started by observer.
# Creates numpy array of random numbers and pickle it to file

import yaml
import numpy as np
import pickle


with open("config_alg_1.yaml", 'r') as f:
    cfg = yaml.load(f)

vs = cfg['model']['vector_size'][0]

rnd_ar = np.random.rand(vs,10)
rnd_ar.dump("dump1")

print(np.load("dump1"))
