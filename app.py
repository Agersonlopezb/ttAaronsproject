import pandas as pd
import streamlit as st
import plotly.express as px
car_data = pd.read_csv('https://github.com/Agersonlopezb/ttAaronsproject/blob/main/vehicles_us.csv') # leer los datos
st.header('Vehiculos Aaron Lopez')
st.write('Esta es mi primer aplicacion funcional.')

hist_button = st.button('Construir histograma ejemplo') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write('Grafico de dispersion.')
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión

st.write('Con casilla de verificacion.')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
