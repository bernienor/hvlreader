# plotting av data

import matplotlib.pyplot as plt
import numpy as np
import argparse


def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
    data = np.loadtxt(file_name, delimiter=',', skiprows=16)
    return data


# Lar programmet håndtere argumenter. Slik at vi enkelt kan plotte en eller
# mange filer.
parser = argparse.ArgumentParser(
    description='Plotting files stored in CSV-format from a Tektronix scope')
parser.add_argument('filename', metavar='Filename', type=str, nargs='+',
                    help="The filename you'd like to plot")
parser.add_argument('--column', default=1, metavar='Column', type=int,
                    help="Column to display. (1 or higher)")
# parser.add_argument('separator', metavar)
# Vi må prosessere de argumentene som er sendt med programmet
args = parser.parse_args()

# Gå gjennom lista over filer og plot dem en etter en.
for filename in args.filename:
    data = read_datafile(filename)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(data[:, 0], data[:, args.column])
    ax1.set_title("Data fra Tektronix skop")
    ax1.set_xlabel("time")
    plt.show()
