from django.shortcuts import render
import pandas as pd
import numpy as np
# Importa las bibliotecas de clustering que vayas a usar

import cx_Oracle
import csv

# Reemplaza estos valores con tu información de conexión
username = 'admin'
password = 'Clusterhire1.'
database = 'oracle-db.c67u6eugv3td.sa-east-1.rds.amazonaws.com:1521/clustdb'

try:
    # Crea una conexión a la base de datos
    conn = cx_Oracle.connect(username, password, database)

    sql_query = "SELECT * FROM usuario"

    # Ejecuta la consulta y recupera los resultados
    cursor = conn.cursor()
    cursor.execute(sql_query)

    # Recupera todas las filas de resultados
    resultados = cursor.fetchall()

    # Especifica la ubicación completa donde deseas guardar el archivo CSV
    archivo_csv = "D:\\ClusterHire\\core\\static\\datos.csv"


    # Abre el archivo CSV en modo escritura
    with open(archivo_csv, "w", newline="") as csv_file:
        # Crea un objeto escritor CSV
        csv_writer = csv.writer(csv_file)

        # Escribe la cabecera del archivo CSV (nombres de columnas)
        column_names = [desc[0] for desc in cursor.description]
        csv_writer.writerow(column_names)

        # Escribe las filas de datos en el archivo CSV
        csv_writer.writerows(resultados)

    print(f"Los datos han sido exportados a {archivo_csv}")

finally:
    # Cierra el cursor y la conexión a la base de datos en el bloque "finally"
    cursor.close()
    conn.close()