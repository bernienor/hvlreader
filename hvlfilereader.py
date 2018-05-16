# Samleklasse for import av datafiler inn i Python.
#
# The idea is to make a general importer to easy the work involved in setting
# up new programs for post processing of test data.
#
# Main attributes:
# * data ( the data set)
# * sample_interval
# * timestamp_of_first_sample (default 0)
#
#
# Nice to have attributes:
# * scale (default 1)
# * unit (default "")
# * source_file_type (subclass of reader)
# * file_timestamp (timestamp in the filesystem of the file)
# * data_timestamp (time and date read from the file)
# * Source name/brand/identifier

import numpy as np


class hvlfilereader:
    """ Generic file reader for various fileformats
    """
    def __init__(self, filename):
        self.data = np.loadtxt(filename, delimiter=',', skiprows=16)
        self.samplerate = np.round(self.data[:, 0][1] - self.data[:, 0][0],
                                   decimals=20)
        self.instrumenttype = 'Unknown'

    def identifyfile(self, filename):
        pass


class tektronixfr(hvlfilereader):
    """ Tektronix oscillioscope file reader tested on: DPO2012B
    """
    def __init__(self, filename):
        headersize = 16
        with open(filename) as file:
            self.header = [next(file).rstrip('\n') for x in range(headersize)]
        self.header = self.header[:16]
        self.header = [[line.split(',') for line in self.header]]
        self.data = np.loadtxt(filename, delimiter=',', skiprows=headersize)
        self.instrumenttype = 'Tektronix oscilioscope'
        self.model = self.header[0][0][1]
        self.samplerate = float(self.header[0][6][1])

    def identifyfile(self, filename):
        pass


''' Rigol oscillioscope file reader

'''


class rigolfr(hvlfilereader):
    def __init__(self, filename):
        headersize = 2
        with open(filename) as file:
            self.header = [next(file).rstrip('\n') for x in range(headersize)]
        self.header = self.header[:2]
        self.header = [[line.split(',') for line in self.header]]
        self.instrumenttype = 'Rigol oscilioscope'
        self.samplerate = float(self.header[0][1][2])
        self.start = float(self.header[0][1][1])
        ampl = np.loadtxt(filename, delimiter=',', skiprows=headersize,
                          usecols=0)
        tstamp = np.array([(self.start + (x * self.samplerate))
                          for x in range(ampl.size)])
        self.data = np.dstack((tstamp, ampl))[0]


'''
A note on importing data:
It is hard to find the right format for the data. Looking at the code above
there is a few tricks:

We start by importing the header from the file:
    with open(filename) as file:
        self.header = [line.rstrip('\n') for line in file]

This is not very efficient as we read the whole file. Need to cut down to two
lines

self.header=self.header[:2]
        self.header = [[line.split(',') for line in self.header]]

This was improved to a more efficient code:
        headersize=2
        with open(filename) as file:
            self.header = [next(file).rstrip('\n') for x in range(headersize)]
This only reads the number of lines neccecerry for the task ahead.

The header is now an array of text-strings. We need to extracts some float
values.
>>> value = '1e-7'
>>> value
'1e-7'
>>> float(value)
1e-07
We use this directly to get the samplerate:
self.samplerate = float(self.header[0][1][2])


For the tektronixfr:
>>> data = np.loadtxt('../T0003CH1.CSV', delimiter=',', skiprows=16)
>>> data
array([[ 2.06000e-06, -8.90625e-03],
       [ 2.06100e-06, -7.73437e-03],
       [ 2.06200e-06, -9.76562e-03],
       ...,
       [ 1.02057e-04,  4.48437e-01],
       [ 1.02058e-04,  4.53516e-01],
       [ 1.02059e-04,  4.59844e-01]])

For rigolfr:
>>> ampl = np.loadtxt('../Rigol_DS1054/20180502_1.csv', delimiter=',',
                      skiprows=2, usecols=0)
>>> ampl
array([ 0.   ,  0.   ,  0.   , ..., -0.028, -0.092, -0.092])

To add the timeline. We need to recalculate it from the information in
the header.
>>> ampl.size
1200
# tstamp=np.array([(self.start + (x * self.samplerate))
#        for x in range(ampl.size)])
>>> tstamp=np.array([(-9.6e-6 + (x * 1e-7)) for x in range(ampl.size)])
>>> tstamp
array([-9.600e-06, -9.500e-06, -9.400e-06, ...,  1.101e-04,  1.102e-04,
        1.103e-04])
Now, all we need to do is to merge or join these two array together.
data=np.dstack((tstamp,ampl))[0]
>>> data
array([[-9.600e-06,  0.000e+00],
       [-9.500e-06,  0.000e+00],
       [-9.400e-06,  0.000e+00],
       ...,
       [ 1.101e-04, -2.800e-02],
       [ 1.102e-04, -9.200e-02],
       [ 1.103e-04, -9.200e-02]])
This way the data array has the same form as data arrays imported using the
other filereaders.
'''
