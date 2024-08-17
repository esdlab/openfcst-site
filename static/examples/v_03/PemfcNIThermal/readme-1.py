import PythonFCST as PythonFCST
from PythonFCST.util.parsers import read_polcurve
import argparse
from itertools import cycle
import pylab as plt
import os
flag=0
path=os.getcwd()
for subdir,dirs,files in os.walk(path):
  for file in files:
      name=os.path.join(subdir,file)
      if 'polarization_curve/regression/test_results.dat' in name:
          fname=name

data01 = read_polcurve(fname)
fig = data01.plot_polcurve(label='Reference Results',
                         format_pol   = 'r-',
                         format_power = 'r--',
                         flag_guides=False)
fname=[]
for subdir,dirs,files in os.walk(path):
  for file in files:
      name=os.path.join(subdir,file)
      if 'polarization_curve.dat' in name:
          fname=name
          flag=1

if flag:
   data02 = read_polcurve(fname)
   fig = data01.plot_polcurve(label='Current Results', fig = fig,
                         format_pol   = 'g-',
                         format_power = 'g--',
                         flag_guides=False)
plt.show()