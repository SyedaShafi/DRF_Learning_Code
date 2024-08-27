from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # adding some read-only fields, these fields can not be updated
    # name = serializers.CharField(max_length=150, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # we can also use read_only_fields for multiple fields
        # read_only_fields = ['name', 'roll']
        # we can also use extra_kwargs
        # extra_kwargs = {'name': {'read_only': True}}
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

