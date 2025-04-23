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
git clone [REPOSITORY_URL]
cd [DIRECTORY_NAME]
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

### GET /api/modelos/
- Get all objects
- Method: GET
- Response: List of objects

### POST /api/modelos/
- Create a new object
- Method: POST
- Request body:
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

### PUT /api/modelos/{id}/
- Update an entire object
- Method: PUT
- Request body:
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

### PATCH /api/modelos/{id}/
- Update specific fields of an object
- Method: PATCH
- Request body (optional fields):
```json
{
    "nombre": "string",
    "descripcion": "string"
}
```

### DELETE /api/modelos/{id}/
- Delete an object
- Method: DELETE

## Data Model

```python
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
```

## Usage Examples

### Create a new object
```bash
curl -X POST http://localhost:8000/api/modelos/ \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Example", "descripcion": "Example description"}'
```

### Get all objects
```bash
curl http://localhost:8000/api/modelos/
```

### Update an object
```bash
curl -X PUT http://localhost:8000/api/modelos/1/ \
     -H "Content-Type: application/json" \
     -d '{"nombre": "New Name", "descripcion": "New description"}'
```

### Delete an object
```bash
curl -X DELETE http://localhost:8000/api/modelos/1/
```


