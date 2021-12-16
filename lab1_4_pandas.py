import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)

nsamp = 100
probCoin = 0.8
vals = np.random.random(nsamp)
df = pd.DataFrame({'trial':range(nsamp), 'value': vals, 'flips': 
                   [0 if i < probCoin else 1 for i in vals]})
print('coin flips mean', df.flips.mean())
print('coin flips std', df.flips.std())    
numTails = df.flips.sum()
binNumber = 20
binNumberFlips = 10

df.plot('trial', 'value', kind = 'scatter', ax = ax1)
df.hist('value', bins = binNumber, ax = ax2)
df.plot('trial', 'flips', kind = 'scatter', ax = ax3)
tailsPercent = 100 * (numTails/nsamp)
headsPercent = 100 - tailsPercent
ax4.bar([0,1], [headsPercent, tailsPercent])
ax4.set_xlabel('flips')
ax4.set_ylabel('counts')
fig.tight_layout()

