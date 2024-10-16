# from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.    
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self, request):
        menu_item = request.data.get('menu_item')

        # Create an article from the above data
        serializer = MenuSerializer(data=menu_item)
        if serializer.is_valid(raise_exception=True):
            menu_item_saved = serializer.save()
        return Response({"success": "Menu item '{}' created successfully".format(menu_item_saved.title)})
    
class SingleMenuItemView(RetrieveAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def put(self, request, pk):
        saved_menu_item = Menu.objects.get(pk=pk)
        data = request.data.get('menu_item')
        serializer = MenuSerializer(instance=saved_menu_item, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            menu_item_saved = serializer.save()
        return Response({"success": "Menu item '{}' updated successfully".format(menu_item_saved.title)})

    def delete(self, request, pk):
        menu_item = Menu.objects.get(pk=pk)
        menu_item.delete()
        return Response({"message": "Menu item with id `{}` has been deleted.".format(pk)},status=204)
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]