from search_data_explorer import SearchDataExplorer
import streamlit as st

"""
数据可视化
"""
with st.echo(code_location="below"):
    sde = SearchDataExplorer()
    sde.open()


# import search_data_explorer as sde

# sde.SearchDataExplorer().open()
