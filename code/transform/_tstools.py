import numpy as np
import xarray as xr
import rioxarray as rxr
from math import floor, ceil

# projection used in the final sla
EPSG: int = 3857
# bounding box tuple of area of interest
BBOX: tuple[float] = (144715.3380, 5388389.2728, 178111.1853, 5419133.2594)
# projected epsg 3857 unit is in meters
_step = 100  # in m
_xs = np.arange(floor(BBOX[0]), ceil(BBOX[2]) + _step, _step)
_ys = np.arange(floor(BBOX[1]), ceil(BBOX[3]) + _step, _step)
# BASE N-d array on which we will project everything
BASE = xr.DataArray(
    data=np.full((1, len(_ys), len(_xs), 1), np.nan),
    dims=["b", "y", "x", "t"],
    coords={"b": [0], "y": _ys, "x": _xs, "t": [np.nan]},
)
BASE = BASE.rio.write_crs(f"EPSG:{EPSG}")
