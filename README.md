
# LAB_APPS_VIEWS: CarsRental Django Project 🚗

This project is a simple Django web application created as part of a lab exercise.  
It demonstrates basic **Django views**, **URL routing**, and **template rendering**.

---

## 📌 Project Description

The project includes a single Django app that handles different routes:

- Home page: When requesting `http://127.0.0.1:8000/`, it should return the phrase:`Hello World, This is my new HOME for Car Rentals Website! we're excited to welcome you here.`
- About page : when requesting `http://127.0.0.1:8000/about/`, it should return:  `A simple paragraph about Car Rentals. `
- Password generator (Bonus task): When requesting `http://127.0.0.1:8000/password/generate/`, it should return a randomly generated password of length 10 characters (letters, upper, lower, symbols) - `Example output: e$dkjf@mA2`

---

## Project Structure

```
CarsRental/
│
├── CarsRental/              # Main project folder
│
├── main/                    # Django app
│   │
│   ├── templates/
│   │   └── main/
│   │       ├── home.html
│   │       ├── about.html
│   │       └── generate_password.html
│   │
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── manage.py
```
---

## Key Learning Outcomes
- Creating Django projects and apps
- Running and stopping the server
- Understanding the MVT (Model-View-Template) architecture
- Handling URLs and views
- Using templates for rendering HTML pages

