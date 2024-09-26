#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import re
import linecache
import math
import shutil
import numpy as np
# import matplotlib.pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])


import matplotlib.pyplot
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
     BSPlotter,BSPlotterProjected,DosPlotter
     
dos_vasprun=Vasprun("./dos/vasprun.xml")
dos_data=dos_vasprun.complete_dos

bs_vasprun=Vasprun("./bands/vasprun.xml",parse_projected_eigen=True)
bs_data=bs_vasprun.get_band_structure(line_mode=1)

plt_2=BSDOSPlotter(bs_projection='elements', dos_projection='elements')
plt_2.get_plot(bs=bs_data,dos=dos_data)
matplotlib.pyplot.savefig('plt_2.png',img_format='png')

