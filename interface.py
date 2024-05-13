import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Análise de venda")
    uploaded_file = st.file_uploader("Coloque o seu arquivo aqui")
    uploaded_file = "relatorio.xlsx"

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file, sheet_name='categorys')

    with st.sidebar:
        selected_analytecs = st.radio("Price or Amount", ["Price", "Amount"], index=None)
        
        if selected_analytecs == "Price":
            colum = "Price Total"
        else:
            colum = "Products Count"

    st.bar_chart(df, x="Category", y= colum )
    st.dataframe(df, use_container_width=True)