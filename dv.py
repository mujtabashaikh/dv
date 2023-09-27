import pandas as pd
import streamlit as st
df = pd.DataFrame(
{
    'sr_no' : [1,2,3,4,5],
    'gender' : ['M','F','F','M','M'],
    'weight' : [50,65,60,70,75],
    'height' : [5.5,5.7,5.8,5.9,6.2]
})

st.table(df)
st.line_chart(df['weight'])