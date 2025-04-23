# Django REST API

This is a basic REST API project built with Django and Django REST Framework. It implements CRUD (Create, Read, Update, Delete) operations for a simple model.

## Features

- Complete CRUD operations implementation
- RESTful endpoints
- Error handling
- Data serialization
- SQLite database

## Requirements

- Python 3.13.2
- Django
- Django REST Framework

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AndreySuavita/Simple_Api.git
cd Simple_api_django
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start development server:
```bash
python manage.py runserver
```

## Project Structure

```
├── mi_app/
│   ├── models.py      # Model definition
│   ├── views.py       # API views
│   ├── urls.py        # URL configuration
│   └── serializers.py # Serializers
├── mi_proyecto/       # Project configuration
├── manage.py
└── requirements.txt
```

## API Endpoints

### GET /api/mimodelo_get/
- Get all objects
- Method: GET
- Response: List of objects

### POST /api/mimodelo_post/
- Create a new object
- Method: POST
- Request body:
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

### PUT /api/mimodelo_put_patch/{id}/
- Update an entire object
- Method: PUT
- Request body:
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

### DELETE /api/mimodelo_delete/{id}/
- Delete an object
- Method: DELETE

## Data Model

```python
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
```

### PATCH /api/mimodelo_put_patch/{id}/
- Update specific fields of an object
- Method: PATCH
- Request body (optional fields):
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

## Usage Examples

### Create a new object
```bash
curl -X POST http://localhost:8000/api/mimodelo_post/ \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Example", "descripcion": "Example description"}'
```

### Get all objects
```bash
curl http://localhost:8000/api/mimodelo_get/
```

### Update an object
```bash
curl -X PUT http://localhost:8000/api/mimodelo_put_patch/1/ \
     -H "Content-Type: application/json" \
     -d '{"nombre": "New Name", "descripcion": "New description"}'
```

### Delete an object
```bash
curl -X DELETE http://localhost:8000/api/mimodelo_delete/1/
```

### Update an object with patch
```bash
curl -X DELETE http://localhost:8000/api/mimodelo_put_patch/1/
```

