# Hello World Django App

This project is a simple Django web application designed to display a "Hello World" message in JSON format. This README outlines the steps to set up, run the application, and access the Hello World JSON response.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

Follow these steps to get your development environment set up:

1. **Clone the repository**

   ```bash
   git clone https://github.com/harikamareedu7/hello-world-django.git
   cd hello-world-django
   ```

## Running the Application

After cloning the project, you can run the application using the following steps:

1. **Apply migrations**

   Django requires you to migrate the database before running the server, even if you don't use it directly. This prepares the database for use:
   ```bash
   python manage.py migrate
   ```

2. **Start the Django development server**

   Run the following command to start the development server:
   ```bash
   python manage.py runserver
   ```

3. **Access the application**

   The server runs on `http://127.0.0.1:8000` by default. To access the Hello World JSON response, navigate to:
   ```text
   http://127.0.0.1:8000/hello-world/
   ```

   You should see the following JSON response in your browser:
   ```json
   {"Message": "Hello World!"}
   ```

   Also as additional part you can view an HTML page with a message (Hello World!) in bold. To see the page navigate to:
   ```text
   http://127.0.0.1:8000/hello-world/template
   ```
