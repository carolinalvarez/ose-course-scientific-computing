# The basic idea is to NOT have any regular package imports here.
# This just confuses students.
from IPython import get_ipython
from IPython.core.display import HTML
import numpy as np

ipython = get_ipython()

ipython.magic("load_ext autoreload")
ipython.magic("load_ext lab_black")

ipython.magic("matplotlib inline")
ipython.magic("autoreload 2")

np.set_printoptions(precision=4)
