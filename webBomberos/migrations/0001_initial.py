# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanante',
            fields=[
                ('idacompanante', models.AutoField(serialize=False, primary_key=True, db_column='idAcompanante')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('rut', models.CharField(max_length=45, null=True, blank=True)),
                ('estado', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'acompanante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AfectadoIncendio',
            fields=[
                ('idafectado', models.AutoField(serialize=False, primary_key=True, db_column='idAfectado')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('rut', models.CharField(max_length=45, null=True, blank=True)),
                ('tipoafectado', models.CharField(max_length=45, null=True, db_column='tipoAfectado', blank=True)),
                ('numeroadulto', models.IntegerField(null=True, db_column='numeroAdulto', blank=True)),
                ('numeroninos', models.IntegerField(null=True, db_column='numeroNinos', blank=True)),
                ('danovivienda', models.IntegerField(null=True, db_column='danoVivienda', blank=True)),
                ('danoenseres', models.IntegerField(null=True, db_column='danoEnseres', blank=True)),
                ('superficie', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'afectado_incendio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AfectadoRescate',
            fields=[
                ('idrescate', models.AutoField(serialize=False, primary_key=True, db_column='idRescate')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('rut', models.CharField(max_length=45, null=True, blank=True)),
                ('tipoafectado', models.CharField(max_length=45, null=True, db_column='tipoAfectado', blank=True)),
                ('estado', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'afectado_rescate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apoyo',
            fields=[
                ('idapoyo', models.AutoField(serialize=False, primary_key=True, db_column='idApoyo')),
                ('tipo', models.CharField(max_length=45, null=True, blank=True)),
                ('procedencia', models.CharField(max_length=45, null=True, blank=True)),
                ('personacargo', models.CharField(max_length=45, null=True, db_column='personaCargo', blank=True)),
                ('rango', models.CharField(max_length=45, null=True, blank=True)),
                ('patente', models.CharField(max_length=45, null=True, blank=True)),
                ('compania', models.CharField(max_length=45, null=True, blank=True)),
                ('municipalidad', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'apoyo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AseguradoraVehiculo',
            fields=[
                ('idaseguradora_vehiculo', models.AutoField(serialize=False, primary_key=True, db_column='idAseguradora_vehiculo')),
                ('poliza', models.CharField(max_length=45, null=True, blank=True)),
                ('compania', models.CharField(max_length=45, null=True, blank=True)),
                ('especie', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'aseguradora_vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AseguradoraViviendaAfectado',
            fields=[
                ('idaseguradora_afectado', models.AutoField(serialize=False, primary_key=True)),
                ('poliza', models.CharField(max_length=45, null=True, blank=True)),
                ('compania', models.CharField(max_length=45, null=True, blank=True)),
                ('especie', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'aseguradora_vivienda_afectado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('idasistencia', models.AutoField(serialize=False, primary_key=True, db_column='idAsistencia')),
                ('codigoasistencia', models.CharField(max_length=45, null=True, db_column='codigoAsistencia', blank=True)),
                ('asistenciaobligatoria', models.IntegerField(null=True, db_column='asistenciaObligatoria', blank=True)),
            ],
            options={
                'db_table': 'asistencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254, null=True, blank=True)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('idcarro', models.AutoField(serialize=False, primary_key=True, db_column='idCarro')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('tipo', models.CharField(max_length=45, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'carro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idcategoria', models.AutoField(serialize=False, primary_key=True, db_column='idCategoria')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('idcompania', models.AutoField(serialize=False, primary_key=True, db_column='idCompania')),
                ('registrocompania', models.CharField(max_length=45, db_column='registroCompania')),
                ('clave', models.CharField(max_length=45)),
                ('calle', models.CharField(max_length=45)),
                ('numerocalle', models.CharField(max_length=45, null=True, db_column='numeroCalle', blank=True)),
                ('ciudad', models.CharField(max_length=45)),
                ('nombrecompania', models.CharField(max_length=45, null=True, db_column='nombreCompania', blank=True)),
            ],
            options={
                'db_table': 'compania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Companiavoluntario',
            fields=[
                ('idcompaniavoluntario', models.AutoField(serialize=False, primary_key=True, db_column='idCompaniaVoluntario')),
                ('fechaingreso', models.DateField(null=True, blank=True)),
                ('fechasalida', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'companiavoluntario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Era',
            fields=[
                ('idera', models.AutoField(serialize=False, primary_key=True, db_column='idEra')),
                ('numeroarne', models.IntegerField(null=True, db_column='numeroArne', blank=True)),
                ('numeromascara', models.IntegerField(null=True, db_column='numeroMascara', blank=True)),
                ('estado', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'era',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idevento', models.AutoField(serialize=False, primary_key=True, db_column='idEvento')),
                ('correlativollamado', models.CharField(max_length=45, null=True, db_column='correlativoLlamado', blank=True)),
                ('correlativocbv', models.CharField(max_length=45, null=True, db_column='correlativoCBV', blank=True)),
                ('claveservicio', models.CharField(max_length=45, null=True, db_column='claveServicio', blank=True)),
                ('fecha', models.DateTimeField(db_column='fecha')),
                ('motivo', models.CharField(max_length=45, null=True, db_column='motivo', blank=True)),
                ('calle', models.CharField(max_length=45, null=True, db_column='calle', blank=True)),
                ('numerocalle', models.IntegerField(null=True, db_column='numeroCalle', blank=True)),
                ('calleproxima', models.CharField(max_length=45, null=True, db_column='calleProxima', blank=True)),
                ('sector', models.CharField(max_length=45, null=True, blank=True)),
                ('poblacion', models.CharField(max_length=45, null=True, blank=True)),
                ('ruta', models.CharField(max_length=45, null=True, blank=True)),
                ('kilometroruta', models.IntegerField(null=True, db_column='kilometroRuta', blank=True)),
                ('codigocargo', models.CharField(max_length=45, null=True, db_column='codigoCargo', blank=True)),
                ('codigoinforme', models.CharField(max_length=45, null=True, db_column='codigoInforme', blank=True)),
                ('numerodepartamento', models.CharField(max_length=45, null=True, db_column='numeroDepartamento', blank=True)),
                ('numeroblock', models.CharField(max_length=45, null=True, db_column='numeroBlock', blank=True)),
                ('resumen', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('idgas', models.AutoField(serialize=False, primary_key=True, db_column='idGas')),
                ('tipocontenedor', models.CharField(max_length=45, null=True, db_column='tipoContenedor', blank=True)),
                ('tipogas', models.CharField(max_length=45, null=True, db_column='tipoGas', blank=True)),
                ('capacidad', models.IntegerField(null=True, blank=True)),
                ('empresa', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'gas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Incendio',
            fields=[
                ('idincendio', models.AutoField(serialize=False, primary_key=True, db_column='idIncendio')),
                ('tipoincendio', models.CharField(max_length=45, null=True, db_column='tipoIncendio', blank=True)),
                ('faseincendio', models.CharField(max_length=45, null=True, db_column='faseIncendio', blank=True)),
                ('det', models.IntegerField(null=True, blank=True)),
                ('bomberodet', models.CharField(max_length=45, null=True, db_column='bomberoDet', blank=True)),
                ('origen', models.CharField(max_length=45, null=True, blank=True)),
                ('causa', models.CharField(max_length=45, null=True, blank=True)),
                ('fuentecalor', models.CharField(max_length=45, null=True, db_column='fuenteCalor', blank=True)),
                ('tipolugar', models.CharField(max_length=45, null=True, db_column='tipoLugar', blank=True)),
                ('tipoconstruccion', models.CharField(max_length=45, null=True, db_column='tipoConstruccion', blank=True)),
            ],
            options={
                'db_table': 'incendio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('idmaterial', models.AutoField(serialize=False, primary_key=True, db_column='idMaterial')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialEvento',
            fields=[
                ('idmaterialevento', models.AutoField(serialize=False, primary_key=True, db_column='idMaterialEvento')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'material_evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materialhospital',
            fields=[
                ('idmaterialhospital', models.AutoField(serialize=False, primary_key=True, db_column='idMaterialHospital')),
                ('tipomaterial', models.CharField(max_length=45, null=True, db_column='tipoMaterial', blank=True)),
                ('cantidadmaterial', models.IntegerField(null=True, db_column='cantidadMaterial', blank=True)),
            ],
            options={
                'db_table': 'materialhospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materialmayor',
            fields=[
                ('idcarroevento', models.AutoField(serialize=False, primary_key=True, db_column='idCarroEvento')),
                ('conductor', models.CharField(max_length=45, null=True, blank=True)),
                ('oficialcargo', models.CharField(max_length=45, null=True, db_column='oficialCargo', blank=True)),
                ('horasalidacuartel', models.TimeField(null=True, db_column='horaSalidaCuartel', blank=True)),
                ('horallegadaevento', models.TimeField(null=True, db_column='horaLlegadaEvento', blank=True)),
                ('horasalidaevento', models.DateTimeField(null=True, db_column='horaSalidaEvento', blank=True)),
                ('horallegadacuartel', models.DateTimeField(null=True, db_column='horaLlegadaCuartel', blank=True)),
                ('kilometrajesalida', models.IntegerField(null=True, db_column='kilometrajeSalida', blank=True)),
                ('kilometrajellegada', models.IntegerField(null=True, db_column='kilometrajeLlegada', blank=True)),
            ],
            options={
                'db_table': 'materialmayor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materialpeligroso',
            fields=[
                ('idmaterialpeligroso', models.AutoField(serialize=False, primary_key=True, db_column='idMaterialPeligroso')),
                ('claveincendio', models.CharField(max_length=45, null=True, db_column='claveIncendio', blank=True)),
                ('tipomaterialpeligroso', models.CharField(max_length=45, null=True, db_column='tipoMaterialPeligroso', blank=True)),
                ('cantidadmaterialpeligroso', models.IntegerField(null=True, db_column='cantidadMaterialPeligroso', blank=True)),
                ('empresa', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'materialpeligroso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Motosierra',
            fields=[
                ('idmotosierra', models.AutoField(serialize=False, primary_key=True, db_column='idMotosierra')),
                ('numeromotosierra', models.IntegerField(null=True, db_column='numeroMotosierra', blank=True)),
                ('limpeza', models.CharField(max_length=45, null=True, blank=True)),
                ('estado', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'motosierra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('idtipo', models.AutoField(serialize=False, primary_key=True, db_column='idTipo')),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'tipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idvehiculo', models.AutoField(serialize=False, primary_key=True, db_column='idVehiculo')),
                ('tipo', models.CharField(max_length=45, null=True, blank=True)),
                ('marca', models.CharField(max_length=45, null=True, blank=True)),
                ('modelo', models.CharField(max_length=45, null=True, blank=True)),
                ('patente', models.CharField(max_length=45, null=True, blank=True)),
                ('dano', models.CharField(max_length=45, null=True, blank=True)),
                ('numeroadultos', models.IntegerField(null=True, db_column='numeroAdultos', blank=True)),
                ('numeroninos', models.IntegerField(null=True, db_column='numeroNinos', blank=True)),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('rut', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('fechanacimiento', models.DateField(db_column='fechaNacimiento')),
                ('ciudadnacimiento', models.CharField(max_length=45, db_column='ciudadNacimiento')),
                ('gruposanguineo', models.CharField(max_length=45, db_column='grupoSanguineo')),
                ('profesion', models.CharField(max_length=45, null=True, blank=True)),
                ('fechaingreso', models.DateField(db_column='fechaingreso')),
                ('fechasalida', models.DateField(db_column='fechasalida')),
                ('serviciomilitar', models.IntegerField(null=True, db_column='servicioMilitar', blank=True)),
                ('insignia', models.IntegerField(null=True, blank=True)),
                ('cargo', models.CharField(max_length=45, null=True, blank=True)),
                ('calificacion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'voluntario',
                'managed': False,
            },
        ),
    ]
