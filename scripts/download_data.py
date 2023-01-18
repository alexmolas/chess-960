import urllib.request
import os

from loggers import get_logger

logger = get_logger(name=__name__)

BASE_PATH = "https://database.lichess.org/chess960/lichess_db_chess960_rated"


def download_month(year: int, month: int, destination_path):
    path = f"{BASE_PATH}_{year}-{month:02}.pgn.zst"
    try:
        logger.info(f"Downloading {path} to {destination_path}")
        urllib.request.urlretrieve(path, destination_path)
        os.system(f"unzstd -f {destination_path}")
        os.remove(destination_path)
    except:
        logger.info(f"{path} doesn't exist")


def download_all_data():
    years = range(2013, 2030)
    months = range(1, 13)
    for year in years:
        for month in months:
            destination_path = f"data/raw/{year}-{month:02}.pgn.zst"
            download_month(year=year, month=month,
                           destination_path=destination_path)


if __name__ == "__main__":
    download_all_data()
