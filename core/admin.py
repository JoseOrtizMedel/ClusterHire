from django.contrib import admin

from .models import Ciudad, Competencia, CompetenciaUsuario, Comuna, Direccion, Educacion, Experiencia, FormacionAcademica, Formulario, Habilidad, HabilidadUsuario, Idioma, IdiomaUsuario, Institucion, LogroAcademico, Oferta, TipoCargo, TipoEmpleo, TituloProf, Usuario, UsuarioLogro

from .models import Ciudad, Competencia, CompetenciaUsuario, Comuna, Direccion, Educacion, Experiencia, ModalidadTrabajo, FormacionAcademica, Formulario, Habilidad, HabilidadUsuario, Idioma, IdiomaUsuario, Institucion, LogroAcademico, Oferta, TipoCargo, TipoEmpleo, TituloProf, Usuario, UsuarioLogro


# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Competencia)
admin.site.register(CompetenciaUsuario)
admin.site.register(Comuna)
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
admin.site.register(TituloProf)
admin.site.register(Usuario)


admin.site.register(UsuarioLogro)
admin.site.register(ModalidadTrabajo)