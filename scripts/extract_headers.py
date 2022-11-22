import os

from chess.pgn import Headers
import chess.pgn
import pandas as pd
import typer

from loggers import get_logger

logger = get_logger(name=__name__)

def read_headers(path: str) -> list[Headers]:
    # todo: remove hardcoded path
    pgn = open(path)
    headers = []
    while pgn:
        header = chess.pgn.read_headers(pgn)
        if header is not None:
            headers.append(header)
        else:
            break
    return headers

def extract_headers(path: str):

    for _, _, files in os.walk(path):
        for file in files:
            if file.endswith('pgn'):
                logger.info(f"Reading {file}")
                headers = read_headers(os.path.join(path, file))
                df_headers = pd.DataFrame(headers)
                filename = file.split(".")[0]
                df_headers.to_parquet(f"data/headers/{filename}.parquet")
        
        
if __name__ == "__main__":
    typer.run(extract_headers)