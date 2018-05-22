import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import hvlfilereader as fr

files = ['testfiles/UB_bunn_foer_necking.CSV',
            'testfiles/UB_bunn_necking.CSV',
            'testfiles/UB_bunn_rettettermax.CSV',
            'testfiles/UB_bunn_slutt.CSV',
            'testfiles/UB_topp_ettermax.CSV',
            'testfiles/UB_topp_foer_necking.CSV',
            'testfiles/UB_topp_necking.CSV',
            'testfiles/UB_topp_slutt.CSV' ]
for myfile in files:
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

    fig, ax = plt.subplots()
    ax.plot(frq,abs(Y),'r') # plotting the spectrum
    ax.set_xlim(1e6,2e6)
    #plt.set_xlabel('Freq (Hz)')
    #plt.set_ylabel('|Y(freq)|')
    plt.show()
