import streamlit as st
from data import *

def judul():
    st.title("📊 Dashboard Covid-19")
    st.write("Selamat Datang di Dashboard ini!")

# sidebar
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# halaman home
if menu == "Home":
    judul()
    year = select_year()
    df = load_data()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)
    kolom(df_filtered)
    pie_chart1(df_filtered)
    bar_chart1(df_filtered)
    bar_chart2(df_filtered)
    map_chart(df_filtered)


# halaman data
elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered) 
    kolomm()     

st.caption("© 2026 Mifthahul Fauziah - NPM 184240008")

