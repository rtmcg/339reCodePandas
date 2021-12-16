"""
Monte Carlo to simulate an unfair coin
"""

import matplotlib.pyplot as plt
import numpy as np

nsamp = 100
probCoin = 0.8

coinFlips = [] # if coinFlips = np.array([]) is used, 
# appending is done as coinFlips = np.append(coinFlips, 1) or with 0 
# since a list appends in place while numpy returns a copy with append
# so I usualy use lists and append and make it into an array or series in a dataframe later
values = np.random.random(nsamp) # array of nsamp random values
for i in values:
    if i < probCoin:
        coinFlips.append(0)
    else:
        coinFlips.append(1)
    
numTails = sum(coinFlips)

print('coin flips mean', np.mean(coinFlips))
print('coin flips std', np.std(coinFlips))

binNumber = 20
binNumberFlips = 10

plt.figure()
plt.subplot(2,2,1) # can also write plt.subplot(221)
plt.plot(values, 'o') # can plot just y if x is just the index array 
plt.xlabel('trials')
plt.ylabel('values')

plt.subplot(2,2,2)
plt.hist(values, bins=binNumber)
plt.xlabel('value')
plt.ylabel('counts')

plt.subplot(2,2,3)
plt.plot(coinFlips, 'o')
plt.xlabel('trials')
plt.ylabel('flips')

plt.subplot(2,2,4)
tailsPercent = 100 * (numTails/nsamp)
headsPercent = 100 - tailsPercent
plt.bar([0,1], [headsPercent, tailsPercent], width = 0.8)
plt.xlabel('flips')
plt.ylabel('counts')

plt.tight_layout() 