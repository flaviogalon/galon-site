# Galon's website
Built with Django

## Running
1. Install requirements with

    ```sh
    pip install -r requirements.txt
    ```
2. Run migrations with
    ```sh
    python manage.py migrate
    ```
3. Run local server with
    ```sh
    python manage.py runserver
    ```

---
## Data Model

| Model | Attributes |
| ---   | :---: |
| Post | Title<br>Excerpt<br>Image Name<br>Date<br>Slug<br>Content |
| Author | First Name<br>Last Name<br>E-mail Address<br><br> One-to-Many relationship with **Post**<br><br> Many-to-Many relationship with **Tag** |
| Tag | Caption |