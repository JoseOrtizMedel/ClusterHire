
from itertools import count
from django.shortcuts import render, redirect
import pandas as pd
import numpy as np
import os
import codecs
from django.urls import reverse

# Importa las bibliotecas de clustering que vayas a usar

from django.http import HttpResponse
import cx_Oracle
import csv

import pandas as pd                                                                                 # Se utiliza para la manipulación de DataFrame
import numpy as np                                                                                  # Utilizado para la manipulación de arreglos númericos
# import dfply as dp                                                                                # Utilizado para la manipulación de DataFrame (análogo a dplyr)
from os import listdir
# Gráficos
from matplotlib import pyplot as plt                                                                # Utilizado para la creación de gráficos
import seaborn as sns                                                                               # Creación de gráficos
from mpl_toolkits.mplot3d import Axes3D                                                             # Para gráficos 3D
# Preprocesado y análisis
import statsmodels.api as sm
from scipy import stats
from scipy.stats import pearsonr
# Preprocesado y modelado
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
# Configuración warnings
import warnings

from core.models import Formulario, Oferta
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
pd.set_option('display.max_columns', None)                                                          # Esto mostrará todas las columnas

def exportar_csv(request, id_oferta, nom_oferta ):
    # Reemplaza estos valores con tu información de conexión
    username = 'usuario'
    password = 'usuario'
    #database = 'localhost:1521/xe'
    database = 'localhost:1521/orcl' #alvi


    # Crea una conexión a la base de datos
    conn = cx_Oracle.connect(username, password, database)

    sql_query = "SELECT use.id_usuario, use.nombre, use.primer_apellido, use.segundo_apellido, use.telefono, use.correo, com.nom_comuna as COMUNA_USER, insti.nombre_institucion, insti.tipo_institucion, forma.tipo_formacion, titu.nombre_titulo, habi.nombre_habilidad, idio.nombre_idioma, logroac.nom_logro, exp.id_experiencia, exp.nombre_empleo, exp.fecha_inicio_exp, exp.fecha_termino_exp, exp.descripcion, comu.nom_comuna as COMUNA_INSTITU, tipemp.nom_tipo_empleo as TIPO_EMPLEO_EXP, tipcarg.nom_cargo as TIPO_CARGO_EXP, moda.nom_modalidad, compe.nombre_competencia as COMPETENCIA_USER, form.id_formulario, form.fecha_formulario, form.pretencion_renta, form.info_adicional, ofe.id_oferta, ofe.nom_oferta, ofe.fecha_oferta, ofe.anhos_experiencia as ANHOS_EXPERIENCIA_OFERTA, tipcargo.nom_cargo as NOM_CARGO_OFERTA, modal.nom_modalidad as MODALIDAD_OFERTA, comun.nom_comuna as COMUNA_OFERTA, compet.nombre_competencia as COMPETENCIA_OFERTA FROM usuario use LEFT JOIN direccion dire ON use.fk_id_direccion = dire.id_direccion LEFT JOIN comuna com ON dire.fk_d_comuna = com.id_comuna LEFT JOIN educacion edu ON use.id_usuario = edu.fk_id_usuario LEFT JOIN institucion insti ON edu.fk_id_institucion = insti.id_institucion LEFT JOIN formacion_academica forma ON forma.id_formacion = edu.fk_id_formacion LEFT JOIN titulo_prof titu ON titu.id_titulo = edu.fk_id_titulo LEFT JOIN habilidad_usuario habiu ON use.id_usuario = habiu.fk_id_usuario LEFT JOIN habilidad habi ON habiu.fk_id_habilidad = habi.id_habilidad LEFT JOIN idioma_usuario idious ON use.id_usuario = idious.fk_id_usuario LEFT JOIN idioma idio ON idious.fk_id_idioma = idio.id_idioma LEFT JOIN usuario_logro usulo ON use.id_usuario = usulo.fk_id_usuario LEFT JOIN logro_academico logroac ON usulo.fk_id_logro_academico = logroac.id_logro_academico LEFT JOIN experiencia exp ON use.id_usuario = exp.fk_id_usuario LEFT JOIN tipo_empleo tipemp ON exp.fk_id_tipo_empleo = tipemp.id_tipo_empleo LEFT JOIN comuna comu ON exp.fk_id_comuna = comu.id_comuna LEFT JOIN tipo_cargo tipcarg ON exp.fk_id_tipo_cargo = tipcarg.id_tipo_cargo LEFT JOIN modalidad_trabajo moda ON exp.fk_id_modalidad = moda.id_modalidad RIGHT JOIN formulario form ON use.id_usuario = form.fk_id_usuario RIGHT JOIN oferta ofe ON form.fk_id_oferta = ofe.id_oferta LEFT JOIN competencia_oferta compof ON ofe.id_oferta = compof.fk_id_oferta LEFT JOIN competencia compet ON compof.fk_id_competencia = compet.id_competencia LEFT JOIN competencia_usuario compus ON use.id_usuario = compus.fk_id_usuario LEFT JOIN competencia compe ON compus.fk_id_competencia = compe.id_competencia LEFT JOIN tipo_cargo tipcargo ON ofe.fk_id_tipo_cargo = tipcargo.id_tipo_cargo LEFT JOIN modalidad_trabajo modal ON ofe.fk_id_modalidad = modal.id_modalidad LEFT JOIN comuna comun ON ofe.fk_id_comuna = comun.id_comuna"

    # Ejecuta la consulta y recupera los resultados
    cursor = conn.cursor()
    cursor.execute(sql_query)

    # Recupera todas las filas de resultados
    resultados = cursor.fetchall()

    # Ruta donde se guardará el archivo CSV
    csv_file_path = 'core/static/datos/datos.csv'

    # Crea un objeto escritor CSV
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Escribe la cabecera del archivo CSV (nombres de columnas)
        column_names = [desc[0] for desc in cursor.description]
        csv_writer.writerow(column_names)

        # Escribe las filas de datos en el archivo CSV
        csv_writer.writerows(resultados)

    # Cierra el cursor y la conexión a la base de datos
    cursor.close()
    conn.close()

    ciencia_url = reverse('ciencia', args=[id_oferta, nom_oferta])

    # Redirige a la URL de la vista ciencia
    return redirect(ciencia_url)
    
 


