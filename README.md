# Django Capstone Project

This is a Django project developed as part of the Capstone Project.

## Prerequisites
- Python 3.x
- Django
- Docker

## Installation
1. Clone this repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the Application
- Run the Django development server: `python manage.py runserver`
- To run the application with Docker, follow these steps:
  1. Build the Docker image: `docker build -t my_django_app .`
  2. Run the Docker container: `docker run -p 8000:8000 my_django_app`

## Additional Information
- For more information, refer to the [documentation](./docs/index.html).
