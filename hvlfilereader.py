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

import matplotlib.pyplot as plt
import numpy as np


class hvlfilereader:
    def __init__(self,filename):
        self.data = np.loadtxt(filename, delimiter=',', skiprows=16)
        #Sample rate calculated from the timestam of the first two samples.Rounded to reduce numerical noise
        self.samplerate =np.round(self.data[:,0][1] - self.data[:,0][0], decimals=20) 
        self.instrumenttype = 'Unknown'

    def identifyfile(self,filename):
        pass


''' Tektronix oscillioscope file reader
Tested on: * DPO2012B

'''
class tektronixfr(hvlfilereader):
    def __init__(self,filename):
        with open(filename) as file:
            self.header = [line.rstrip('\n') for line in file]
        self.header=self.header[:16]
        self.header = [[line.split(',') for line in self.header] ]
        self.data = np.loadtxt(filename, delimiter=',', skiprows=16)
        self.instrumenttype = 'Tektronix oscilioscope'
        self.model = self.header[0][0][1]
        self.samplerate = self.header[0][6][1]

    def identifyfile(self,filename):
        pass

        
''' Rigol oscillioscope file reader
WORK IN PROGRESS!!!
'''

class rigolfr(hvlfilereader):
    def __init__(self,filename):
        with open(filename) as file:
            self.header = [line.rstrip('\n') for line in file]
        self.header=self.header[:2]
        self.header = [[line.split(',') for line in self.header] ]
#        self.instrumenttype = 'Rigol oscilioscope'
#        self.model = self.header[0][0][1]
        self.data-length
        self.samplerate = self.header[0][1][2]
        self.start = self.header[0][1][1]
# Trenger å merge de to datasettene på en grei måte.
#        tidsakse: data = [(-1e-6 + x*1e-7) for x in range(1200)],
#        amplitude: np.loadtxt(filename, delimiter=',', skiprows=2, usecols=0)



