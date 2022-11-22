from typing import List
import urllib.request
import bz2
import lzma
import pathlib
import shutil


from loggers import get_logger

logger = get_logger(name=__name__)

BASE_PATH = "https://database.lichess.org/chess960/lichess_db_chess960_rated"

def download_month(year: int, month: int, destination_path):
    path = f"{BASE_PATH}_{year}-{month:02}.pgn.zst"
    logger.info(f"Downloading {path} to {destination_path}")
    try:
        urllib.request.urlretrieve(path, destination_path)
        input_file = pathlib.Path(destination_path)
        with lzma.open(input_file) as compressed:
            output_path = destination_path[:-4]
            with open(output_path, 'wb') as destination:
                shutil.copyfileobj(compressed, destination)
    except:
        logger.info(f"{path} not found")

def download_all_data():
    years = range(2013, 2020)
    months = range(1, 13)
    for year in years:
        for month in months:
            destination_path = f"data/raw/{year}-{month:02}.pgn.zst"
            download_month(year=year, month=month, destination_path=destination_path)            


if __name__ == "__main__":
    download_all_data()
