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

        sql_query = "select use.id_usuario, use.nombre, use.primer_apellido, use.segundo_apellido, use.telefono, use.correo, com.nom_comuna as COMUNA_USER, insti.nombre_institucion, insti.tipo_institucion, forma.tipo_formacion, titu.nombre_titulo, habi.nombre_habilidad, idio.nombre_idioma, logroac.nom_logro, exp.id_experiencia ,exp.nombre_empleo, exp.fecha_inicio_exp, exp.fecha_termino_exp, exp.descripcion, comu.nom_comuna as COMUNA_INSTITU, tipemp.nom_tipo_empleo as TIPO_EMPLEO_EXP, tipcarg.nom_cargo as TIPO_CARGO_EXP, moda.nom_modalidad, compe.nombre_competencia as COMPETENCIA_USER, form.id_formulario, form.fecha_formulario, form.pretencion_renta, form.info_adicional, ofe.nom_oferta, ofe.fecha_oferta, ofe.anhos_experiencia as ANHOS_EXPERIENCIA_OFERTA, tipcargo.nom_cargo as NOM_CARGO_OFERTA, modal.nom_modalidad as MODALIDAD_OFERTA, comun.nom_comuna as COMUNA_OFERTA, compet.nombre_competencia as COMPETENCIA_OFERTA from usuario use left join direccion dire on use.fk_id_direccion = dire.id_direccion left join comuna com on dire.fk_d_comuna = com.id_comuna left join educacion edu on use.id_usuario  = edu.fk_id_usuario left join institucion insti on edu.fk_id_institucion = insti.id_institucion left join formacion_academica forma on forma.id_formacion = edu.fk_id_formacion left join titulo_prof titu on titu.id_titulo = edu.fk_id_titulo left join habilidad_usuario habiu on use.id_usuario = habiu.fk_id_usuario left join habilidad habi on habiu.fk_id_habilidad = habi.id_habilidad left join idioma_usuario idious on use.id_usuario = idious.fk_id_usuario left join idioma idio on idious.fk_id_idioma = idio.id_idioma left join usuario_logro usulo on use.id_usuario = usulo.fk_id_usuario left join logro_academico logroac on usulo.fk_id_logro_academico = logroac.id_logro_academico left join experiencia exp on use.id_usuario = exp.fk_id_usuario left join tipo_empleo tipemp on exp.fk_id_tipo_empleo = tipemp.id_tipo_empleo left join comuna comu on exp.fk_id_comuna = comu.id_comuna left join tipo_cargo tipcarg on exp.fk_id_tipo_cargo = tipcarg.id_tipo_cargo left join modalidad_trabajo moda on exp.fk_id_modalidad = moda.id_modalidad left join competencia_usuario compus on use.id_usuario = compus.fk_id_usuario left join competencia compe on compus.fk_id_competencia = compe.id_competencia right join formulario form on use.id_usuario = form.fk_id_usuario right join oferta ofe on form.fk_id_oferta=ofe.id_oferta left join tipo_cargo tipcargo on ofe.fk_id_tipo_cargo = tipcargo.id_tipo_cargo left join modalidad_trabajo modal on ofe.fk_id_modalidad = modal.id_modalidad left join comuna comun on ofe.fk_id_comuna = comun.id_comuna left join competencia_oferta compof on ofe.id_oferta = compof.fk_id_oferta left join competencia compet on compof.fk_id_competencia = compe.id_competencia"
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



