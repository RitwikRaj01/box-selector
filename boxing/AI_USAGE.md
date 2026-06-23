# AI Usage Documentation

## AI Tools Used
- Claude (claude.ai)

## Prompts Given
1. "Help me design Django models for a box selection system with Box, Product, Order and OrderItem"
2. "Write a service function to recommend the cheapest fitting box based on volume and weight"
3. "Write an API view using Django REST Framework to return box recommendation for an order"
4. "Write test cases for the box recommendation logic"

## What I Accepted
- Basic model structure for Box, Product, Order, OrderItem
- URL routing setup
- Service function structure using volume and weight comparison
- API view structure using Django REST Framework

## What I Rejected / Modified
- AI initially suggested only volume-based comparison; I ensured weight check was also included
- AI's test case for large box used quantity=50 which actually exceeded weight limit of all boxes, returning None instead of Large box. I identified this logical error and fixed the test to use weight=3 with quantity=3 instead

## Mistakes AI Made
1. Pasting model code into wrong file (manage.py instead of models.py) during initial setup guidance
2. Wrote a flawed test case: `test_large_box_for_big_order` used 50 books weighing 0.5kg each (25kg total) which exceeded both box weight limits, so the function correctly returned None but the test expected "Large". I caught and fixed this.
3. AI's volume-only approach does not account for individual item shape/dimensions — noted as a known limitation

## How I Verified
- Ran all 4 test cases using `python manage.py test boxing`
- Verified server runs without errors using `python manage.py runserver`
- Manually checked migration output confirmed all models created correctly
- Reviewed service logic manually to confirm both weight and volume checks work correctly

## Known Limitations
- Box recommendation uses total volume, not individual item dimensions
- Real-world packing may require more complex 3D bin-packing algorithms