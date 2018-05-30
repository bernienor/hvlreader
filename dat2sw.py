'''
Converts airfoil .datfiles to solidworks coordinate files.
Z value can be given as argument, 0.0 as default.


'''

import argparse

# set up the parser
parser = argparse.ArgumentParser(
    description='Airfoil .dat to SolidWorks coordinate file converter')
parser.add_argument('filename', metavar='Filename', type=str,
                    help="The filename of the airfoil you'd like to convert")
parser.add_argument('--Z', default=0.0, metavar='Z', type=float,
                    help="optional Z-axis value, default is 0.0")
args = parser.parse_args()

with open(args.filename) as airfoilfile:
    airfoil = airfoilfile.readlines()[1:]
    for line in airfoil:
        data = line.split()
        print(data[0], '\t', data[1], '\t', args.Z)
