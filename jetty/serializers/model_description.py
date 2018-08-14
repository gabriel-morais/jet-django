from rest_framework import serializers

from jetty.models.model_description import ModelDescription


class ModelDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelDescription
        fields = (
            'app_label',
            'model',
            'params',
            'date_add'
        )
