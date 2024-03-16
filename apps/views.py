from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Product, Category
from apps.models import User
from apps.permissions import IsOwnerOrReadOnly
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, RegisterModelSerializer
from apps.utils import send_verification_email


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

    def get_success_headers(self, data):
        import uuid
        _uuid = uuid.uuid4()
        send_verification_email(data['email'], _uuid.__str__())
        cache.set(_uuid, data['email'])
        print('sent email!')
        return super().get_success_headers(data)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    pagination_class = None


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    filterset_fields = ('name', 'description')
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        if search := self.request.GET.get('search', ):
            return queryset.filter(name__icontains=search)
        return queryset

    def gett_queryset(self):
        return super().get_queryset().filter(owner_id=self.request.user.id)


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    serializer_class = ProductModelSerializer
    http_method_names = ['put', 'delete', 'patch']