def read_csv(request, id_oferta):

    # Ruta al archivo CSV
    csv_file_path = 'core/static/datos/datos.csv'

    #------------------------------------------------------------Lee el archivo CSV con pandas
    df2 = pd.read_csv(csv_file_path, encoding='latin1')  # o prueba con 'ISO-8859-1'

    #------------------------------------------------------------Eliminar columnas que no se usen
    df2 = df2.drop(['SEGUNDO_APELLIDO'], axis=1)
    df2 = df2.drop(['TELEFONO'], axis=1)
    df2 = df2.drop(['CORREO'], axis=1)
    df2 = df2.drop(['NOMBRE_INSTITUCION'], axis=1)
    df2 = df2.drop(['TIPO_INSTITUCION'], axis=1)
    df2 = df2.drop(['NOM_LOGRO'], axis=1)
    df2 = df2.drop(['DESCRIPCION'], axis=1)
    df2 = df2.drop(['COMUNA_INSTITU'], axis=1)
    df2 = df2.drop(['TIPO_EMPLEO_EXP'], axis=1)
    df2 = df2.drop(['PRETENCION_RENTA'], axis=1)
    df2 = df2.drop(['INFO_ADICIONAL'], axis=1)
    #------------------------------------------------------------Se filtra por id_oferta
    oferta_id = id_oferta  # alvi
    resultado = df2[df2['ID_OFERTA'] == oferta_id]
    #------------------------------------------------------------Desarrollo

    # Identifica los usuarios con más de un cargo de experiencia distinto
    usuarios_con_multiples_cargos = resultado.groupby('ID_USUARIO')['TIPO_CARGO_EXP'].nunique()
    usuarios_multiples_cargos = usuarios_con_multiples_cargos[usuarios_con_multiples_cargos > 1].index

    # Filtra el DataFrame resultado para dejar solo las filas donde TIPO_CARGO_EXP coincide con NOM_CARGO_OFERTA
    resultado = resultado[~((resultado['ID_USUARIO'].isin(usuarios_multiples_cargos)) & (resultado['TIPO_CARGO_EXP'] != resultado['NOM_CARGO_OFERTA']))]

    # Elimina las filas duplicadas basadas en todas las columnas del DataFrame
    resultado = resultado.drop_duplicates()

    # Convierte las columnas de fechas en formato datetime
    resultado['FECHA_INICIO_EXP'] = pd.to_datetime(df2['FECHA_INICIO_EXP'])
    resultado['FECHA_TERMINO_EXP'] = pd.to_datetime(df2['FECHA_TERMINO_EXP'])

    # Calcula la diferencia en años y crea una nueva columna llamada 'ANHOS_EXPERIENCIA'
    resultado['ANHOS_EXPERIENCIA_USER'] = (resultado['FECHA_TERMINO_EXP'] - resultado['FECHA_INICIO_EXP']).dt.days // 365

    # Rellena los valores nulos en la columna 'ANHOS_EXPERIENCIA_USER' con 0
    resultado['ANHOS_EXPERIENCIA_USER'] = resultado['ANHOS_EXPERIENCIA_USER'].fillna(0)

    def asignar_puntaje_formacion(tipo_formacion):
        if tipo_formacion == "Basica completa":
            return 0
        elif tipo_formacion == "Media completa":
            return 1
        elif tipo_formacion == "Superior completa":
            return 2
        else:
            return 0  # Maneja otros valores si es necesario

    # Aplica la función a la columna 'TIPO_FORMACION' para crear la nueva columna 'ptj_formacion'
    resultado['ptj_formacion'] = df2['TIPO_FORMACION'].apply(asignar_puntaje_formacion)

    def asignar_puntaje_titulo(nombre_titulo):
        if pd.notna(nombre_titulo):
            return 1
        else:
            return 0

    # Aplica la función a la columna 'NOMBRE_TITULO' para crear la nueva columna 'ptj_titulo'
    resultado['ptj_titulo'] = df2['NOMBRE_TITULO'].apply(asignar_puntaje_titulo)

    # Realiza el conteo de habilidades distintas por usuario en el DataFrame resultado
    conteo_habilidades = resultado.groupby('ID_USUARIO')['NOMBRE_HABILIDAD'].nunique().reset_index()
    conteo_habilidades.columns = ['ID_USUARIO', 'CANTIDAD_HABILIDADES']

    # Define la función para asignar puntajes de habilidades
    def asignar_puntaje_habilidades(cantidad_habilidades):
        if cantidad_habilidades == 0:
            return 0
        elif cantidad_habilidades == 1:
            return 1
        elif cantidad_habilidades == 2:
            return 2
        elif cantidad_habilidades == 3:
            return 3
        else:
            return 0

    # Aplica la función a la columna 'CANTIDAD_HABILIDADES' para crear la nueva columna 'ptj_habilidades'
    conteo_habilidades['ptj_habilidades'] = conteo_habilidades['CANTIDAD_HABILIDADES'].apply(asignar_puntaje_habilidades)

    # Fusiona el DataFrame conteo_habilidades con resultado
    resultado = resultado.merge(conteo_habilidades[['ID_USUARIO', 'ptj_habilidades']], on='ID_USUARIO', how='left')

    # Elimina la columna 'NOMBRE_HABILIDAD' de resultado
    resultado = resultado.drop('NOMBRE_HABILIDAD', axis=1)

    # Elimina las filas duplicadas basadas en todas las columnas del DataFrame
    resultado = resultado.drop_duplicates()

    # Realiza el conteo de idiomas distintos por usuario en el DataFrame resultado
    conteo_idiomas = resultado.groupby('ID_USUARIO')['NOMBRE_IDIOMA'].nunique().reset_index()
    conteo_idiomas.columns = ['ID_USUARIO', 'CANTIDAD_IDIOMAS']

    # Define la función para asignar puntajes de idiomas
    def asignar_puntaje_idiomas(cantidad_idiomas):
        if cantidad_idiomas == 0:
            return 0
        elif cantidad_idiomas == 1:
            return 1
        elif cantidad_idiomas > 1:
            return 2
        else:
            return 0

    # Aplica la función a la columna 'CANTIDAD_IDIOMAS' para crear la nueva columna 'ptj_idiomas'
    conteo_idiomas['ptj_idiomas'] = conteo_idiomas['CANTIDAD_IDIOMAS'].apply(asignar_puntaje_idiomas)

    # Fusiona el DataFrame conteo_idiomas con resultado
    resultado = resultado.merge(conteo_idiomas[['ID_USUARIO', 'ptj_idiomas']], on='ID_USUARIO', how='left')
    # Elimina la columna 'NOMBRE_IDIOMA' de resultado
    resultado = resultado.drop('NOMBRE_IDIOMA', axis=1)
    # Elimina las filas duplicadas basadas en todas las columnas del DataFrame
    resultado = resultado.drop_duplicates()

    # Crea una nueva columna 'ptj_cargo' con valor inicial de 0 en el DataFrame filtrado
    resultado['ptj_cargo'] = 0

    # Itera a través de las filas del DataFrame filtrado
    for index, row in resultado.iterrows():
        usuario_id = row['ID_USUARIO']
        cargo_usuario = row['TIPO_CARGO_EXP']

        # Filtra las ofertas que coinciden con el usuario y el nombre del cargo
        ofertas_coincidentes = resultado[(resultado['ID_USUARIO'] == usuario_id) & (resultado['NOM_CARGO_OFERTA'] == cargo_usuario)]

        # Si hay ofertas que coinciden, asigna un punto al usuario en el DataFrame filtrado
        if len(ofertas_coincidentes) > 0:
            resultado.at[index, 'ptj_cargo'] = 2

    # Crea una nueva columna 'ptj_cargo' con valor inicial de 0 en el DataFrame filtrado
    resultado['ptj_cargo'] = 0

    # Itera a través de las filas del DataFrame filtrado
    for index, row in resultado.iterrows():
        usuario_id = row['ID_USUARIO']
        cargo_usuario = row['TIPO_CARGO_EXP']

        # Filtra las ofertas que coinciden con el usuario y el nombre del cargo
        ofertas_coincidentes = resultado[(resultado['ID_USUARIO'] == usuario_id) & (resultado['NOM_CARGO_OFERTA'] == cargo_usuario)]

        # Si hay ofertas que coinciden, asigna un punto al usuario en el DataFrame filtrado
        if len(ofertas_coincidentes) > 0:
            resultado.at[index, 'ptj_cargo'] = 2


    # Crea una nueva columna 'ptj_competencia' con valor inicial de 0 en el DataFrame filtrado
    resultado['ptj_competencia'] = 0

    # Itera a través de las filas del DataFrame filtrado
