from django.shortcuts import render
import pandas as pd
import numpy as np
# Importa las bibliotecas de clustering que vayas a usar

from django.http import HttpResponse
import cx_Oracle
import csv

def exportar_datos_a_csv(request):
    # Reemplaza estos valores con tu información de conexión
    username = 'usuario'
    password = 'usuario'
    database = 'localhost:1521/xe'

    try:
        # Crea una conexión a la base de datos
        conn = cx_Oracle.connect(username, password, database)

        sql_query = "SELECT * FROM usuario"

        # Ejecuta la consulta y recupera los resultados
        cursor = conn.cursor()
        cursor.execute(sql_query)

        # Recupera todas las filas de resultados
        resultados = cursor.fetchall()

        # Configura la respuesta HTTP para descargar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datos.csv"'

        # Crea un objeto escritor CSV
        csv_writer = csv.writer(response)

        # Escribe la cabecera del archivo CSV (nombres de columnas)
        column_names = [desc[0] for desc in cursor.description]
        csv_writer.writerow(column_names)

        # Escribe las filas de datos en el archivo CSV
        csv_writer.writerows(resultados)

        return response

    finally:
        # Cierra el cursor y la conexión a la base de datos en el bloque "finally"
        cursor.close()
        conn.close()


from django.shortcuts import render
from .models import (
    Ciudad,
    Competencia,
    CompetenciaOferta,
    CompetenciaUsuario,
    Comuna,
    Direccion,
    Educacion,
    Experiencia,
    FormacionAcademica,
    Formulario,
    Habilidad,
    HabilidadUsuario,
    Idioma,
    IdiomaUsuario,
    Institucion,
    LogroAcademico,
    ModalidadTrabajo,
    Oferta,
    TipoCargo,
    TipoEmpleo,
    TituloProf,
    Usuario,
    UsuarioLogro,
)


""" --------------------------------------BASE DE DATOS--------------------------------------------- """
def ciencia_datos(request):
    # Extraer datos de las tablas
    ciudades = Ciudad.objects.all()
    competencias = Competencia.objects.all()
    competencia_ofertas = CompetenciaOferta.objects.all()
    competencia_usuarios = CompetenciaUsuario.objects.all()
    comunas = Comuna.objects.all()
    direcciones = Direccion.objects.all()
    educaciones = Educacion.objects.all()
    experiencias = Experiencia.objects.all()
    formaciones_academicas = FormacionAcademica.objects.all()
    formularios = Formulario.objects.all()
    habilidades = Habilidad.objects.all()
    habilidades_usuarios = HabilidadUsuario.objects.all()
    idiomas = Idioma.objects.all()
    idiomas_usuarios = IdiomaUsuario.objects.all()
    instituciones = Institucion.objects.all()
    logros_academicos = LogroAcademico.objects.all()
    modalidades_trabajo = ModalidadTrabajo.objects.all()
    ofertas = Oferta.objects.all()
    tipos_cargo = TipoCargo.objects.all()
    tipos_empleo = TipoEmpleo.objects.all()
    titulos_profesionales = TituloProf.objects.all()
    usuarios = Usuario.objects.all()
    usuarios_logros = UsuarioLogro.objects.all()

    ciudades_usuarios = []

    for usuario in usuarios:


        ciudad_usuario = {
            'ciudad': usuario.fk_id_direccion.fk_d_comuna.fk_id_ciudad.nom_ciudad,
            'usuario': usuario.nombre,
        }
        ciudades_usuarios.append(ciudad_usuario)
            # Agregar registros de depuración
    
    print(ciudades_usuarios)

    # Renderizar la vista con los datos
    return render(request, 'ciencia.html', {'ciudades_usuarios': ciudades_usuarios})



