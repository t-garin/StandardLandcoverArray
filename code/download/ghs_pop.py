from ._dltools import download_from_url, unzip


def main(verbose: bool = False) -> None:
    for year in range(1975, 2030 + 1, 5):
        url = f"https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E{year}_GLOBE_R2023A_54009_100/V1-0/tiles/GHS_POP_E{year}_GLOBE_R2023A_54009_100_V1_0_R4_C19.zip"
        path = f"../data/raw/ghs-pop/{year}.zip"
        download_from_url(url, dst=path, verbose=verbose)
        unzip(src=path, verbose=verbose)
