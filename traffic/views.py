from django.core.validators import validate_email
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from traffic.models import TrafficOfficer, TrafficViolation
from traffic.serializers import TrafficViolationSerializer


class ChargeViolationView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TrafficViolationSerializer

    def charge_violation(self, request):
        data = request.data
        user = request.user
        data['officer'] = TrafficOfficer.objects.get(user=user).id
        serializer = TrafficViolationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_report(self, request):
        try:
            validate_email(request.GET.get('email'))
            qs = TrafficViolation.objects.filter(plate_number__owner__email__exact=request.GET.get('email'))
            if qs:
                serializer = TrafficViolationSerializer(qs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'No violations found or email invalid'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': str(e)})