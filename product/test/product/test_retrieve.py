from django.urls import reverse
from rest_framework.test import APITestCase
from globals.test_objects import create_user, create_category, create_product


class TestRetrieveProduct (APITestCase) :


    def endpoint (self, id):
        return reverse('retrieve-product', args=[id])
    

    def test_retrieve_product_not_found(self):
        res = self.client.get(self.endpoint(1))
        self.assertEqual(res.status_code, 404)
    
    def test_success(self) : 
        pd = create_product()
        res = self.client.get(self.endpoint(pd.id))
        self.assertEqual(res.status_code, 200)
    

    def test_zero_quantity(self) : 
        pd = create_product(quantity=0)
        res = self.client.get(self.endpoint(pd.id))
        self.assertEqual(res.status_code, 404)