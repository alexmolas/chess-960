import pandas as pd


def assign_time_control(x):
    seconds = int(x.split("+")[0])
    if seconds < 180:
        return 'bullet'
    if seconds < 8*60:
        return 'blitz'
    if seconds < 30*60:
        return 'rapid'
    else:
        return 'classical'


def clean_headers_dataframe(df: pd.DataFrame) ->  pd.DataFrame:
    df = df.copy()
    df = df[df['Result'] != "*"]
    df = df[df['TimeControl'] != "-"]
    df = df[df['FEN'] != "?"]
    df = df[df['BlackElo'] != "?"]
    df = df[df['WhiteElo'] != "?"]
    df['WhiteElo'] = df['WhiteElo'].astype(int)
    df['BlackElo'] = df['BlackElo'].astype(int)
    return df


def result_to_points(result):
    if result == '1-0':
        return 1
    if result == '1/2-1/2':
        return 0.5
    return 0


def custom_round(x, base=5):
    return int(base * round(float(x)/base))


def group_fens(df):
    df = df.copy()
    df_g = df.groupby(['pos'], as_index=False)[['white_points', 'black_points']].sum()

    df_g['white_points'] = df_g['white_points'].astype(int)
    df_g['black_points'] = df_g['black_points'].astype(int)
    df_g['count'] = df_g['white_points'] + df_g['black_points']

    df_g.rename(columns={"white_points": "won", "black_points": "lost"}, inplace=True)

    df_g['rate'] = df_g['won'] / df_g['count']

    return df_g


def generate_comparisons(df, n):
    low_positions = df.sort_values("rate").head(n).copy()
    top_positions = df.sort_values("rate").tail(n).copy()
    m = low_positions.merge(top_positions, how='cross', suffixes=("_low", "_top"))
    return m

