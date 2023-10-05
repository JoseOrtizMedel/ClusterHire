# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ciudad(models.Model):
    id_ciudad = models.BigIntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Competencia(models.Model):
    id_competencia = models.BigIntegerField(primary_key=True)
    nombre_competencia = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'competencia'


class CompetenciaUsuario(models.Model):
    pf_id_competencia = models.OneToOneField(Competencia, models.DO_NOTHING, db_column='pf_id_competencia', primary_key=True)  # The composite primary key (pf_id_competencia, pf_id_usuario) found, that is not supported. The first column is selected.
    pf_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='pf_id_usuario')

    class Meta:
        managed = False
        db_table = 'competencia_usuario'
        unique_together = (('pf_id_competencia', 'pf_id_usuario'),)


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=250)
    fk_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='fk_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class Debilidad(models.Model):
    id_debilidad = models.BigIntegerField(primary_key=True)
    nom_debilidad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'debilidad'


class DebilidadUsuario(models.Model):
    pf_id_debilidad = models.OneToOneField(Debilidad, models.DO_NOTHING, db_column='pf_id_debilidad', primary_key=True)  # The composite primary key (pf_id_debilidad, pf_id_usuario) found, that is not supported. The first column is selected.
    pf_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='pf_id_usuario')

    class Meta:
        managed = False
        db_table = 'debilidad_usuario'
        unique_together = (('pf_id_debilidad', 'pf_id_usuario'),)


class Direccion(models.Model):
    id_direccion = models.BigIntegerField(primary_key=True)
    numeracion = models.IntegerField()
    nombre_calle = models.CharField(max_length=200)
    fk_d_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='fk_d_comuna')
    fk_id_institucion = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='fk_id_institucion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Educacion(models.Model):
    id_educacion = models.BigIntegerField(primary_key=True)
    annio_inicio_educ = models.IntegerField()
    annio_fin_educ = models.IntegerField()
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_institucion = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='fk_id_institucion')
    fk_id_formacion = models.ForeignKey('FormacionAcademica', models.DO_NOTHING, db_column='fk_id_formacion')

    class Meta:
        managed = False
        db_table = 'educacion'


class Experiencia(models.Model):
    id_experiencia = models.BigIntegerField(primary_key=True)
    cargo_empleo = models.CharField(max_length=250, db_comment='ejemplo: responsable de ventas')
    nombre_empleo = models.CharField(max_length=250)
    modo_trabajo = models.CharField(max_length=100, db_comment='Hibrido\nPresencial\nOnline')
    fecha_inicio_exp = models.DateField()
    fecha_termino_exp = models.DateField()
    descripcion = models.BinaryField()
    fk_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='fk_id_comuna')
    fk_id_tipo_empleo = models.ForeignKey('TipoEmpleo', models.DO_NOTHING, db_column='fk_id_tipo_empleo')
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')

    class Meta:
        managed = False
        db_table = 'experiencia'


class FormacionAcademica(models.Model):
    id_formacion = models.BigIntegerField(primary_key=True)
    tipo_formacion = models.CharField(max_length=250, db_comment='Basica completa\nMedia completa\nSuperior completa\n')

    class Meta:
        managed = False
        db_table = 'formacion_academica'


class Formulario(models.Model):
    id_formulario = models.BigIntegerField(primary_key=True)
    fecha_formulario = models.DateField()
    pretencion_renta = models.IntegerField()
    carta_recomendacion = models.BinaryField(blank=True, null=True)
    info_adicional = models.BinaryField(blank=True, null=True)
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_oferta = models.ForeignKey('Oferta', models.DO_NOTHING, db_column='fk_id_oferta')

    class Meta:
        managed = False
        db_table = 'formulario'


class Habilidad(models.Model):
    id_habilidad = models.BigIntegerField(primary_key=True)
    nombre_habilidad = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'habilidad'


class HabilidadUsuario(models.Model):
    pf_id_habilidad = models.OneToOneField(Habilidad, models.DO_NOTHING, db_column='pf_id_habilidad', primary_key=True)  # The composite primary key (pf_id_habilidad, pf_id_usuario) found, that is not supported. The first column is selected.
    pf_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='pf_id_usuario')

    class Meta:
        managed = False
        db_table = 'habilidad_usuario'
        unique_together = (('pf_id_habilidad', 'pf_id_usuario'),)


