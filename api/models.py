# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import bcrypt
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.hashers import *
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
#from users.managers import CustomUserManager

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

'''

class CUser(AbstractBaseUser, PermissionsMixin):
    userid = models.AutoField(db_column='CUserID',primary_key=True)
    username = models.CharField(db_column='CUsername',max_length=40,unique=True)
    password = models.CharField(db_column='Password', max_length=1000)
    email = models.EmailField(db_column='Email',max_length=125,unique=True)
    firstname = models.CharField(db_column='FirstName', max_length=40, blank=True, null=True)
    lastname = models.CharField(db_column='LastName', max_length=40, blank=True, null=True)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

'''

class User(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', max_length=40)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=1000)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=40, blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return self.loginname

    def create(request):
        user = form.save(commit=False)
        user.loginname = request.get('loginame')
        user.firstname = request.get('firstname')
        user.lastname = request.get('lastname')
        user.password = bcrypt.hashpw(request.get('password'),bcrypt.gensalt())
        user.save()
        return redirect('user_list')

    def save(self,*args,**kwargs):
        self.password = make_password(self.password)
        super().save(*args,**kwargs)




    class Meta:
        managed = True
        db_table = 'user'
        #ordering = ['created']


class Actualtotalload(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    actiontaskid = models.BigIntegerField(db_column='ActionTaskID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    totalloadvalue = models.DecimalField(db_column='TotalLoadValue', max_digits=24, decimal_places=2)  # Field name made lowercase.
    areatypecodeid = models.ForeignKey('Areatypecode', models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)  # Field name made lowercase.
    areacodeid = models.ForeignKey('Allocatedeicdetail', models.DO_NOTHING, db_column='AreaCodeId')  # Field name made lowercase.
    resolutioncodeid = models.ForeignKey('Resolutioncode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)  # Field name made lowercase.
    mapcodeid = models.ForeignKey('Mapcode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)  # Field name made lowercase.
    rowhash = models.CharField(db_column='RowHash', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'actualtotalload'



class Aggregatedgenerationpertype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    actiontaskid = models.BigIntegerField(db_column='ActionTaskID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    actualgenerationoutput = models.DecimalField(db_column='ActualGenerationOutput', max_digits=24, decimal_places=2)  # Field name made lowercase.
    actualconsuption = models.DecimalField(db_column='ActualConsuption', max_digits=24, decimal_places=2)  # Field name made lowercase.
    areatypecodeid = models.ForeignKey('Areatypecode', models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)  # Field name made lowercase.
    areacodeid = models.ForeignKey('Allocatedeicdetail', models.DO_NOTHING, db_column='AreaCodeId')  # Field name made lowercase.
    resolutioncodeid = models.ForeignKey('Resolutioncode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)  # Field name made lowercase.
    mapcodeid = models.ForeignKey('Mapcode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)  # Field name made lowercase.
    productiontypeid = models.ForeignKey('Productiontype', models.DO_NOTHING, db_column='ProductionTypeId', blank=True, null=True)  # Field name made lowercase.
    rowhash = models.CharField(db_column='RowHash', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'aggregatedgenerationpertype'


class Allocatedeicdetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    mrid = models.CharField(db_column='MRID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    docstatusvalue = models.CharField(db_column='DocStatusValue', max_length=250, blank=True, null=True)  # Field name made lowercase.
    attributeinstancecomponent = models.CharField(db_column='AttributeInstanceComponent', max_length=250, blank=True, null=True)  # Field name made lowercase.
    longnames = models.CharField(db_column='LongNames', max_length=250, blank=True, null=True)  # Field name made lowercase.
    displaynames = models.CharField(db_column='DisplayNames', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lastrequestdateandortime = models.DateTimeField(db_column='LastRequestDateAndOrTime', blank=True, null=True)  # Field name made lowercase.
    deactivaterequestdateandortime = models.DateTimeField(db_column='DeactivateRequestDateAndOrTime', blank=True, null=True)  # Field name made lowercase.
    marketparticipantstreetaddresscountry = models.CharField(db_column='MarketParticipantStreetAddressCountry', max_length=250, blank=True, null=True)  # Field name made lowercase.
    marketparticipantacercode = models.CharField(db_column='MarketParticipantACERCode', max_length=250, blank=True, null=True)  # Field name made lowercase.
    marketparticipantvatcode = models.CharField(db_column='MarketParticipantVATcode', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eicparentmarketdocumentmrid = models.CharField(db_column='EICParentMarketDocumentMRID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    elcresponsiblemarketparticipantmrid = models.CharField(db_column='ELCResponsibleMarketParticipantMRID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.TextField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'allocatedeicdetail'


class Areatypecode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    areatypecodetext = models.CharField(db_column='AreaTypeCodeText', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    areatypecodenote = models.CharField(db_column='AreaTypeCodeNote', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'areatypecode'

'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

'''
class Dayaheadtotalloadforecast(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    actiontaskid = models.BigIntegerField(db_column='ActionTaskID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime')  # Field name made lowercase.
    totalloadvalue = models.DecimalField(db_column='TotalLoadValue', max_digits=24, decimal_places=2)  # Field name made lowercase.
    areatypecodeid = models.ForeignKey(Areatypecode, models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)  # Field name made lowercase.
    areacodeid = models.ForeignKey(Allocatedeicdetail, models.DO_NOTHING, db_column='AreaCodeId')  # Field name made lowercase.
    resolutioncodeid = models.ForeignKey('Resolutioncode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)  # Field name made lowercase.
    mapcodeid = models.ForeignKey('Mapcode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)  # Field name made lowercase.
    rowhash = models.CharField(db_column='RowHash', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dayaheadtotalloadforecast'

'''
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'

'''
class Mapcode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    mapcodetext = models.CharField(db_column='MapCodeText', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    mapcodenote = models.CharField(db_column='MapCodeNote', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mapcode'


class Productiontype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    productiontypetext = models.CharField(db_column='ProductionTypeText', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    productiontypenote = models.CharField(db_column='ProductionTypeNote', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'productiontype'


class Resolutioncode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitycreatedat = models.DateTimeField(db_column='EntityCreatedAt')  # Field name made lowercase.
    entitymodifiedat = models.DateTimeField(db_column='EntityModifiedAt')  # Field name made lowercase.
    resolutioncodetext = models.CharField(db_column='ResolutionCodeText', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    resolutioncodenote = models.CharField(db_column='ResolutionCodeNote', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'resolutioncode'

'''
class SnippetsSnippet(models.Model):
    created = models.DateTimeField()
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.IntegerField()
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    highlighted = models.TextField()

    class Meta:
        managed = True
        db_table = 'snippets_snippet'
'''
