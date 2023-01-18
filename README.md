# Chess960 Analysis
---

Before running any code I recommend you to start a new virtual environment and install all the packages in `requirements.txt`.

## Download data

To generate the dataset needed for the analysis and the ML model you first need to run these steps one by one

1 - Download data `download_data.py`

2 - Decompress data with `decompress_data.py`

3 - Extract headers with `extract_headers.py`

4 - Store data in a single parquet with `compact_all_data.py`


You can also download directly the dataset from Kaggle ([link](https://www.kaggle.com/datasets/alexmolas/chess-960-lichess)), however this dataset is not updated. If you want to use an up to date dataset I recommend to run above scripts.

## Analysis

The analysis is in the `notebooks/AB-testing.ipynb` notebook.

## ML model

The ML model and its evaluation are in the `notebooks/ML.ipynb` notebook.
