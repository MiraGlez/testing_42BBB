import streamlit as st
import pandas as pd
import numpy as np

st.write("Hola Miri")

df = pd.read_csv("ACPs_Breast_cancer.csv")

print(df.isnull())
print(df.isnull().sum())

print (df)


