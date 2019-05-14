# opendap-viewer [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/danwild/opendap-viewer.git/master)

Example of using [itk-jupyter-widgets](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets), with Dask
to visualise 3D hydrodynamic model data in a Jupyter Notebook.

## Run (assuming you have jupyter and conda):

```
conda env create -f environment.yml
conda activate opendap-viewer
jupyer notebook
```

![Screenshot](/screenshots/gbr4.png?raw=true)

## Example data

Data shown for the Great Barrier Reef is pulled from [CSIRO's eReefs products](https://research.csiro.au/ereefs/)
