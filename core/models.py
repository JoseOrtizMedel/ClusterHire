# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    nom_ciudad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Competencia(models.Model):
    id_competencia = models.BigAutoField(primary_key=True)
    nombre_competencia = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'competencia'


class CompetenciaOferta(models.Model):
    id_comp_oferta = models.BigAutoField(primary_key=True)
    fk_id_oferta = models.ForeignKey('Oferta', models.DO_NOTHING, db_column='fk_id_oferta')
    fk_id_competencia = models.ForeignKey(Competencia, models.DO_NOTHING, db_column='fk_id_competencia')

    class Meta:
        managed = False
        db_table = 'competencia_oferta'


class CompetenciaUsuario(models.Model):
    id_compe_usuario = models.BigAutoField(primary_key=True)
    fk_id_competencia = models.ForeignKey(Competencia, models.DO_NOTHING, db_column='fk_id_competencia')
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')

    class Meta:
        managed = False
        db_table = 'competencia_usuario'


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    nom_comuna = models.CharField(max_length=250)
    fk_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='fk_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    id_direccion = models.BigAutoField(primary_key=True)
    numeracion = models.IntegerField()
    nombre_calle = models.CharField(max_length=200)
    fk_d_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='fk_d_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class Educacion(models.Model):
    id_educacion = models.BigAutoField(primary_key=True)
    annio_inicio_educ = models.IntegerField()
    annio_fin_educ = models.IntegerField()
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_institucion = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='fk_id_institucion')
    fk_id_formacion = models.ForeignKey('FormacionAcademica', models.DO_NOTHING, db_column='fk_id_formacion')
    fk_id_titulo = models.ForeignKey('TituloProf', models.DO_NOTHING, db_column='fk_id_titulo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educacion'


class Experiencia(models.Model):
    id_experiencia = models.BigAutoField(primary_key=True)
    nombre_empleo = models.CharField(max_length=250)
    fecha_inicio_exp = models.DateField()
    fecha_termino_exp = models.DateField()
    descripcion = models.TextField()
    fk_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='fk_id_comuna')
    fk_id_tipo_empleo = models.ForeignKey('TipoEmpleo', models.DO_NOTHING, db_column='fk_id_tipo_empleo')
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_modalidad = models.ForeignKey('ModalidadTrabajo', models.DO_NOTHING, db_column='fk_id_modalidad')
    fk_id_tipo_cargo = models.ForeignKey('TipoCargo', models.DO_NOTHING, db_column='fk_id_tipo_cargo')

    class Meta:
        managed = False
        db_table = 'experiencia'


class FormacionAcademica(models.Model):
    id_formacion = models.BigAutoField(primary_key=True)
    tipo_formacion = models.CharField(max_length=250, db_comment='Basica completa\nMedia completa\nSuperior completa\n')

    class Meta:
        managed = False
        db_table = 'formacion_academica'


class Formulario(models.Model):
    id_formulario = models.BigAutoField(primary_key=True)
    fecha_formulario = models.DateField()
    pretencion_renta = models.IntegerField()
    info_adicional = models.TextField(blank=True, null=True)
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_oferta = models.ForeignKey('Oferta', models.DO_NOTHING, db_column='fk_id_oferta')

    class Meta:
        managed = False
        db_table = 'formulario'


class Habilidad(models.Model):
    id_habilidad = models.BigAutoField(primary_key=True)
    nombre_habilidad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'habilidad'


class HabilidadUsuario(models.Model):
    id_habilidad_usuario = models.BigAutoField(primary_key=True)
    fk_id_habilidad = models.ForeignKey(Habilidad, models.DO_NOTHING, db_column='fk_id_habilidad')
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')

    class Meta:
        managed = False
        db_table = 'habilidad_usuario'


class Idioma(models.Model):
    id_idioma = models.BigAutoField(primary_key=True)
    nombre_idioma = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'idioma'


class IdiomaUsuario(models.Model):
    id_idioma_usuario = models.BigAutoField(primary_key=True)
    fk_id_idioma = models.ForeignKey(Idioma, models.DO_NOTHING, db_column='fk_id_idioma')
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')

    class Meta:
        managed = False
        db_table = 'idioma_usuario'


class Institucion(models.Model):
    id_institucion = models.BigAutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=250)
    tipo_institucion = models.CharField(max_length=250, db_comment='Instituto\nUniversidad\nColegio\nLiceo\netc')
    fk_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='fk_id_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institucion'


class LogroAcademico(models.Model):
    id_logro_academico = models.BigAutoField(primary_key=True)
    nom_logro = models.CharField(max_length=250)
    descripcion_logro = models.TextField()

    class Meta:
        managed = False
        db_table = 'logro_academico'


class ModalidadTrabajo(models.Model):
    id_modalidad = models.BigAutoField(primary_key=True)
    nom_modalidad = models.CharField(max_length=255, db_comment='Hibrido\nPresencial\nOnline')

    class Meta:
        managed = False
        db_table = 'modalidad_trabajo'


class Oferta(models.Model):
    id_oferta = models.BigAutoField(primary_key=True)
    nom_oferta = models.CharField(max_length=250)
    fecha_oferta = models.DateField()
    anhos_experiencia = models.IntegerField()
    fk_id_tipo_cargo = models.ForeignKey('TipoCargo', models.DO_NOTHING, db_column='fk_id_tipo_cargo')
    fk_id_modalidad = models.ForeignKey(ModalidadTrabajo, models.DO_NOTHING, db_column='fk_id_modalidad')
    fk_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='fk_id_comuna')

    class Meta:
        managed = False
        db_table = 'oferta'


class TipoCargo(models.Model):
    id_tipo_cargo = models.BigAutoField(primary_key=True)
    nom_cargo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tipo_cargo'


class TipoEmpleo(models.Model):
    id_tipo_empleo = models.BigAutoField(primary_key=True)
    nom_tipo_empleo = models.CharField(max_length=250, db_comment='Jornada completa\nJornada parcial\nAut¾nomo\nProfesional independiente\nContrato temporal\nContrato de prßcticas\nContrato de formaci¾n\nTemporal')

    class Meta:
        managed = False
        db_table = 'tipo_empleo'


class TituloProf(models.Model):
    id_titulo = models.BigAutoField(primary_key=True)
    nombre_titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulo_prof'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    rut_usuario = models.IntegerField(blank=True, null=True)
    dv_usuario = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=250)
    segundo_nombre = models.CharField(max_length=250, blank=True, null=True)
    primer_apellido = models.CharField(max_length=250)
    segundo_apellido = models.CharField(max_length=250, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=200)
    fk_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='fk_id_direccion')

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioLogro(models.Model):
    id_usuario_logro = models.BigAutoField(primary_key=True)
    fk_id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_logro_academico = models.ForeignKey(LogroAcademico, models.DO_NOTHING, db_column='fk_id_logro_academico')

    class Meta:
        managed = False
        db_table = 'usuario_logro'
