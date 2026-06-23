from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .services import recommend_box


class BoxRecommendationView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)

        box = recommend_box(order)

        if box is None:
            return Response({'error': 'No suitable box found'}, status=200)

        return Response({
            'order_id': order.id,
            'recommended_box': {
                'name': box.name,
                'dimensions': f"{box.length}x{box.width}x{box.height} cm",
                'max_weight': f"{box.max_weight} kg",
                'cost': str(box.cost),
            }
        })