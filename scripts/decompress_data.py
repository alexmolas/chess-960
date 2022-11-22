import zstandard
import os
import pathlib
import shutil
from loggers import get_logger

import typer

logger = get_logger(__name__)

destination_dir = pathlib.Path("data/decompressed")

def decompress_zstandard_to_folder(input_file):
    input_file = pathlib.Path(input_file)
    with open(input_file, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()
        output_path = pathlib.Path(destination_dir) / input_file.stem
        with open(output_path, 'wb') as destination:
            decomp.copy_stream(compressed, destination)

def decompress_all_data(path: str):
    for dirpath, _, files in os.walk(path):
        for file in sorted(files):
            if file.endswith('zst'):
                input_file = pathlib.Path(f"{dirpath}/{file}")
                logger.info(f"Decompressing {input_file}")
                decompress_zstandard_to_folder(input_file)

if __name__ == "__main__":
    typer.run(decompress_all_data)
