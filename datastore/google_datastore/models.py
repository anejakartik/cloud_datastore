# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Tablea(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    created_on = models.DateField(blank=True, null=True)
    operation = models.CharField(max_length=500, blank=True, null=True)
    property_type = models.CharField(max_length=500, blank=True, null=True)
    place_name = models.CharField(max_length=500, blank=True, null=True)
    place_with_parent_names = models.CharField(max_length=500, blank=True, null=True)
    country_name = models.CharField(max_length=500, blank=True, null=True)
    state_name = models.CharField(max_length=500, blank=True, null=True)
    geonames_id = models.IntegerField(blank=True, null=True)
    lat_lon = models.CharField(max_length=500, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=500, blank=True, null=True)
    price_aprox_local_currency = models.FloatField(blank=True, null=True)
    price_aprox_usd = models.FloatField(blank=True, null=True)
    surface_total_in_m2 = models.IntegerField(blank=True, null=True)
    surface_covered_in_m2 = models.IntegerField(blank=True, null=True)
    price_usd_per_m2 = models.FloatField(blank=True, null=True)
    price_per_m2 = models.FloatField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    expenses = models.IntegerField(blank=True, null=True)
    properati_url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    image_thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablea'
