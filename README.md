# Roki's Corner

**Roki's Corner** is a personal portfolio website built with Django, dedicated
to showcasing my work experience and projects. It's a space where I highlight my
professional journey, the skills I've developed, and the projects I've worked
on. Whether you're interested in my career path or the work I've done, Roki's
Corner provides a comprehensive view of my expertise.

## Getting Started

1. Clone the repository:
    ```bash
    git clone git@github.com:roknicmilos/rokis-corner.git
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install wkhtmltopdf (required
   by [django-pdf-view](https://pypi.org/project/django-pdf-view/) for
   generating PDFs):
    ```bash
    sudo apt install wkhtmltopdf
    ```

5. Create a `.env` file in the root directory based on the `example.env` file
   <br/><br/>

6. Run migrations:
    ```bash
    python manage.py migrate
    ```

7. (Optional) Load (all) fixtures using custom management command:
    ```bash
    python manage.py load_fixtures
    ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```

- If you loaded the fixtures, you can access some CVs on the following URLs:
    - http://localhost:8000/cv/eric-cartman/
- If you didn't load the fixtures, you can create a superuser and add CVs
  manually:
    ```bash
    python manage.py createsuperuser
    ```
    - Access the admin panel at http://localhost:8000/admin/ and add CVs
      manually