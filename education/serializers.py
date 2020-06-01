from rest_framework import serializers
from .models import Education
from . import models
from datetime import date

class EducatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'institution_name', 'qualification_name', 'start_date', 'end_date', 'currently_studying', 'user', 'created_on')

    def create(self, validated_data):
        if validated_data["start_date"] > date.today():
            raise serializers.ValidationError("Start date cannot be in future");
        elif validated_data["end_date"] > date.today():
            raise serializers.ValidationError("End date cannot be in future");
        elif validated_data["end_date"] < validated_data["start_date"]:
            raise serializers.ValidationError("End date cannot be before start date.");

        # Save job
        education = models.Education(
            institution_name=validated_data["institution_name"],
            start_date=validated_data["start_date"],
            end_date=validated_data["end_date"],
            qualification_name=validated_data["qualification_name"],
            currently_studying=validated_data["currently_studying"],
        )

        education.save()
        return education
