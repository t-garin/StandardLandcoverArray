# Standard Landcover Array

Working with multiple landcover sources can be a hassle. This projects aims at streamlining this process by standardizing everything in a N-dimensional array - as the cost of some precision - that can be accessed through xarray in python for example.

Every product has 4 dimensions (x, y, t, b)
- x, y: lat, lon in EPSG:4326
- t: unix timestamp
- b: band, for product containing multiple overlaping information, or originally columnar data
