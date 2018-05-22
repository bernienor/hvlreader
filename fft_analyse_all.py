import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import hvlfilereader as fr

files = (
    'testfiles/UB_topp_slutt.CSV', # ingen strekking?
    'testfiles/UB_topp_foer_necking.CSV',
#    'testfiles/UB_topp_necking.CSV',
#    'testfiles/UB_topp_ettermax.CSV',

    'testfiles/UB_bunn_slutt.CSV', # ingen strekking?
    'testfiles/UB_bunn_foer_necking.CSV'
#    'testfiles/UB_bunn_necking.CSV',
#    'testfiles/UB_bunn_rettettermax.CSV',
)

fig, ax = plt.subplots(4,1)

for myfile, idx in zip(files, range(len(files))):
    mydata = fr.tektronixfr(myfile)
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

    ax[idx].plot(frq,abs(Y),'r') # plotting the spectrum
    ax[idx].set_xlim(0,5e6)
    ax[idx].set_ylim(0,0.001)
    ax[idx].set_xlabel(str(myfile).split('/')[1])
    
    #plt.set_xlabel('Freq (Hz)')
    #plt.set_ylabel('|Y(freq)|')
plt.show()
