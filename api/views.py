from main import models 
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone



@api_view(['GET'])
def staff_list(request):
    """For staff list"""
    staff=models.Staff.objects.all()
    serializer_date = serializers.StaffSerializerList(staff, many=True)

    return Response(serializer_date.data)


@api_view(['POST'])
def attendance_create(request):
    """create reports"""
    serializer_data = serializers.AttendanceSerializer(data=request.data)
    if serializer_data.is_valid():
        staff = serializer_data.validated_data.get('staff')
        start_time = serializer_data.validated_data.get('start_time')
        end_time = serializer_data.validated_data.get('end_time')

        if not start_time:
            start_time = timezone.now()
            serializer_data.validated_data['start_time'] = start_time

        last_attendance = models.Attendance.objects.filter(staff=staff).last()

        if last_attendance and not end_time:
            last_attendance.end_time = start_time
            last_attendance.save()
        else:
            serializer_data.save()

        return Response({'success': True})
    return Response({'success': False})