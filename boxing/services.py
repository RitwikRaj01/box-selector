from .models import Box


def recommend_box(order):
    """
    Strategy:
    1. Sum total weight and total volume of all items in the order.
    2. Find all boxes that can fit the total volume AND support the weight.
    3. Among eligible boxes, pick the cheapest one.
    """
    total_weight = sum(
        item.product.weight * item.quantity
        for item in order.orderitem_set.select_related('product').all()
    )

    total_volume = sum(
        item.product.volume() * item.quantity
        for item in order.orderitem_set.select_related('product').all()
    )

    eligible_boxes = [
        box for box in Box.objects.all()
        if box.volume() >= total_volume and box.max_weight >= total_weight
    ]

    if not eligible_boxes:
        return None  # No suitable box found

    return min(eligible_boxes, key=lambda b: b.cost)