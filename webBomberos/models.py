# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Acompanante(models.Model):
    idacompanante = models.AutoField(db_column='idAcompanante', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    rut = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    fk_idvehiculo = models.ForeignKey('Vehiculo', db_column='fk_idVehiculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acompanante'


class AfectadoIncendio(models.Model):
    idafectado = models.AutoField(db_column='idAfectado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    rut = models.CharField(max_length=45, blank=True, null=True)
    tipoafectado = models.CharField(db_column='tipoAfectado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroadulto = models.IntegerField(db_column='numeroAdulto', blank=True, null=True)  # Field name made lowercase.
    numeroninos = models.IntegerField(db_column='numeroNinos', blank=True, null=True)  # Field name made lowercase.
    danovivienda = models.IntegerField(db_column='danoVivienda', blank=True, null=True)  # Field name made lowercase.
    danoenseres = models.IntegerField(db_column='danoEnseres', blank=True, null=True)  # Field name made lowercase.
    superficie = models.IntegerField(blank=True, null=True)
    fk_idincendioafectado = models.ForeignKey('Incendio', db_column='fk_idIncendioAfectado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afectado_incendio'


class AfectadoRescate(models.Model):
    idrescate = models.AutoField(db_column='idRescate', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    rut = models.CharField(max_length=45, blank=True, null=True)
    tipoafectado = models.CharField(db_column='tipoAfectado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=45, blank=True, null=True)
    fk_ideventorescate = models.ForeignKey('Evento', db_column='fk_idEventoRescate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'afectado_rescate'


class Apoyo(models.Model):
    idapoyo = models.AutoField(db_column='idApoyo', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)
    procedencia = models.CharField(max_length=45, blank=True, null=True)
    personacargo = models.CharField(db_column='personaCargo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rango = models.CharField(max_length=45, blank=True, null=True)
    patente = models.CharField(max_length=45, blank=True, null=True)
    compania = models.CharField(max_length=45, blank=True, null=True)
    municipalidad = models.CharField(max_length=45, blank=True, null=True)
    fk_ideventoapoyo = models.ForeignKey('Evento', db_column='fk_idEventoApoyo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apoyo'


class AseguradoraVehiculo(models.Model):
    idaseguradora_vehiculo = models.AutoField(db_column='idAseguradora_vehiculo', primary_key=True)  # Field name made lowercase.
    poliza = models.CharField(max_length=45, blank=True, null=True)
    compania = models.CharField(max_length=45, blank=True, null=True)
    especie = models.CharField(max_length=45, blank=True, null=True)
    fk_idaseguradoravehiculo = models.ForeignKey('Vehiculo', db_column='fk_idAseguradoraVehiculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aseguradora_vehiculo'


class AseguradoraViviendaAfectado(models.Model):
    idaseguradora_afectado = models.AutoField(primary_key=True)
    poliza = models.CharField(max_length=45, blank=True, null=True)
    compania = models.CharField(max_length=45, blank=True, null=True)
    especie = models.CharField(max_length=45, blank=True, null=True)
    fk_idafectado = models.ForeignKey(AfectadoIncendio, db_column='fk_idAfectado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aseguradora_vivienda_afectado'


class Asistencia(models.Model):
    idasistencia = models.AutoField(db_column='idAsistencia', primary_key=True)  # Field name made lowercase.
    fk_rut = models.ForeignKey('Voluntario', db_column='fk_rut', blank=True, null=True)
    fk_idevento = models.ForeignKey('Evento', db_column='fk_idEvento', blank=True, null=True)  # Field name made lowercase.
    codigoasistencia = models.CharField(db_column='codigoAsistencia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    asistenciaobligatoria = models.IntegerField(db_column='asistenciaObligatoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asistencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Carro(models.Model):
    idcarro = models.AutoField(db_column='idCarro', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carro'


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Compania(models.Model):
    idcompania = models.AutoField(db_column='idCompania', primary_key=True)  # Field name made lowercase.
    registrocompania = models.CharField(db_column='registroCompania', max_length=45)  # Field name made lowercase.
    clave = models.CharField(max_length=45)
    calle = models.CharField(max_length=45)
    numerocalle = models.CharField(db_column='numeroCalle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(max_length=45)
    nombrecompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compania'


class Companiavoluntario(models.Model):
    idcompaniavoluntario = models.AutoField(db_column='idCompaniaVoluntario', primary_key=True)  # Field name made lowercase.
    fk_companiavol = models.ForeignKey('Compania', db_column='fk_companiavol', blank=True, null=True)
    fk_vol = models.ForeignKey('Voluntario', db_column='fk_vol', blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    fechasalida = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companiavoluntario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Era(models.Model):
    idera = models.AutoField(db_column='idEra', primary_key=True)  # Field name made lowercase.
    numeroarne = models.IntegerField(db_column='numeroArne', blank=True, null=True)  # Field name made lowercase.
    numeromascara = models.IntegerField(db_column='numeroMascara', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=45, blank=True, null=True)
    fk_ideventoera = models.ForeignKey('Evento', db_column='fk_idEventoEra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'era'


class Evento(models.Model):
    idevento = models.AutoField(db_column='idEvento', primary_key=True)  # Field name made lowercase.
    correlativollamado = models.CharField(db_column='correlativoLlamado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correlativocbv = models.CharField(db_column='correlativoCBV', max_length=45, blank=True, null=True)  # Field name made lowercase.
    claveservicio = models.CharField(db_column='claveServicio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='fecha', auto_now_add=True)
    motivo = models.CharField(db_column='motivo',max_length=45, blank=True, null=True)
    calle = models.CharField(db_column='calle',max_length=45, blank=True, null=True)
    numerocalle = models.IntegerField(db_column='numeroCalle', blank=True, null=True)  # Field name made lowercase.
    calleproxima = models.CharField(db_column='calleProxima', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(max_length=45, blank=True, null=True)
    poblacion = models.CharField(max_length=45, blank=True, null=True)
    ruta = models.CharField(max_length=45, blank=True, null=True)
    kilometroruta = models.IntegerField(db_column='kilometroRuta', blank=True, null=True)  # Field name made lowercase.
    fk_bomberocargo = models.ForeignKey('Voluntario', related_name='bomberocargo',db_column='fk_bomberoCargo', blank=True, null=True)  # Field name made lowercase.
    fk_bomberoinforme = models.ForeignKey('Voluntario', related_name='bomberoinforme',db_column='fk_bomberoInforme', blank=True, null=True)  # Field name made lowercase.
    codigocargo = models.CharField(db_column='codigoCargo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigoinforme = models.CharField(db_column='codigoInforme', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerodepartamento = models.CharField(db_column='numeroDepartamento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroblock = models.CharField(db_column='numeroBlock', max_length=45, blank=True, null=True)  # Field name made lowercase.
    resumen = models.CharField(max_length=45, blank=True, null=True)
    fk_idcompaniae = models.ForeignKey(Compania, db_column='fk_idCompaniaE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evento'


class Gas(models.Model):
    idgas = models.AutoField(db_column='idGas', primary_key=True)  # Field name made lowercase.
    tipocontenedor = models.CharField(db_column='tipoContenedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipogas = models.CharField(db_column='tipoGas', max_length=45, blank=True, null=True)  # Field name made lowercase.
    capacidad = models.IntegerField(blank=True, null=True)
    empresa = models.CharField(max_length=45, blank=True, null=True)
    fk_idincendiogas = models.ForeignKey('Incendio', db_column='fk_idIncendioGas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gas'


class Incendio(models.Model):
    idincendio = models.AutoField(db_column='idIncendio', primary_key=True)  # Field name made lowercase.
    tipoincendio = models.CharField(db_column='tipoIncendio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    faseincendio = models.CharField(db_column='faseIncendio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    det = models.IntegerField(blank=True, null=True)
    bomberodet = models.CharField(db_column='bomberoDet', max_length=45, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(max_length=45, blank=True, null=True)
    causa = models.CharField(max_length=45, blank=True, null=True)
    fuentecalor = models.CharField(db_column='fuenteCalor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipolugar = models.CharField(db_column='tipoLugar', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipoconstruccion = models.CharField(db_column='tipoConstruccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fk_ideventoinc = models.ForeignKey(Evento, db_column='fk_idEventoInc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incendio'


class Material(models.Model):
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    fk_idcarro = models.ForeignKey(Carro, db_column='fk_idCarro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material'


class MaterialEvento(models.Model):
    idmaterialevento = models.AutoField(db_column='idMaterialEvento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    fk_idmaterial = models.ForeignKey(Material, db_column='fk_idMaterial', blank=True, null=True)  # Field name made lowercase.
    fk_ideventomaterial = models.ForeignKey(Evento, db_column='fk_idEventoMaterial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material_evento'


class Materialhospital(models.Model):
    idmaterialhospital = models.AutoField(db_column='idMaterialHospital', primary_key=True)  # Field name made lowercase.
    tipomaterial = models.CharField(db_column='tipoMaterial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cantidadmaterial = models.IntegerField(db_column='cantidadMaterial', blank=True, null=True)  # Field name made lowercase.
    fk_ideventohospital = models.ForeignKey(Evento, db_column='fk_idEventoHospital', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materialhospital'


class Materialmayor(models.Model):
    idcarroevento = models.AutoField(db_column='idCarroEvento', primary_key=True)  # Field name made lowercase.
    conductor = models.CharField(max_length=45, blank=True, null=True)
    oficialcargo = models.CharField(db_column='oficialCargo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horasalidacuartel = models.TimeField(db_column='horaSalidaCuartel', blank=True, null=True)  # Field name made lowercase.
    horallegadaevento = models.TimeField(db_column='horaLlegadaEvento', blank=True, null=True)  # Field name made lowercase.
    horasalidaevento = models.DateTimeField(db_column='horaSalidaEvento', blank=True, null=True)  # Field name made lowercase.
    horallegadacuartel = models.DateTimeField(db_column='horaLlegadaCuartel', blank=True, null=True)  # Field name made lowercase.
    fk_idcarromaterial = models.ForeignKey(Carro, db_column='fk_idCarroMaterial', blank=True, null=True)  # Field name made lowercase.
    fk_ideventomateriales = models.ForeignKey(Evento, db_column='fk_idEventoMateriales', blank=True, null=True)  # Field name made lowercase.
    kilometrajesalida = models.IntegerField(db_column='kilometrajeSalida', blank=True, null=True)  # Field name made lowercase.
    kilometrajellegada = models.IntegerField(db_column='kilometrajeLlegada', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materialmayor'


class Materialpeligroso(models.Model):
    idmaterialpeligroso = models.AutoField(db_column='idMaterialPeligroso', primary_key=True)  # Field name made lowercase.
    claveincendio = models.CharField(db_column='claveIncendio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipomaterialpeligroso = models.CharField(db_column='tipoMaterialPeligroso', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cantidadmaterialpeligroso = models.IntegerField(db_column='cantidadMaterialPeligroso', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(max_length=45, blank=True, null=True)
    fk_idincendio = models.ForeignKey(Incendio, db_column='fk_idIncendio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materialpeligroso'


class Motosierra(models.Model):
    idmotosierra = models.AutoField(db_column='idMotosierra', primary_key=True)  # Field name made lowercase.
    numeromotosierra = models.IntegerField(db_column='numeroMotosierra', blank=True, null=True)  # Field name made lowercase.
    limpeza = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    fk_ideventomotosierra = models.ForeignKey(Evento, db_column='fk_idEventoMotosierra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'motosierra'


class Tipo(models.Model):
    idtipo = models.AutoField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fk_idcategoria = models.ForeignKey(Categoria, db_column='fk_idCategoria', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'


class Vehiculo(models.Model):
    idvehiculo = models.AutoField(db_column='idVehiculo', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    patente = models.CharField(max_length=45, blank=True, null=True)
    dano = models.CharField(max_length=45, blank=True, null=True)
    numeroadultos = models.IntegerField(db_column='numeroAdultos', blank=True, null=True)  # Field name made lowercase.
    numeroninos = models.IntegerField(db_column='numeroNinos', blank=True, null=True)  # Field name made lowercase.
    fk_idrescate = models.ForeignKey(AfectadoRescate, db_column='fk_idRescate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehiculo'


class Voluntario(models.Model):
    rut = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=45)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    ciudadnacimiento = models.CharField(db_column='ciudadNacimiento', max_length=45)  # Field name made lowercase.
    gruposanguineo = models.CharField(db_column='grupoSanguineo', max_length=45)  # Field name made lowercase.
    profesion = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaingreso')
    fechasalida = models.DateField(db_column='fechasalida')
    serviciomilitar = models.IntegerField(db_column='servicioMilitar', blank=True, null=True)  # Field name made lowercase.
    insignia = models.IntegerField(blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)
    calificacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voluntario'
