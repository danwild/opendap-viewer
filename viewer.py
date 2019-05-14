# Install dependencies for this example
# Note: This does not include itk-jupyter-widgets, itself
import dask.array as da
from dask.distributed import Client
from netCDF4 import Dataset
import netCDF4 as nc
import dask
import numpy
from itkwidgets import view
import sys

#  !{sys.executable} - m pip install dask toolz scikit-image matplotlib itk-io itkwidgets netCDF4
#  !{sys.executable} - m pip install toolz itk-io itkwidgets

# create dataset from Unidata's opendap endpoint
url = 'http://dapds00.nci.org.au/thredds/dodsC/fx3/model_data/gbr4_2.0.ncml'
ds = Dataset(url)


# !{sys.executable} - m pip install dask distributed --upgrade

client = Client(n_workers=2)

temp = ds['temp'][20000, :, :, :]
arr = da.from_array(temp)
arr

view(arr[:, :, :], shadow=False, gradient_opacity=0.4)
