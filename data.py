import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df = load_data()
    st.subheader("🦠 Data Kasus Covid-19 di Indonesia")
    st.dataframe(df.head(10))
    
    st.subheader("📈 Statistika Deskriptif Pada Dataset")
    st.write(df.describe())

def total_kasus():
    df = load_data()
    total_kasus = df["Total Cases"].sum()
    st.subheader("📊 Total Kasus Keseluruhan")
    st.success(f"Total seluruh kasus : {total_kasus:,}")

def kolom():
    df = load_data()
    kolom_tampil = [
        "Location",
        "New Cases",
        "New Deaths",
        "New Recovered",
        "New Active Cases",
        "Total Cases",
        "Total Deaths",
        "Total Recovered"
    ]
    df_filtered = df[kolom_tampil]
    st.subheader("📋 Data Kolom Tertentu")
    st.dataframe(df_filtered)

# footer 
st.markdown("---")
st.markdown(
    "<center>© 2026 Mifthahul Fauziah - NPM 184240008</center>",
    unsafe_allow_html=True
)