import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax1, ax2) = plt.subplots(ncols = 2)

Nsamp = 10
binNumber = 20

df = pd.DataFrame({'trial':range(Nsamp), 'value': np.random.random(Nsamp)})
df.plot('trial', 'value', kind = 'scatter', ax = ax1)
df.hist('value', bins = binNumber, ax = ax2)

print('mean', df.value.mean())
print('std', df.value.std())