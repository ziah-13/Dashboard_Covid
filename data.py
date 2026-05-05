import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    df = df[df["Location"] != "Indonesia"]
    return df

def filter_data(df, year=None, locations=None):

    # filter tahun
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]

    # filter multi provinsi
    if locations:
        df = df[df['Location'].isin(locations)]

    return df

def select_location(df):
    locations = sorted(df['Location'].unique())

    selected_locations = st.sidebar.multiselect(
        "Pilih Provinsi 📍",
        options=locations,
        default=locations   
    )

    return selected_locations

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
    total_kasus = df.sort_values('Date').groupby('Location', as_index = False).last()
    return total_kasus['Total Cases'].sum()

#total kematian
def total_death(df):
    total_kematian = df.sort_values('Date').groupby('Location', as_index = False).last()
    return total_kematian['Total Deaths'].sum()

#total sembuh
def total_recovery(df):
    total_sembuh = df.sort_values('Date').groupby('Location', as_index = False).last()
    return total_sembuh['Total Recovered'].sum()

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
        title='🏥 Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4de89f', '#ff6459']
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
def bar_chart1(df):
    df_last = df.sort_values('Date').groupby('Location', as_index = False).last()
    top5 = df_last.nlargest(5, "Total Deaths")
    
    fig = px.bar(
        top5,
        x='Location',
        y = 'Total Deaths',
        color = 'Total Deaths',
        color_continuous_scale='Reds',
        title = '🔝 5 Provinsi dengan Kematian Tertinggi',
        labels = {'Total Deaths': 'Total Kematian', 'Location': 'Provinsi'}
    )
    
    fig.update_layout(xaxis_title = 'Provinsi', yaxis_title ='Total Kematian', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
    
def bar_chart2(df):
    df_last = df.sort_values('Date').groupby('Location', as_index =False).last()
    top5 = df_last.nlargest(5, 'Total Recovered')
    
    fig = px.bar(
        top5,
        x='Location',
        y = 'Total Recovered',
        color = 'Total Recovered',
        color_continuous_scale = 'Greens',
        title = '🔝 5 Provinsi dengan Kesembuhan Tertinggi',
        labels = {'Total Recovered': 'Total Kesembuhan', 'Location': 'Provinsi'}
        
    )
    
    fig.update_layout(xaxis_title = 'Provinsi', yaxis_title ='Total Kesembuhan', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
    
def map_chart(df, year=None):
    df['Date'] = pd.to_datetime(df['Date'])
    if year :
        df = df[df['Date'].dt.year ==year]
    
    df_agg = df.groupby(['Location', 'Latitude', 'Longitude'], as_index = False) ["New Cases"].sum()
    df_map = df_agg.dropna(subset=['Latitude', 'Longitude', 'New Cases'])
    
    if df_map.empty:
        st.info("⚠️ Tidak ada data untuk ditampilkan di peta")
        return
    
    fig = px.scatter_mapbox(
        df_map, 
        lat = 'Latitude',
        lon = 'Longitude',
        size = 'New Cases',
        color = 'New Cases',
        hover_name = 'Location',
        zoom = 3,
        center={'lat': -2.5, 'lon':118},
        size_max=20,
        opacity = 0.7,
        color_continuous_scale ='OrRd',
        title = f"🤳 Sebaran Kasus Baru di Covid-19 di Indonesia ({year if year else 'Semua Tahun'})"
    )
    
    fig.update_layout(
        mapbox_style = "carto-positron",
        height = 600,
        margin= {'r':0,'t':50,'l':0,'b':0}
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

st.caption("© 2026 Mifthahul Fauziah - NPM 184240008")