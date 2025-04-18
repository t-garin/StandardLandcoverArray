""" """

import os
import urllib.request
from zipfile import ZipFile


def download_from_url(url: str, dst: str, verbose: bool = True) -> None:
    """
    ...
    """
    if not os.path.exists(dst):
        try:
            urllib.request.urlretrieve(url, dst)
            if verbose:
                print(f"File downloaded successfully: '{dst}'")
        except Exception as e:
            print(f"Error downloading file: {e}")
    else:
        if verbose:
            print(f"File {dst} already exists. Skipping download.")
    return None


def unzip(src: str, verbose=True) -> None:
    """
    ...
    """
    rootdir = os.path.dirname(src)
    subdir = os.path.basename(src).split(".")[0]
    dstdir = os.path.join(rootdir, subdir)
    if not os.path.exists(dstdir):
        with ZipFile(src, "r") as z:
            z.extractall(dstdir)
        if verbose:
            print(f"Unzipped {src}.")
    else:
        if verbose:
            print(f"Folder {dstdir} already exists")
    return None
