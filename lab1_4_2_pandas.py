import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax1, ax2) = plt.subplots(ncols = 2)

Nsamp = 10
po = 1/6.0
bias = 0.05

p6 = po + bias
p = (1 - p6)/5

probVect = [p, p, p, p, p, p6]
cumVect = np.cumsum(probVect)

vals = np.random.random(Nsamp)
dieToss = np.array([1 if i < cumVect[0] else 2 if cumVect[0] <= i < cumVect[1] 
 else 3 if cumVect[1] <= i < cumVect[2] else 4 if cumVect[2] <= i < cumVect[3] 
 else 5 if cumVect[3] <= i < cumVect[4] else 6 for i in vals])

numTossPercent = 100*np.array([(dieToss==i).sum() for i in range(1,7)])/Nsamp

pd.DataFrame({'toss trials': range(Nsamp),'toss value': dieToss}) \
    .plot.scatter('toss trials', 'toss value', ax = ax1)
pd.DataFrame({'toss value': range(1,7),'percent counts': numTossPercent}) \
    .plot.bar('toss value', 'percent counts', width = 0.8, ax = ax2)

