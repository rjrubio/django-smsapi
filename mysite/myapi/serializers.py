from rest_framework import serializers

from .models import Sm
from .models import College
from .models import Meta
from .models import Device


class SmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sm
        fields = ('id', 'name', 'mobilenumber', 'message', 'status')

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.name = validated_data.get('name', instance.name)
            instance.mobilenumber = validated_data.get('mobilenumber', instance.mobilenumber)
            instance.message = validated_data.get('message', instance.message)
            instance.status = validated_data.get('status', instance.status)

            instance.save()
            return instance


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'device_id', 'device_model', 'device_manufacturer','clinicid', 'status', 'created_document_timestamp')

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.device_id = validated_data.get('device_id', instance.device_id)
            instance.device_model = validated_data.get('device_model', instance.device_model)
            instance.device_manufacturer = validated_data.get('device_manufacturer', instance.device_manufacturer)
            instance.status = validated_data.get('status', instance.status)
            instance.clinicid = validated_data.get('clinicid', instance.clinicid)
            instance.created_document_timestamp = validated_data.get('created_document_timestamp', instance.created_document_timestamp)
            print(instance)
            instance.save()
            return instance


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'college_name', 'status', 'created_at')

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.college_name = validated_data.get('college_name', instance.college_name)
            instance.status = validated_data.get('status', instance.status)
            instance.created_at = validated_data.get('created_at', instance.created_at)

            instance.save()
            return instance


class MetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meta
        fields = ('id', 'client_id', 'timestamp')

        def update(self, instance, validated_data):
            instance.id = validated_data.get('client_id', instance.id)
            instance.created_at = validated_data.get('timestamp', instance.created_at)

            instance.save()
            return instance
