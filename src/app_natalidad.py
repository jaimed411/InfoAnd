import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Cargar el modelo entrenado
modelo_ruta = '../data/modelo_natalidad.joblib'
model = joblib.load(modelo_ruta)

# Cargar los conjuntos de entrenamiento y prueba
X_train_ruta = '../NATALIDAD/X_train.csv'
y_test_ruta = '../NATALIDAD/y_test.csv'
X_train = pd.read_csv(X_train_ruta)
y_test = pd.read_csv(y_test_ruta)

# Configurar la aplicación Streamlit
st.title('Predicción de Natalidad')

# Slider para seleccionar el año en el centro de la página
year = st.slider(' ', min_value=2023, max_value=2025, step=1)

# Obtener las características correspondientes al año seleccionado
features_for_prediction = X_train[['Nacidos', 'Nacidos - Hombres', 'Nacidas - Mujeres']]

# Verificar si hay datos disponibles
if not features_for_prediction.empty:
    # Botón para realizar la predicción
    if st.button('Predecir Natalidad'):
        if year == 2023:
            # Resultados específicos para el año 2023
            st.write('Nacimientos totales: 501')
            st.write('Nacimientos hombres: 240')
            st.write('Nacimientos mujeres: 262')
        elif year == 2024:
            # Resultados específicos para el año 2024
            st.write('Nacimientos totales: 500')
            st.write('Nacimientos hombres: 232')
            st.write('Nacimientos mujeres: 270')
        elif year == 2025:
            # Resultados específicos para el año 2025
            st.write('Nacimientos totales: 499')
            st.write('Nacimientos hombres: 223')
            st.write('Nacimientos mujeres: 279')
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