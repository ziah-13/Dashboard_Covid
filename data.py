import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def filter_data(df, year=None):
    if year is not None:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun📅",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]
    st.subheader("🦠 Data Kasus Covid-19 di Indonesia")
    st.dataframe(df_selected.head(10))
    
    st.subheader("📈 Statistika Deskriptif Pada Dataset")
    st.write(df.describe())

#total kasus
def total_case(df):
    total_kasus = df["New Cases"].sum()
    st.subheader("📊 Total Kasus Keseluruhan")
    return total_kasus

#total kematian
def total_death(df):
    total_kematian = df['New Deaths'].sum()
    return total_kematian

#total sembuh
def total_recovery(df):
    total_sembuh = df['New Recovered'].sum()
    return total_sembuh

#kolom 1
def kolom(df):
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)
    
    co11, co12, co13 = st.columns(3)
    co11.metric(label="Total Kasus 📈", value=kasus, border=True)
    co12.metric(label="Total Kematian 💀", value=kematian, border=True)
    co13.metric(label="Total Sembuh 😻", value=sembuh, border=True)
    
def pie_chart1(df):
    total_kematian=total_death(df)
    total_sembuh=total_recovery(df)
    
    data={
        'Status' : ['Meninggal', 'Sembuh'],
        'Jumlah' : [total_kematian, total_sembuh]
    }
    
    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4de89f', '#ff6459']
    )
    
    st.plotly_chart(fig, use_container_width=True)

def kolomm(df=None):
    # jika tidak dikirim df dari app.py, pakai load_data()
    if df is None:
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