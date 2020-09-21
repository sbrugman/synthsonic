from io import StringIO
from os import getenv

import pandas as pd
import requests
import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder

DISPLAY_ROWS = 6


def _bytes_to_df(data: bytes) -> pd.DataFrame:
    data = StringIO(str(data, 'utf-8'))

    return pd.read_csv(data)


def _df_to_bytes(df: pd.DataFrame) -> bytes:
    _result = StringIO()

    df.to_csv(_result, mode='w', encoding='UTF_8', index=False)

    result = _result.getvalue().encode('utf-8')

    return result


def process(input_data: StringIO, server_url: str) -> str:
    m = MultipartEncoder(
        fields={'file': ('filename', input_data, 'text/csv')}
    )

    r = requests.post(server_url,
                      data=m,
                      headers={'Content-Type': m.content_type},
                      timeout=8000)

    return r.content.decode('utf-8')


url = getenv('API_URL', 'http://localhost:8000')
endpoint = '/synthesize'

# UI -------------------------------------------------------------------------------------------------------------------

st.title('Synthsonic - synthetic data service')
st.write('''Obtain synthetic data based on real data.''')  # description and instructions

input_data = st.sidebar.file_uploader('insert csv data with headers')  # image upload widget

if input_data is None:
    st.write("Insert not empty CSV!")
else:
    st.markdown('### Raw data')
    _raw_data = _bytes_to_df(input_data.getvalue().encode('utf-8')).head(DISPLAY_ROWS)
    st.write(_raw_data)

if st.sidebar.button('Get synthetic data') and input_data:
    synthetic_data_bytes = process(input_data, url + endpoint)
    data = StringIO(synthetic_data_bytes)

    df = pd.read_csv(data)

    st.markdown('### Synthetic data')
    st.write(df.head(DISPLAY_ROWS))
