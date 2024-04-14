import streamlit as st
import pandas as pd
import sqlite3
import altair as alt

# Título de la página
st.set_page_config(layout='wide')
st.title('Tablero de Control de RRHH')

min_sal = st.slider('Salario', 50*1e3, 100*1e3, step=1e3)

# Conexión a la base de datos SQLite y carga de datos
conn = sqlite3.connect('rrhh.db')
data = pd.read_sql('SELECT * FROM empleados', conn)
data = data[data['salario'] > min_sal]

st.metric(label="Temp", value="273 K", delta="1.2 K")

# Estadísticas sobre los empleados
total_empleados = len(data)
salario_promedio = data['salario'].mean()
salario_maximo = data['salario'].max()
salario_minimo = data['salario'].min()

# Filas y columnas para organizar las visualizaciones
col1, col2 = st.columns(2)

# Visualización de la tabla de datos
with col1:
    st.subheader('Datos de Empleados')
    st.dataframe(data, height=400, hide_index=True)

# Gráfico de barras para distribución de salarios
with col2:
    salario_chart = alt.Chart(data).mark_bar().encode(
        alt.X('salario:Q', bin=True),
        y='count()',
        tooltip=['count()']
    ).properties(
        width=300,
        height=200
    ).interactive()
    st.subheader('Distribución de Salarios')
    st.altair_chart(salario_chart)

a, b = st.columns(2)
with a:
    # Extracción del año de contratación
    data['año_contratacion'] = pd.to_datetime(data['fecha_contratacion']).dt.day_name()

    # Agrupación de los datos por año de contratación y conteo de empleados
    empleados_por_año = data.groupby('año_contratacion').size().reset_index(name='cantidad')

    # Creación del gráfico de barras
    bar_chart = alt.Chart(empleados_por_año).mark_bar().encode(
        x=alt.X('año_contratacion:O', title='Día de Contratación'),
        y=alt.Y('cantidad:Q', title='Cantidad de Empleados'),
        tooltip=['año_contratacion', 'cantidad']
    ).properties(
        width=800,
        height=400
    ).interactive()

    # Visualización del gráfico de barras
    st.subheader('Cantidad de Empleados por Año de Contratación')
    st.altair_chart(bar_chart)
with b:

    # Estadísticas sobre los empleados
    st.subheader('Estadísticas de Empleados')
    with st.expander('Ver Estadísticas'):
        st.write(f"Total de empleados: {total_empleados}")
        st.write(f"Salario promedio: {salario_promedio:.2f}")
        st.write(f"Salario máximo: {salario_maximo}")
        st.write(f"Salario mínimo: {salario_minimo}")

# Cerrar la conexión a la base de datos
conn.close()
