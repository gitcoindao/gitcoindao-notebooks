from zipfile import ZipFile
from pathlib import Path


def open_largest_file_in_zip(zip_path: Path, callback: callable) -> object:
    with ZipFile(zip_path) as zip_file:
        file_list = zip_file.filelist
        largest_file = list(sorted(file_list, key=lambda x: x.file_size))[-1]
        with zip_file.open(largest_file.filename) as fid:
            return callback(fid)
