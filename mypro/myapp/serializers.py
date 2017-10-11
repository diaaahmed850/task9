from rest_framework import serializers
from .models import data
class dataserializer(serializers.ModelSerializer):
    class Meta:
        model=data
        fields=('ProfilePicture','Name','Email','Mobile','NationalId','University','Faculty','Major','Minor','ExpectedGraduationYear')
        #fields=(__all__)