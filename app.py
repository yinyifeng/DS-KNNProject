import streamlit as st
import pandas as pd
import numpy as np

st.write("Presentation of Dataset US Housing")

df_housing = pd.read_csv("USA_Housing.csv")
st.dataframe(df_housing)

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)
