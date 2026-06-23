from django.test import TestCase
from .models import Box, Product, Order, OrderItem
from .services import recommend_box


class BoxRecommendationTest(TestCase):

    def setUp(self):
        self.small_box = Box.objects.create(
            name="Small", length=20, width=20, height=20,
            max_weight=5, cost=2.00
        )
        self.large_box = Box.objects.create(
            name="Large", length=50, width=50, height=50,
            max_weight=20, cost=5.00
        )
        self.product = Product.objects.create(
            name="Book", length=15, width=10, height=5, weight=0.5
        )

    def test_recommends_cheapest_fitting_box(self):
        """Small box should be recommended for a single small product"""
        order = Order.objects.create()
        OrderItem.objects.create(order=order, product=self.product, quantity=1)
        box = recommend_box(order)
        self.assertEqual(box.name, "Small")

    def test_no_box_when_too_heavy(self):
        """Should return None when no box can handle the weight"""
        heavy = Product.objects.create(
            name="Iron Block", length=10, width=10, height=10, weight=100
        )
        order = Order.objects.create()
        OrderItem.objects.create(order=order, product=heavy, quantity=1)
        box = recommend_box(order)
        self.assertIsNone(box)

    def test_large_box_for_big_order(self):
        """Large box should be picked when small box cannot handle the weight"""
        heavy_product = Product.objects.create(
            name="Heavy Book", length=15, width=10, height=5, weight=3
        )
        order = Order.objects.create()
        OrderItem.objects.create(order=order, product=heavy_product, quantity=3)
        box = recommend_box(order)
        self.assertEqual(box.name, "Large")

    def test_no_box_found_returns_none(self):
        """Should return None when product is too big for all boxes"""
        huge = Product.objects.create(
            name="Huge Item", length=100, width=100, height=100, weight=1
        )
        order = Order.objects.create()
        OrderItem.objects.create(order=order, product=huge, quantity=1)
        box = recommend_box(order)
        self.assertIsNone(box)