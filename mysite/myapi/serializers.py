from rest_framework import serializers

from .models import Sm


class SmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sm
        fields = ('id', 'name', 'mobilenumber', 'message', 'status')

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.name = validated_data.get('name', instance.name)
            instance.mobilenumber = validated_data.get('mobilenumber', instance.mobilenumber)
            instance.message = validated_data.get('message', instance.message)
            instance.status = validated_data.get('message', instance.status)

            instance.save()
            return instance