class Idioma(models.Model):
    id_idioma = models.BigIntegerField(primary_key=True)
    nombre_idioma = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'idioma'


class IdiomaUsuario(models.Model):
    pf_id_idioma = models.OneToOneField(Idioma, models.DO_NOTHING, db_column='pf_id_idioma', primary_key=True)  # The composite primary key (pf_id_idioma, pf_id_usuario) found, that is not supported. The first column is selected.
    pf_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='pf_id_usuario')

    class Meta:
        managed = False
        db_table = 'idioma_usuario'
        unique_together = (('pf_id_idioma', 'pf_id_usuario'),)


class Institucion(models.Model):
    id_institucion = models.BigIntegerField(primary_key=True)
    nombre_institucion = models.CharField(max_length=250)
    tipo_institucion = models.CharField(max_length=250, db_comment='Instituto\nUniversidad\nColegio\nLiceo\netc')

    class Meta:
        managed = False
        db_table = 'institucion'


class LogroAcademico(models.Model):
    id_logro_academico = models.BigIntegerField(primary_key=True)
    nom_logro = models.CharField(max_length=250)
    descripcion_logro = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'logro_academico'


class Oferta(models.Model):
    id_oferta = models.BigIntegerField(primary_key=True)
    nom_oferta = models.CharField(max_length=250)
    descripcion_oferta = models.BinaryField()
    fecha_oferta = models.DateField()
    fk_id_tipo_cargo = models.ForeignKey('TipoCargo', models.DO_NOTHING, db_column='fk_id_tipo_cargo')

    class Meta:
        managed = False
        db_table = 'oferta'


class TipoCargo(models.Model):
    id_tipo_cargo = models.BigIntegerField(primary_key=True)
    nom_cargo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'tipo_cargo'


class TipoEmpleo(models.Model):
    id_tipo_empleo = models.BigIntegerField(primary_key=True)
    nom_tipo_empleo = models.CharField(max_length=250, db_comment='Jornada completa\nJornada parcial\nAut├│nomo\nProfesional independiente\nContrato temporal\nContrato de pr├ícticas\nContrato de formaci├│n\nTemporal')

    class Meta:
        managed = False
        db_table = 'tipo_empleo'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.BigIntegerField(primary_key=True)
    nom_tipo_usuario = models.CharField(max_length=250, db_comment='USUARIO CLIENTE\nUSUARIO ADMINISTRADOR')

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class TituloProf(models.Model):
    id_titulo = models.BigIntegerField(primary_key=True)
    nombre_titulo = models.CharField(max_length=250)
    descripcion = models.BinaryField(blank=True, null=True)
    pdf = models.BinaryField(blank=True, null=True)
    fk_id_educacion = models.ForeignKey(Educacion, models.DO_NOTHING, db_column='fk_id_educacion')

    class Meta:
        managed = False
        db_table = 'titulo_prof'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    rut_usuario = models.IntegerField(blank=True, null=True)
    dv_usuario = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=250)
    segundo_nombre = models.CharField(max_length=250, blank=True, null=True)
    primer_apellido = models.CharField(max_length=250)
    segundo_apellido = models.CharField(max_length=250, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=250)
    telefono = models.IntegerField()
    foto = models.BinaryField(blank=True, null=True)
    correo = models.CharField(max_length=200)
    contrasenha = models.CharField(max_length=250)
    fk_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='fk_id_direccion')
    fk_id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='fk_id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioLogro(models.Model):
    pf_id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='pf_id_usuario', primary_key=True)  # The composite primary key (pf_id_usuario, pf_id_logro_academico) found, that is not supported. The first column is selected.
    pf_id_logro_academico = models.ForeignKey(LogroAcademico, models.DO_NOTHING, db_column='pf_id_logro_academico')

    class Meta:
        managed = False
        db_table = 'usuario_logro'
        unique_together = (('pf_id_usuario', 'pf_id_logro_academico'),)
