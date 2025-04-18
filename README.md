# Standard Landcover Array

> very much a prototype for now

Working with multiple landcover sources can be a hassle. This projects aims at streamlining this process by standardizing everything at the same spatial scale in a N-dimensional array - as the cost of some precision - that can be accessed through xarray in python for example.

Every product has 4 dimensions (x, y, t, b)
- x, y: lat, lon in EPSG:4326
- t: unix timestamp
- b: band, for product containing multiple overlaping information, or originally columnar data

This repo only shows this concept on a [reduced spatial extent](http://bboxfinder.com/#43.500000,1.300000,43.700000,1.600000) for easier data handling on my personal computer.

Final products will look like:
- sla_10m.zarr (or .nc)
- sla_100m.zarr (or .nc)
- ...

The transformation part is built as much as possible on GDAL, to not reinvent the wheel. 