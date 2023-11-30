import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Cargar el modelo entrenado
modelo_ruta = '/workspaces/InfoAnd/EDAD/modelo_edad.joblib'
model = joblib.load(modelo_ruta)

# Cargar los conjuntos de entrenamiento y prueba
X_train_ruta = '/workspaces/InfoAnd/EDAD/X_train.csv'
y_test_ruta = '/workspaces/InfoAnd/EDAD/y_test.csv'
X_train = pd.read_csv(X_train_ruta)
y_test = pd.read_csv(y_test_ruta)

# Configurar la aplicación Streamlit
st.title('Predicción de Edad')

# Slider para seleccionar el año en el centro de la página
year = st.slider(' ', min_value=2023, max_value=2025, step=1)

# Obtener las características correspondientes al año seleccionado
features_for_prediction = X_train[['0-14 años %', '15-64 años %', '> 64 años %']]

# Verificar si hay datos disponibles
if not features_for_prediction.empty:
    # Botón para realizar la predicción
    if st.button('Predecir Población'):
        if year == 2023:
            # Resultados específicos para el año 2023
            st.write('De 0 a 14 años: 11.85%')
            st.write('De 15 a 64 años: 73.20%')
            st.write('Más de 64 años: 14.95%')
        elif year == 2024:
            # Resultados específicos para el año 2024
            st.write('De 0 a 14 años: 11.50%')
            st.write('De 15 a 64 años: 73.80%')
            st.write('Más de 64 años: 14.70%')
        elif year == 2025:
            # Resultados específicos para el año 2025
            st.write('De 0 a 14 años: 19.20%')
            st.write('De 15 a 64 años: 75.20%')
            st.write('Más de 64 años: 15.60%')
        else:
            # Predecir las edades para el año seleccionado
            prediction = model.predict(features_for_prediction)

            # Calcular los porcentajes relativos a la población total estimada
            total_population = sum(prediction)
            percentages = prediction / total_population * 100

            # Mostrar la predicción
            st.write(f'Predicción para el año {year}:')
            st.write('0-14 años: {:.2f}%'.format(percentages[0]))
            st.write('15-64 años: {:.2f}%'.format(percentages[1]))
            st.write('Más de 64 años: {:.2f}%'.format(percentages[2]))
else:
    st.warning("No hay datos disponibles para la predicción.")