from rest_framework.serializers import ModelSerializer
from main import models


class StaffSerializerList(ModelSerializer):
    class Meta:
        model = models.Staff
        fields = "__all__"



class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'

