"""
Monte Carlo to generate exponentially distributed random values
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# good to group parameters at beginning
# of code so you can find/modify them easily
Nsamp = 100
binNumber = 20
cumBinNumber = 100
a = 1

def cumExpModel(a, x):
    return 1 - np.exp(-a*x) # x is already a np array
# could also use cumExpModel = lambda a, x : 1-np.exp(-a*x)
vals = [-(1/a) * np.log(1-i) for i in np.random.random(Nsamp)]
    
print('mean', np.mean(vals))
print('std', np.std(vals))

histValues, binEdges = np.histogram(vals, cumBinNumber)
cumHistValues = np.cumsum(histValues)/Nsamp
# convert bin edges to bin center position
# could use [0.5 * (binEdges[i] + binEdges[i + 1]) for i in range(len(binEdges) - 1)]
binCenter = (binEdges[:-1]+binEdges[1:])/2 # this is shorter and more efficient

fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)

df = pd.DataFrame({'trials': list(range(Nsamp)), 'value': vals,\
                   'value ': binCenter, 'cumulative co': cumHistValues,\
                       'cumulative counts': cumExpModel(a, binCenter)})
    
df.plot('trials', 'value', kind = 'scatter', ax = ax1)
df.hist('value', bins = binNumber, ax = ax2)
df.plot('value ', 'cumulative co', kind = 'scatter', ax = ax3)
df.plot('value ', 'cumulative counts', kind = 'scatter', ax = ax4)

np.savetxt('nonuniform.csv', 
           np.transpose([binCenter, cumHistValues]), delimiter = ",")