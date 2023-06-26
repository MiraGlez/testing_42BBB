import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
#st.set_page_config(page_title="TESTING PROJECT", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----

df = pd.read_excel("wdbc_mfg.xlsx",sheet_name="wdbc")

st.dataframe(df)


