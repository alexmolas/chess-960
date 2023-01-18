import pandas as pd

import typer


def compact_folder(path: str):
    columns = ['UTCDate', 'Black', 'BlackElo', 'BlackTitle', 'FEN',
               'Result', 'Site', 'TimeControl',
               'UTCTime', 'White', 'WhiteElo',
               'WhiteTitle']
    df = pd.read_parquet(path, columns=columns)
    df.to_parquet("data/compacted/compact_data.parquet")


if __name__ == "__main__":
    typer.run(compact_folder)
