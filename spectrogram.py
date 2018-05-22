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
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

# sp = np.fft.rfft(mydata.data[:, 1] )

Y = np.fft.fft(mydata.data[:, 1])/n # fft computing and normalization
Y = Y[range(int(n/2))]

plt.plot(frq,abs(Y),'r') # plotting the spectrum
plt.set_xlabel('Freq (Hz)')
plt.set_ylabel('|Y(freq)|')
plt.show()

#amp = 2 * np.sqrt(2)
#noise_power = 0.01 * fs / 2
#time = np.arange(N) / float(fs)
#mod = 500*np.cos(2*np.pi*0.25*time)
#carrier = amp * np.sin(2*np.pi*3e3*time + mod)
#noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
#noise *= np.exp(-time/5)
#x = carrier + noise

f, t, Sxx = signal.spectrogram(mydata.data[: ,1], fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()