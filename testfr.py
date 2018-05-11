# testfile for hvlfilereader
# 
#
import hvlfilereader as fr
import matplotlib.pyplot as plt
import numpy as np


#f = fr.hvlfilereader('testfiles/tektronix_DPO2012B/T0003CH1.CSV')
#f = fr.tektronixfr('testfiles/tektronix_DPO2012B/T0003CH1.CSV')
f = fr.rigolfr('testfiles/Rigol_DS1054/20180502_1.csv')

fig = plt.figure()
ax1 = fig.add_subplot(111)
print(f.data)
print(f.data[0:10,0],f.data[0:10,1])
ax1.plot(f.data[:,0],f.data[:,1])
ax1.set_xlabel("time")
plt.show()

#print(f.header)

#print("Instrument type:",f.instrumenttype)
#print("Instrument model:", f.model)
print("sample rate:",f.samplerate)


#print(d)
#data = np.loadtxt('../Rigol_DS1054/20180502_1.csv', delimiter=',', skiprows=2, usecols=0)
#data = np.loadtxt('../T0003CH1.CSV', delimiter=',', skiprows=16)