# Itera a través de las filas del DataFrame filtrado
    for index, row in resultado.iterrows():
        usuario_id = row['ID_USUARIO']
        competencias_usuario = row['COMPETENCIA_USER']

        # Verifica si 'COMPETENCIA_OFERTA' es una cadena antes de intentar dividirla
        if pd.notna(row['COMPETENCIA_OFERTA']) and isinstance(row['COMPETENCIA_OFERTA'], str):
            competencias_oferta = row['COMPETENCIA_OFERTA'].split(';')
        else:
            competencias_oferta = []

        # Verifica si 'COMPETENCIA_USER' es una cadena antes de intentar dividirla
        if isinstance(competencias_usuario, str):
            # Calcula el puntaje basado en las coincidencias de competencias
            puntaje = sum(1 for competencia in competencias_usuario.split(';') if competencia in competencias_oferta)

            # Asigna el puntaje al usuario en el DataFrame filtrado
            resultado.at[index, 'ptj_competencia'] = puntaje * 2
        else:
            # Si 'COMPETENCIA_USER' no es una cadena, asigna 0 como puntaje
            resultado.at[index, 'ptj_competencia'] = 0



    resultado['NOM_MODALIDAD'].fillna('N/A', inplace=True)

    columnas_seleccionadas = ['ID_OFERTA','NOM_OFERTA', 'ID_FORMULARIO','FECHA_FORMULARIO', 'ID_USUARIO','NOMBRE', 'PRIMER_APELLIDO',
                            'ANHOS_EXPERIENCIA_USER','TIPO_CARGO_EXP','ptj_formacion', 'ptj_titulo','ptj_habilidades', 'ptj_idiomas', 'ptj_cargo',
                            'ptj_competencia', 'COMPETENCIA_USER','COMPETENCIA_OFERTA', 'NOM_MODALIDAD']

    # Seleccionar columnas
    df = resultado[columnas_seleccionadas]

    # Ordenar por 'FECHA_FORMULARIO' en orden descendente
    df = df.sort_values(by='FECHA_FORMULARIO', ascending=False)

    # Eliminar duplicados, conservando la primera ocurrencia (la más reciente)
    df = df.drop_duplicates(subset='ID_USUARIO', keep='first')

    # Realizar el agrupamiento y suma
    df = df.groupby(['ID_OFERTA','NOM_OFERTA','ID_FORMULARIO', 'ID_USUARIO','NOMBRE', 'PRIMER_APELLIDO', 'NOM_MODALIDAD',
                    'ANHOS_EXPERIENCIA_USER', 'ptj_formacion', 'ptj_titulo', 'ptj_habilidades', 'ptj_idiomas', 'ptj_cargo'
                 ])['ptj_competencia'].sum().reset_index()

