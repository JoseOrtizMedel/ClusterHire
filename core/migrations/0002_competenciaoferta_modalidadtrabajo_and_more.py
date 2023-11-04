

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenciaOferta',
            fields=[
                ('id_comp_oferta', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'competencia_oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModalidadTrabajo',
            fields=[
                ('id_modalidad', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_modalidad', models.CharField(db_comment='Hibrido\nPresencial\nOnline', max_length=255)),
            ],
            options={
                'db_table': 'modalidad_trabajo',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='debilidadusuario',
            name='pf_id_debilidad',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='Debilidad',
        ),
        migrations.DeleteModel(
            name='DebilidadUsuario',
        ),
    ]
