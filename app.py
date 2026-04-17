import streamlit as st
from data import show_data, total_kasus, kolom

def judul():
    st.title("📊 Dashboard Covid-19")
    st.write("Selamat Datang di Dashboard ini!")

# sidebar
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# halaman home
if menu == "Home":
    judul()

# halaman data
elif menu == "Halaman Data":
    total_kasus()   
    show_data()     
    kolom()         

# footer
st.markdown("---")
st.markdown(
    "<center>© 2026 Mifthahul Fauziah - NPM 184240008</center>",
    unsafe_allow_html=True
)