#----------------------------------------------------K-MEANS------------------------------------------------------
    conteo_formularios = df['ID_FORMULARIO'].count()

    if conteo_formularios  >= 3:
        print(conteo_formularios)

    else:
        print("Hay menos de 3")
        

    df['NOM_MODALIDAD'] = df['NOM_MODALIDAD'].replace(['Presencial','Online','Hibrido','N/A'],[1,2,3,4])

    X = np.array(df[["ANHOS_EXPERIENCIA_USER","ptj_formacion","ptj_titulo","ptj_habilidades", "ptj_idiomas", "ptj_cargo", "ptj_competencia"]])
    y = np.array(df['NOM_MODALIDAD'])
    X.shape

    Nc = range(1, 3)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    kmeans
    score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]

    fig = plt.figure()
    ax = Axes3D(fig)
    colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
    #NOTA: asignamos la posición cero del array repetida pues las categorias comienzan en id 1. 
    asignar=[]
    for row in y:
        asignar.append(colores[row])
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)

    

    
    from sklearn.metrics import silhouette_samples, silhouette_score
    random_seed = 42    
    km = KMeans(n_clusters=2, random_state=random_seed).fit(X)

    km.fit_predict(X)

    scores = silhouette_score(X, km.labels_, metric='euclidean')


    # Obtenemos las etiquetas de cada punto de nuestros datos
    labels = km.predict(X)
    # Obtenemos los centroids
    C = km.cluster_centers_
    colores=['blue','green']
    asignar=[]
    for row in labels:
        asignar.append(colores[row])

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
    ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)

    # contamos cuantos usuarios hay en cada grupo
    copy =  pd.DataFrame()
    copy['NOMBRE']=df['NOMBRE'].values
    copy['NOM_MODALIDAD']=df['NOM_MODALIDAD'].values
    copy['label'] = labels;
    cantidadGrupo =  pd.DataFrame()
    cantidadGrupo['color']=colores
    cantidadGrupo['cantidad']=copy.groupby('label').size()

    df['cluster']=labels

    # Primer grupo
    grupo_mejor_recomendado = df.sort_values(by=['cluster'])[0:(cantidadGrupo['cantidad'][0])]
    grupo_mejor_recomendado

    # Segundo grupo
    grupo_menor_recomendado = df.sort_values(by=['cluster'])[(cantidadGrupo['cantidad'][0]):(cantidadGrupo['cantidad'][0] + cantidadGrupo['cantidad'][1])]
    grupo_menor_recomendado
    
