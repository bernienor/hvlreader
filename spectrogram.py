import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import hvlfilereader as fr

#mydata = fr.tektronixfr('testfiles/UB_bunn_foer_necking.CSV')
#mydata = fr.tektronixfr('testfiles/UB_bunn_necking.CSV')
#mydata = fr.tektronixfr('testfiles/UB_bunn_rettettermax.CSV')
#mydata = fr.tektronixfr('testfiles/UB_bunn_slutt.CSV')
#mydata = fr.tektronixfr('testfiles/UB_topp_ettermax.CSV')
#mydata = fr.tektronixfr('testfiles/UB_topp_foer_necking.CSV')
#mydata = fr.tektronixfr('testfiles/UB_topp_necking.CSV')
#mydata = fr.tektronixfr('testfiles/UB_topp_slutt.CSV')

mydata = fr.tektronixfr('testfiles/UB_bunn_foer_necking.CSV')
t = mydata.data[:, 0]

fs = 1 / mydata.samplerate
n = mydata.data.shape[0]
k = np.arange(n)
T = n/fs

#amp = 2 * np.sqrt(2)
#noise_power = 0.01 * fs / 2
#time = np.arange(N) / float(fs)
#mod = 500*np.cos(2*np.pi*0.25*time)
#carrier = amp * np.sin(2*np.pi*3e3*time + mod)
#noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
#noise *= np.exp(-time/5)
#x = carrier + noise

f, t, Sxx = signal.spectrogram(mydata.data[: ,1], fs, nperseg=1024, scaling='density')
fig, ax = plt.subplots()
ax.pcolormesh(t, f, Sxx)
ax.ylabel('Frequency [Hz]')
ax.xlabel('Time [sec]')
ax.set_ylim(0,1e7)
plt.show()