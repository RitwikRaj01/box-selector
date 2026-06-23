# Box Selection System

A Django-based REST API that recommends the most suitable and cost-effective shipping box for an ecommerce order.

## Tech Stack
- Python 3.x
- Django 6.x
- Django REST Framework

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/box-selector.git
cd box-selector
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install django djangorestframework
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

## API Endpoint

### Get Box Recommendation

#### Success Response:
```json
{
    "order_id": 1,
    "recommended_box": {
        "name": "Small",
        "dimensions": "20.0x20.0x20.0 cm",
        "max_weight": "5.0 kg",
        "cost": "2.00"
    }
}
```

#### No Box Found Response:
```json
{
    "error": "No suitable box found"
}
```

## Box Recommendation Logic

1. Calculate total weight and total volume of all items in the order
2. Filter boxes that can fit the total volume AND support the total weight
3. Among eligible boxes, pick the cheapest one

## Running Tests
```bash
python manage.py test boxing
```