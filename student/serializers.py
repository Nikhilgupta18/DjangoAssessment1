from rest_framework import serializers
from student import models


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        fields = '__all__'
        



class StudentSerializer(serializers.ModelSerializer):

    section = SectionSerializer()

    class Meta:
        model = models.Student
        fields = '__all__'

    def create(self, validated_data):
        section_data = validated_data.pop('section')
        section_instance, created = models.Section.objects.get_or_create(**section_data)
        student_instance = models.Student.objects.create(section=section_instance, **validated_data)
        return student_instance
    
    
    
    
    
