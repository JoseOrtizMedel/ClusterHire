from django.contrib import admin
from .models import Ciudad, Competencia, CompetenciaUsuario, Comuna, Debilidad, DebilidadUsuario, Direccion, Educacion, Experiencia, FormacionAcademica, Formulario, Habilidad, HabilidadUsuario, Idioma, IdiomaUsuario, Institucion, LogroAcademico, Oferta, TipoCargo, TipoEmpleo, TipoUsuario, TituloProf, Usuario, UsuarioLogro

# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Competencia)
admin.site.register(CompetenciaUsuario)
admin.site.register(Comuna)
admin.site.register(Debilidad)
admin.site.register(DebilidadUsuario)
admin.site.register(Direccion)
admin.site.register(Educacion)
admin.site.register(Experiencia)
admin.site.register(FormacionAcademica)
admin.site.register(Formulario)
admin.site.register(Habilidad)
admin.site.register(HabilidadUsuario)
admin.site.register(Idioma)
admin.site.register(IdiomaUsuario)
admin.site.register(Institucion)
admin.site.register(LogroAcademico)
admin.site.register(Oferta)
admin.site.register(TipoCargo)
admin.site.register(TipoEmpleo)
admin.site.register(TipoUsuario)
admin.site.register(TituloProf)
admin.site.register(Usuario)
admin.site.register(UsuarioLogro)
