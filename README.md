# Django-based CV Renderer

This project implements a dynamic CV rendering system using Django web framework. The system takes structured CV data and presents it through an elegantly formatted web interface.

## Project Overview

The CV Renderer is built with:
- Django 5.1.6
- Python 3.12
- HTML5
- Standard Django Template Language (DTL)

## System Requirements

Before running this project, ensure you have the following prerequisites installed:
- Python 3.12 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation and Setup

1. **Install Required Dependencies**
   ```bash
   pip install django==5.1.6
   ```

2. **Clone the Project**
   ```bash
   git clone [your-repository-url]
   cd mycv
   ```

3. **Initialize Database**
   ```bash
   python manage.py migrate
   ```

## Running the Application

1. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   The server will start at http://127.0.0.1:8000/

2. **Access the CV**
   - Open your web browser
   - Navigate to http://127.0.0.1:8000/render/cv/
   - The CV should now be displayed in your browser

## License

This project is licensed under the MIT License - see the LICENSE file for details.