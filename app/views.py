from .serializers import CompanySerializer, CompanyListSerializer, EmployeeListSerializer, PartnershipListSerializer, PartnershipSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Company, Employee, Partnership

class SerializerMixin(object):
    def get_serializer_class(self):
        return self.serializers.get(self.action)

class CompanyView(SerializerMixin, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializers = {'retrieve': CompanySerializer, 'list': CompanyListSerializer, 'create': CompanySerializer, 'update': CompanySerializer}
    queryset = Company.objects.all()
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method == 'PUT':
            return [IsAdminUser()]

class EmployeeView(SerializerMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializers = {'list': EmployeeListSerializer}
    queryset = Employee.objects.all()
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)

class PartnershipView(SerializerMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializers = {'list': PartnershipListSerializer, 'create': PartnershipSerializer}
    queryset = Partnership.objects.all()
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]