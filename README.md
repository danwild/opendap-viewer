# opendap-viewer [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/danwild/opendap-viewer.git/master)

Example of using [itk-jupyter-widgets](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets), with Dask
to visualise 3D hydrodynamic model data in a Jupyter Notebook.

## Run:

##### Option #1

Run remotely via binder - follow the [badge link](https://binder.pangeo.io/v2/gh/danwild/opendap-viewer.git/master).
You also need to run in a jupyter lab terminal:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager itk-jupyter-widgets
```

##### Option #2

Run locally (requires jupyter and conda install)

```
conda env create -f environment.yml
conda activate opendap-viewer
jupyer notebook
```

![Screenshot](/screenshots/gbr4.png?raw=true)

## Example data

Data shown for the Great Barrier Reef is pulled from [CSIRO's eReefs products](https://research.csiro.au/ereefs/)
