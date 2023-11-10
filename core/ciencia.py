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

        sql_query = "SELECT use.id_usuario, use.nombre, use.primer_apellido, use.segundo_apellido, use.telefono, use.correo, com.nom_comuna as COMUNA_USER, insti.nombre_institucion, insti.tipo_institucion, forma.tipo_formacion, titu.nombre_titulo, habi.nombre_habilidad, idio.nombre_idioma, logroac.nom_logro, exp.id_experiencia, exp.nombre_empleo, exp.fecha_inicio_exp, exp.fecha_termino_exp, exp.descripcion, comu.nom_comuna as COMUNA_INSTITU, tipemp.nom_tipo_empleo as TIPO_EMPLEO_EXP, tipcarg.nom_cargo as TIPO_CARGO_EXP, moda.nom_modalidad, compe.nombre_competencia as COMPETENCIA_USER, form.id_formulario, form.fecha_formulario, form.pretencion_renta, form.info_adicional, ofe.id_oferta, ofe.nom_oferta, ofe.fecha_oferta, ofe.anhos_experiencia as ANHOS_EXPERIENCIA_OFERTA, tipcargo.nom_cargo as NOM_CARGO_OFERTA, modal.nom_modalidad as MODALIDAD_OFERTA, comun.nom_comuna as COMUNA_OFERTA, compet.nombre_competencia as COMPETENCIA_OFERTA FROM usuario use LEFT JOIN direccion dire ON use.fk_id_direccion = dire.id_direccion LEFT JOIN comuna com ON dire.fk_d_comuna = com.id_comuna LEFT JOIN educacion edu ON use.id_usuario = edu.fk_id_usuario LEFT JOIN institucion insti ON edu.fk_id_institucion = insti.id_institucion LEFT JOIN formacion_academica forma ON forma.id_formacion = edu.fk_id_formacion LEFT JOIN titulo_prof titu ON titu.id_titulo = edu.fk_id_titulo LEFT JOIN habilidad_usuario habiu ON use.id_usuario = habiu.fk_id_usuario LEFT JOIN habilidad habi ON habiu.fk_id_habilidad = habi.id_habilidad LEFT JOIN idioma_usuario idious ON use.id_usuario = idious.fk_id_usuario LEFT JOIN idioma idio ON idious.fk_id_idioma = idio.id_idioma LEFT JOIN usuario_logro usulo ON use.id_usuario = usulo.fk_id_usuario LEFT JOIN logro_academico logroac ON usulo.fk_id_logro_academico = logroac.id_logro_academico LEFT JOIN experiencia exp ON use.id_usuario = exp.fk_id_usuario LEFT JOIN tipo_empleo tipemp ON exp.fk_id_tipo_empleo = tipemp.id_tipo_empleo LEFT JOIN comuna comu ON exp.fk_id_comuna = comu.id_comuna LEFT JOIN tipo_cargo tipcarg ON exp.fk_id_tipo_cargo = tipcarg.id_tipo_cargo LEFT JOIN modalidad_trabajo moda ON exp.fk_id_modalidad = moda.id_modalidad RIGHT JOIN formulario form ON use.id_usuario = form.fk_id_usuario RIGHT JOIN oferta ofe ON form.fk_id_oferta = ofe.id_oferta LEFT JOIN competencia_oferta compof ON ofe.id_oferta = compof.fk_id_oferta LEFT JOIN competencia compet ON compof.fk_id_competencia = compet.id_competencia LEFT JOIN competencia_usuario compus ON use.id_usuario = compus.fk_id_usuario LEFT JOIN competencia compe ON compus.fk_id_competencia = compe.id_competencia LEFT JOIN tipo_cargo tipcargo ON ofe.fk_id_tipo_cargo = tipcargo.id_tipo_cargo LEFT JOIN modalidad_trabajo modal ON ofe.fk_id_modalidad = modal.id_modalidad LEFT JOIN comuna comun ON ofe.fk_id_comuna = comun.id_comuna"
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



