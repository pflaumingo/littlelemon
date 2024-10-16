from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
# from restaurant.views import MenuItemView, SingleMenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        request = self.client.get('/restaurant/menu/')
        self.assertEqual(request.status_code, 200)
    
    def test_getall(self):
        request = self.client.get('/restaurant/menu/')
        data = MenuSerializer (Menu.objects.all(), many=True).data
        self.assertEqual(request.data, data)