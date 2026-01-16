import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Panel de anuncios de venta de coches")

car_data = pd.read_csv("vehicles_us.csv")

st.write("Vista previa del dataset:")
st.dataframe(car_data.head(10))

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión: precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
