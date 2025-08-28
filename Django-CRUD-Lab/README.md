# Django CRUD App Lab (FBV)

## Introduction

In this lab, your challenge is to create a complete full-stack application using **Django**, **PostgreSQL**, and **HTML templates**. Your application will center around **one resource of your choosing**, for which you’ll implement full **Create, Read, Update, and Delete (CRUD)** functionality using **function-based views (FBV)**.

> Choose something you enjoy — e.g., Blogs, Cars, Shoes, Saudi Desserts, Dogs, Food, Planets, Quotes.

---

## Select your resource

Pick a real-world entity and define the fields you’ll need (e.g., `name`, `description`, `price_cents`, `is_active`, `created_at`). Keep the **model name singular** (e.g., `Plant`) and the **table/listing plural** (e.g., “plants”).

---

## Minimum Viable Product (MVP)

Build an app that lets users:

1. **Create** new items via a form.
2. **Read**: view a list of items and a detail page.
3. **Update**: edit an existing item via a form.
4. **Delete**: remove an item with confirmation.

Test each step as you go. Focus on correctness first; you can polish UI later.

---

## Getting Started

### 1) Create & activate a virtual environment

* Create a project folder and open it in your terminal.
* Create and activate a **virtualenv**.

---

### 2) Install dependencies

Install Django and PostgreSQL driver:

```
pip install Django psycopg2-binary
```

> You will freeze dependencies at the end.

---

### 3) Start a Django project & app

* Start a project (replace `myproject` with your name).
* Start an app (replace `catalog` with your resource’s app name).

```
django-admin startproject myproject .
python manage.py startapp catalog
```

* Add the app to `INSTALLED_APPS` in `myproject/settings.py`.

---

### 4) Configure PostgreSQL

* Create a PostgreSQL database  (in pgAdmin).
* Load env vars in `settings.py` using `python-dotenv`.
* Configure `DATABASES` for PostgreSQL in `settings.py`.


---

### 5) Define your model (schema)

* In `catalog/models.py`, create **one model** for your resource with at least 3 of the following:

  * A required `CharField` (e.g., `name`)
  * A `IntegerField`
  * A `BooleanField`
  * A `created_at = models.DateTimeField(auto_now_add=True)` (recommended)
  * A `DateTimeField`

* Run:

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6) Register model in the admin

* Register your model in `catalog/admin.py`.
* Create a superuser:

```
python manage.py createsuperuser
```

* Log in to `/admin/` and add a few sample records to test.

---

### 7) URLs & project structure

* Create `catalog/urls.py` and wire it in `myproject/urls.py` under a prefix (e.g., `/items/`).
* Use **named URL patterns** that match your views (see REST table below).

> Suggested structure:

```
project-root/
├─ manage.py
├─ .env
├─ myproject/
│  ├─ settings.py
│  ├─ urls.py
├─ catalog/
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/
│  │  └─ catalog/
│  │     ├─ base.html
│  │     ├─ item_list.html
│  │     ├─ item_detail.html
│  │     ├─ item_form.html
└─ venv/
```

---

### 8) Templates

* Create a `templates/catalog/` directory with:

  * `base.html` (MUST have a header block for header info and a content block for the body content)
  * `item_list.html`
  * `item_detail.html`
  * `item_form.html` (used for create & update)

---

### 9) FBV Views (Function-Based Views)

Implement **five views** in `catalog/views.py`:

1. **Index/List** view (shows all items)
2. **Detail** view (shows one item)
3. **New/Create** (GET: form, POST: create)
4. **Edit/Update** (GET: form with instance, POST: save)
5. **Delete/Destroy** (GET: confirm, POST: delete)

> Use Django forms or `ModelForm`. Add success redirects and messages if you like.

---

### 10) RESTful routes (your naming must match)

Your application should expose these routes (adjust `items` to your plural resource name):

| HTTP Method | Route               | Action  | URL Name      | Description                    |
| ----------- | ------------------- | ------- | ------------- | ------------------------------ |
| GET         | /items/             | Index   | `item_list`   | Show list of all items         |
| GET         | /items/new/         | New     | `item_create` | Show form to create a new item |
| POST        | /items/             | Create  | `item_create` | Create a new item              |
| GET         | /items/<id>/        | Show    | `item_detail` | Show one item by ID            |
| GET         | /items/<id>/edit/   | Edit    | `item_update` | Show form to edit an item      |
| POST        | /items/<id>/edit/   | Update  | `item_update` | Update an item                 |
| POST | /items/<id>/delete/ | Destroy | `item_delete` | Delete an item                 |

> Note: Using POST for update/delete is acceptable in classic Django form flows (HTML forms don’t support PUT/DELETE). You may also implement method override if you want.

---

### 11) Tie it all together

* Wire each view into `catalog/urls.py` with the **exact names** above.
* In templates, navigate using `{% url 'item_list' %}`, `{% url 'item_detail' pk=item.pk %}`, etc.
* Add links in `base.html` to the list page and a “New Item” button.

---

### 12) Run & test

```
python manage.py runserver
```

* Visit the list page, create items, view details, edit, and delete.
* Verify that each template loads and redirects correctly.

---

### 13) Freeze dependencies

Create a `requirements.txt`:

```
pip freeze > requirements.txt
```

Ensure it includes at least:

* `Django`
* `psycopg2-binary`

