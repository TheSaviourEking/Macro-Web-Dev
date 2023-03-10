from django.shortcuts import get_object_or_404

from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin


class ProductMixinView(
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView,
                       mixins.CreateModelMixin,
                       ):
    queryset = Product.objects.all()
    serialzer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        pass
    def delete(self, request, *args, **kwargs):
        pass
    
    def perfom_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = "this is a single view performing miracles"
        serializer.save(content=content)
        return Response(serializer.data)
    
product_mixin_view = ProductMixinView().as_view()


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    def perfom_create(self, serializer):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        
    
product_list_create_view = ProductListCreateAPIView().as_view()


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView().as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
product_update_view = ProductUpdateAPIView().as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
product_destroy_view = ProductDestroyAPIView().as_view()
        
    
    
product_update_view = ProductUpdateAPIView().as_view



@api_view(['GET', 'POST'])
def product_alt_view(request,pk = None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        else:
            queryset  = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
        
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            price = serializer.validated_data.get('price')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
