from rest_framework import serializers

from traffic.models import TrafficViolation, Vehicle


class TrafficViolationSerializer(serializers.ModelSerializer):
    plate_number = serializers.CharField()
    comments = serializers.CharField(max_length=500)
    timestamp = serializers.DateTimeField()
    officer_fullname = serializers.SerializerMethodField('get_officer_fullname')

    class Meta:
        model = TrafficViolation
        fields = ['plate_number', 'comments', 'timestamp', 'officer', 'officer_fullname']
        read_only_fields = ['plate_number', 'officer_fullname']

    def get_officer_fullname(self, instance):
        return instance.officer.user.get_full_name()

    def validate_plate_number(self, value):
        '''
        Check if the vehicle exists
        '''
        if not value:
            raise serializers.ValidationError('Plate number is required')
        vehicle = Vehicle.objects.filter(plate_number=value).first()
        if not vehicle:
            raise serializers.ValidationError('Vehicle not found')
        return vehicle
