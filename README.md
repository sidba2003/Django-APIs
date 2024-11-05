# Django Web App

### Install backend (Python) dependencies

install the backend (Python) dependencies:

```console
$ pip install -r requirements.txt
```

The main backend dependencies (see requirements.txt) are the Django framework itself (Django) and [django-cors-headers](https://pypi.org/project/django-cors-headers/) which is needed for CORS requests (since the request origin address http://localhost:5713 is different from the address that sent the JavaScript code to the browser http://localhost:8000).

### Start backend server

To start the backend server cd into the backend folder where the manage.py file is (if not already there)

```console
$ cd backend
```

and run

```console
$ python manage.py runserver
```

The server will start on http://localhost:8000

### API app

An "api" Django app has already been created with the command

```console
$ python manage.py startapp api
```

## Vue frontend

### Install frontend (JavaScript) dependencies

To install the frontend (JavaScript) dependencies cd into the frontend folder

```console
$ cd frontend
$ npm i
```

(The main frontend dependencies (see package.json) are [vue](https://vuejs.org/guide/introduction.html) and [bootstrap](https://getbootstrap.com/docs/5.0/getting-started/download/).)

and run:

```console
$ npm run dev
```

the server will start on http://localhost:5173
