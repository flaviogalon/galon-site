# Galon's website

---
## Data Model

| Model | Attributes |
| ---   | :---: |
| Post | Title<br>Excerpt<br>Image Name<br>Date<br>Slug<br>Content |
| Author | First Name<br>Last Name<br>E-mail Address<br><br> One-to-Many relationship with **Post**<br><br> Many-to-Many relationship with **Tag** |
| Tag | Caption |