#-----------------------------------------------------------------------------------------------------------------
    
    # Supongamos que df es tu DataFrame
    columnas_a_mostrar = ['ID_OFERTA', 'NOM_OFERTA', 'ID_USUARIO', 'NOMBRE', 'PRIMER_APELLIDO', 'ANHOS_EXPERIENCIA_USER']

    # Filtra el DataFrame para incluir solo las columnas deseadas
    df_filtrado = grupo_mejor_recomendado[columnas_a_mostrar]  
    df_filtrado2 = grupo_menor_recomendado[columnas_a_mostrar] 


    #nuevos_nombres = {'ID_OFERTA': 'ID Oferta', 'NOM_OFERTA': 'Nombre oferta', 'ID_USUARIO': 'ID Usuario', 'NOMBRE': 'Nombre', 'PRIMER_APELLIDO': 'Apellido', 'ANHOS_EXPERIENCIA_USER': 'Años de experiencia'}
    #df_filtrado = df_filtrado.rename(columns=nuevos_nombres)
    #df_filtrado2 = df_filtrado2.rename(columns=nuevos_nombres)

    # Convierte el DataFrame a formato HTML
    df_html = df_filtrado.to_html(classes='table table-striped', index=False)
    df_html2 = df_filtrado2.to_html(classes='table table-striped', index=False)

    # Pasa el HTML directamente al contexto
    context = {'df_filtrado': df_filtrado,'df_filtrado2': df_filtrado2,'df_html': df_html,'df_html2': df_html2, 'id_oferta': id_oferta}

    
    # Renderiza la plantilla con los datos
    return render(request, 'ciencia.html', context)


    





