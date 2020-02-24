from rest_framework import serializers
from api.models import *
import bcrypt


class AreatypecodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Areatypecode
        fields = ['id','entitycreatedat','entitymodifiedat','areatypecodetext','areatypecodenote']

    def create(self,valdated_data):
        return Areatypecode.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.areatypecodetext = validated_data.get('areatypecodetext',instance.areatypecodetext)
        instance.areatypecodenote = validated_data.get('areatypecodenote',instance.areatypecodenote)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['userid','loginname','password','firstname','lastname']

    def create(self,validated_data):
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.loginname = validated_data.get('loginname',instance.loginname)
        pp = validated_data.get('password',instance.password)
        newp = bcrypt.hashpw(pp,bcrypt.gensalt())
        instance.password = newp
        instance.firstname = validated_data.get('firstname',instance.firstname)
        instance.LastName = validated_data.get('LastName',instance.lastname)


class ActualtotalloadSerializer(serializers.HyperlinkedModelSerializer):
    areatypecode = AreatypecodeSerializer(many = True,read_only=True)
    class Meta:
        model = Actualtotalload
        fields =['year','month','day','areatypecode']

    '''def t0_representation(self,obj):
        serializer_data = super(ActualtotalloadSerializer,self).to_representation(obj)
        areacode_id = serializer_data.get('areacodeid')
        areacode = Areatypecode.objects.get(areatypecodetext = areacode_id)
        serializer_data['areacode'] = areacode
        serializer_data['year'] = 2017
        return serializer_data'''

    def create(self,validated_data):
        return Actualtotalload.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.actiontaskid = validated_data.get('actiontaskid',instance.actiontaskid)
        instance.status = validated_data.get('status',instance.status)
        instance.year = validated_data.get('year',instance.year)
        instance.day = validated_data.get('day',instance.day)
        instance.datetime = validated_data.get('datetime',instance.datetime)
        instance.areaname = validated_data.get('areaname',instance.areaname)
        instance.updatetime = validated_data.get('updatetime',instance.updatetime)
        instance.totalloadvalue = validated_data.get('totalloadvalue',instance.totalloadvalue)
        instance.areatypecodeid = validated_data.get('areatypecodeid',instance.areatypecodeid)
        instance.areacodeid = validated_data.get('areacodeid',instance.areacodeid)
        instance.resolutioncodeid = validated_data.get('resolutioncodeid',instance.resolutioncodeid)
        instance.mapcodeid = validated_data.get('mapcodeid',instance.mapcodeid)
        instance.rowhash = validated_data.get('rowhash',instance.rowhash)

class AggregatedgenerationpertypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aggregatedgenerationpertype
        fields = ['id','entitycreatedat','entitymodifiedat','actiontaskid','status','year','month','day','datetime','areaname','updatetime','actualgenerationoutput','actualconsuption','areatypecodeid','areacodeid','resolutioncodeid','mapcodeid','productiontypeid','rowhash']

    def create(self,validated_data):
        return Aggregatedgenerationpertype.objects.create(**validated_add)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.actiontaskid = validated_data.get('actiontaskid',instance.actiontaskid)
        instance.status = validated_data.get('status',instance.status)
        instance.year = validated_data.get('year',instance.year)
        instance.month = validated_data.get('month',instance.month)
        instance.day = validated_data.get('day',instance.day)
        instance.datetime = validated_data.get('datetime',instance.datetime)
        instance.areaname = validated_data.get('areaname',instance.areaname)
        instance.updatetime = validated_data.get('updatetime',instance.updatetime)
        instance.actualgenerationoutput = validated_data.get('actualgenerationoutput',instance.actualgenerationoutput)
        instance.actualconsuption = validated_data.get('actualconsuption',instance.actualconsuption)
        instance.areatypecodeid = validated_data.get('areatypecodeid',instance.areatypecodeid)
        instance.areacodeid = validated_data.get('areacodeid',instance.areacodeid)
        instance.resolutioncodeid = validated_data.get('resolutioncodeid',instance.resolutioncodeid)
        instance.mapcodeid = validated_data.get('mapcodeid',instance.mapcodeid)
        instance.productiontypeid = validated_data.get('productiontypeid',instance.productiontypeid)
        instance.rowhash = validated_data.get('rowhash',instance.rowhash)

class AllocatedeicdetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allocatedeicdetail
        fields = ['id','entitycreatedat','entitymodifiedat','mrid','docstatusvalue','attributeinstancecomponent','longnames','displaynames','lastrequestdateandortime','deactivaterequestdateandortime','marketparticipantstreetaddresscountry','marketparticipantacercode','marketparticipantvatcode','description','eicparentmarketdocumentmrid','elcresponsiblemarketparticipantmrid','isdeleted']

    def create(self,valdated_data):
        return Allocatedeicdetail.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.mrid = validated_data.get('mrid',instance.mrid)
        instance.docstatusvalue = validated_data.get('docstatusvalue',instance.docstatusvalue)
        instance.attributeinstancecomponent = validated_data.get('attributeinstancecomponent',instance.attributeinstancecomponent)
        instance.longnames = validated_data.get('longnames',instance.longnames)
        instance.displaynames = validated_data.get('displaynames',instance.displaynames)
        instance.lastrequestdateandortime = validated_data.get('lastrequestdateandortime',instance.lastrequestdateandortime)
        instance.deactivaterequestdateandortime = validated_data.get('deactivaterequestdateandortime',instance.deactivaterequestdateandortime)
        instance.marketparticipantstreetaddresscountry = validated_data.get('marketparticipantstreetaddresscountry',instance.marketparticipantstreetaddresscountry)
        instance.marketparticipantacercode = validated_data.get('marketparticipantacercode',instance.marketparticipantacercode)
        instance.marketparticipantvatcode = validated_data.get('marketparticipantvatcode',instance.marketparticipantvatcode)
        instance.description = validated_data.get('description',instance.description)
        instance.eicparentmarketdocumentmrid = validated_data.get('eicparentmarketdocumentmrid',instance.eicparentmarketdocumentmrid)
        instance.elcresponsiblemarketparticipantmrid = validated_data.get('elcresponsiblemarketparticipantmrid',instance.elcresponsiblemarketparticipantmrid)
        instance.isdeleted = validated_data.get('isdeleted',instance.isdeleted)




class ResolutioncodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resolutioncode
        fields = ['id','entitycreatedat','entitymodifiedat','resolutioncodetext','resolutioncodenote']

    def create(self,validated_data):
        return Resolutioncode.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.resolutioncodetext = validated_data.get('resolutioncodetext',instance.resolutioncodetext)
        instance.resolutioncodenote = validated_data.get('resolutioncodenote',instance.resolutioncodenote)

class ProductiontypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productiontype
        fields = ['id','entitycreatedat','entitymodifiedat','productiontypetext','productiontypenote']

    def create(self,validated_data):
        return Productiontype.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.productiontypetext = validated_data.get('productiontypetext',instance.productiontypetext)
        instance.productiontypenote = validated_data.get('productiontypenote',instance.productiontypenote)

class MapcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mapcode
        fields = ['id','entitycreatedat','entitymodifiedat','mapcodetext','mapcodenote']

    def create(self,validated_data):
        return Mapcode.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.productiontypetext = validated_data.get('productiontypetext',instance.productiontypetext)
        instance.productiontypenote = validated_data.get('productiontypenote',instance.productiontypenote)

class DayaheadtotalloadforecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dayaheadtotalloadforecast
        fields = ['id','entitycreatedat','entitymodifiedat','actiontaskid','status','year','month','day','datetime','areaname','updatetime','totalloadvalue','areatypecodeid','areacodeid','resolutioncodeid','mapcodeid','rowhash']

    def create(self,validated_data):
        return Dayaheadtotalloadforecast.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.entitycreatedat = validated_data.get('entitycreatedat',instance.entitycreatedat)
        instance.entitymodifiedat = validated_data.get('entitymodifiedat',instance.entitymodifiedat)
        instance.actiontaskid = validated_data.get('actiontaskid',instance.actiontaskid)
        instance.status = validated_data.get('status',instance.status)
        instance.year = validated_data.get('year',instance.year)
        instance.month = validated_data.get('month',instance.month)
        instance.day = validated_data.get('day',instance.day)
        instance.datetime = validated_data.get('datetime',instance.datetime)
        instance.areaname = validated_data.get('areaname',instance.areaname)
        instance.updatetime = validated_data.get('updatetime',instance.updatetime)
        instance.totalloadvalue = validated_data.get('totalloadvalue',instance.totalloadvalue)
        instance.areatypecodeid = validated_data.get('areatypecodeid',instance.areatypecodeid)
        instance.areacodeid = validated_data.get('areacodeid',instance.areacodeid)
        instance.resolutioncodeid = validated_data.get('resolutioncodeid',instance.resolutioncodeid)
        instance.mapcodeid = validated_data.get('mapcodeid',instance.mapcodeid)
        instance.rowhash = validated_data.get('rowhash',instance.rowhash)
