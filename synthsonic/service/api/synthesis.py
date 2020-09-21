from io import StringIO

import pandas as pd


def _bytes_to_df(data: bytes) -> pd.DataFrame:
    data = StringIO(str(data, 'utf-8'))

    return pd.read_csv(data)


def _df_to_bytes(df: pd.DataFrame) -> bytes:
    _result = StringIO()

    df.to_csv(_result, mode='w', encoding='UTF_8', index=False)

    result = _result.getvalue().encode('utf-8')

    return result


# @todo implement with our model
def get_model():
    return None


# @todo implement this, for now it's just a pass-through
def get_data(model, bytes_data, rows=5) -> bytes:
    df = _bytes_to_df(bytes_data).head(rows)

    result = _df_to_bytes(df)

    return result
