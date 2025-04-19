import time

import xarray as xr
import rioxarray as rxr

from tqdm import tqdm

from _tstools import BASE, EPSG


def year_range():
    return range(1975, 2030 + 1, 5)


def da_gen():
    for year in tqdm(year_range()):
        path = f"../../data/raw/ghs-pop/{year}/GHS_POP_E{year}_GLOBE_R2023A_54009_100_V1_0_R4_C19.tif"
        da = rxr.open_rasterio(path)
        da = da.rio.reproject_match(BASE)
        # da.shape = (band, y, x) because of rxr
        # BAND.shape = (b, y, x, t), so when reshaping
        # it will only had a length 1 dim with nan val
        """
        TODO: BE CAREFUL IF BASE AND da DONT MATHC RESOLUTION
        IT WILL CHANGE THE POPULATION AMOUNT PER PIXEL
        """
        yield BASE.copy(data=da.values.reshape(BASE.shape))


def unix_time_gen():
    for year in year_range():
        # set the unix time to first january of the year
        struct_time = time.strptime(f"{year}", "%Y")
        # assume we dont have landcover that varies by the millisecond
        yield round(time.mktime(struct_time))


# concat along time
ds = xr.concat(list(da_gen()), dim="t")
# add actual time information
ds["t"] = list(unix_time_gen())
# remove 'spatial_ref' that was used to reproject using rxr
ds = ds.drop_vars("spatial_ref")
# add attrs
ds.attrs = {
    "b_unit": "population amount per pixel",
    "y_unit": "latitude",
    "x_unit": "longitude",
    "t_unit": "unix time",
    "EPSG": EPSG,
    "resolution": "100m",
}
ds.to_netcdf("../../data/sla/single/sla_ghs_pop_100m.nc")
