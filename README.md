# Project info

---
### Description
- Web application called 'health_app' that allows users to log
their daily symptoms. Over time, their data will be stored and
the user can view a chart with information about their health.

- Users may log in via the home page as well as register for the app.

- Once a user logs in, they will be prompted with a checklist of available symptoms
as well as take user inputs for notes, scale of
symptoms, and more. 

---

## Create an application with Python, Django, and SQLite Database using PyCharm.

### Setting up the project
*Must have PyCharm installed as well as Python to begin.*

https://www.python.org/downloads/

https://www.jetbrains.com/pycharm/download/

1. Create a new project
2. Select Django
3. Create

- Once a project is created all the necessary files 
for Django will be included

---

### Create the database

```python3 manage.py migrate```

![Screen Shot 2023-06-21 at 15.28.04 PM.png](health_app_python%2Fimg%2FScreen%20Shot%202023-06-21%20at%2015.28.04%20PM.png))

To confirm that the database has been added run ```ls```

Your folder should now contain a `db.sqlite3` file

---

### Run the project

`python3 manage.py runserver`

![Screen Shot 2023-06-21 at 15.28.59 PM.png](health_app_python%2Fimg%2FScreen%20Shot%202023-06-21%20at%2015.28.59%20PM.png)

Click the link to go to the web-page.
You should see a page created by Django, which lets you know
the server is running properly.

![Screen Shot 2023-06-21 at 15.32.45 PM.png](health_app_python%2Fimg%2FScreen%20Shot%202023-06-21%20at%2015.32.45%20PM.png)

---

### Possible errors

If you get an error message after the last step
try changing the port number.


`python3 manage.py runserver 8001`

If this does not work, try other port numbers with the same command

---

### Create infrastructure to build app

`python3 manage.py startapp health_app`

Notice the name is different from the original. This creates a directory inside the root.


In the new directory: *models.py, admin.py, and views.py*
are created.