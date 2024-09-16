# Roki's Corner

**Roki's Corner** is a web application built with Django that enables users to
create, customize, and manage their portfolio pages. Users can easily generate
and download their portfolios as CVs in PDF format, providing a convenient way
to showcase their professional experience and skills.

## Getting Started

### Prerequisites

- [Python 3.12+](https://www.python.org/)
- [Python Poetry](https://python-poetry.org/)
- [wkhtmltopdf](https://wkhtmltopdf.org/)

### Project Setup

1. Clone the repository:
    ```bash
    git clone git@github.com:roknicmilos/rokis-corner.git
    ```

2. Install the required packages:
    ```bash
    poetry install
    ```

3. Create a `.env` file in the root directory based on the `example.env` file
   <br/><br/>

4. Run migrations:
    ```bash
    poetry run python manage.py migrate
    ```

5. (Optional) Load (all) fixtures using custom management command:
    ```bash
    poetry run python manage.py load_fixtures
    ```
6. (Optional) Create a superuser with credentials defined in the `.env` file:
    ```bash
    poetry run python manage.py create_superuser
    ```

7. Start the **development** server:
    ```bash
    poetry run python manage.py runserver
    ```
   or the **production** server:
    ```bash
    poetry run gunicorn rokis_corner.wsgi
    ```

- If you created superuser, you can access Django Admin
  at http://localhost:8000/admin/
- If you loaded fixtures, you can check Eric's Cartman portfolio page
  at http://localhost:8000/eric-cartman/

## Use `systemd` to Manage Gunicorn

Using `systemd` to manage our Gunicorn server allows us to automatically start,
stop, and restart the Gunicorn process for our Django project as a service.
You can name the service file whatever you want, but it should end with
`.service`. We'll name our service file `rokis-corner.gunicorn.service`.

1. Create a new service file:
    ```bash
    sudo nano /etc/systemd/system/rokis-corner.gunicorn.service
    ```
2. Add the following configuration to the service file:
    ```ini
    [Unit]
    Description=gunicorn daemon
    After=network.target
    
    [Service]
    User={username}
    Group=www-data
    WorkingDirectory=/var/www/rokis-corner
    ExecStart=/path/to/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 rokis_corner.wsgi:application
    
    [Install]
    WantedBy=multi-user.target
    ```
    - Replace `{username}` with your username. Using `root` user is not
      recommended.
    - Replace `/var/www/rokis-corner` with the path to your project directory.
    - We use 3 workers for Gunicorn as it's a recommended number for minimal
      server resources (1 CPU core). Formula used to calculate the number of
      workers: `2 * cpu_cores + 1`.
    - Instead of binding Gunicorn to a TCP/IP socket (like `0.0.0.0:8000`), you
      can bind it to a Unix socket (e.g.
      `unix:/var/www/rokis-corner/rokis_corner.sock`). This is more secure and
      faster than binding to a TCP/IP socket. However, you'll need to configure
      a web server (e.g. Nginx) to communicate with Gunicorn via the Unix
      socket.
      <br/><br/>

3. Start the `rokis-corner.gunicorn` service:
    ```bash
    sudo systemctl start rokis-corner.gunicorn
    ```
   This will start the Gunicorn process for our Django project, and you
   should be able to access the website at http://localhost:8000

- Set service to start on boot:
  ```bash
  sudo systemctl enable rokis-corner.gunicorn
  ```
- Stop service:
  ```bash
  sudo systemctl stop rokis-corner.gunicorn
  ```
- Restart service:
  ```bash
  sudo systemctl restart rokis-corner.gunicorn
  ```
- Check service status:
  ```bash
  sudo systemctl status rokis-corner.gunicorn
  ```
- View logs:
    ```bash
    journalctl -u rokis-corner.gunicorn
    ```
