# Standard Landcover Array

> very much a prototype for now

Working with multiple landcover sources can be a hassle. This projects aims at streamlining this process by standardizing everything at the same spatial scale in a N-dimensional array - as the cost of some precision - that can be accessed through xarray in python for example.

Every product has 4 dimensions (b, y, x, t)
- y, x: in EPSG:3857
- t: unix timestamp
- b: band, for product containing multiple overlaping information, or originally columnar data

This repo only shows this concept on a [reduced spatial extent](http://bboxfinder.com/#43.500000,1.300000,43.700000,1.600000) for easier data handling on my personal computer.

Final products will look like:
- sla_10m.nc (or .zarr)
- sla_100m.nc (or .zarr)
- ...
