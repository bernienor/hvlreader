# testfile for hvlfilereader

import hvlfilereader as fr
import matplotlib.pyplot as plt
import numpy as np

f = fr.tektronixfile('../T0003CH1.CSV')

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(f.data[:,0],f.data[:,1])
ax1.set_title("Data fra Tektronix skop")
ax1.set_xlabel("time")
plt.show()

#print(f.header)

#print("Instrument type:",f.instrumenttype)
#print("Instrument model:", f.model)
#print("sample rate:",f.samplerate)


#print(d)

