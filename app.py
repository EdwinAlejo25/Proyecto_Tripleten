import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Construcción Histograma')

car_data = pd.read_csv('C:/Users/User/Proyecto_Tripleten/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Construir un gráfico de dispersión')
if hist_button_2:
        st.write('Creación de un un gráfico de dispersión para el conjunto de datos')
        fig_2 = px.scatter(car_data, x="price", y="model_year")
        st.plotly_chart(fig_2, use_container_width=True)