# 🔗 URL Shortener

A simple and user-friendly URL Shortener web application built using **Flask** and **SQLite**. It allows users to convert long URLs into short, shareable links and manage them through a dashboard.

---

## ✨ Features

- 🔗 Shorten long URLs into unique short links
- 🌐 Redirect to the original URL using the short link
- 📊 Dashboard to view all shortened URLs
- 🔍 Search URLs by original URL or short code
- 🗑️ Delete unwanted URLs
- 💾 Stores all URLs using SQLite database
- 🎨 Clean and responsive user interface

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML5
- CSS3
- Git & GitHub

---

## 📂 Project Structure

```
Url_Shortener/
│── app.py
│── database.py
│── models.py
│── requirements.txt
│── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
│
├── instance/
│   └── urls.db
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/purple-del/url-shortener-flask.git
```

### 2. Open the project

```bash
cd url-shortener-flask
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

You can add screenshots of:

- Home Page
- Shortened URL Result
- Dashboard

---

## 📌 Future Improvements

- Track the number of clicks for each shortened URL
- Generate QR codes for shortened URLs
- User authentication
- URL expiration feature
- Custom short URLs
- Analytics dashboard

---

## 👩‍💻 Author

**Pirkhan Ayesha Abdul Vahid**

- GitHub: https://github.com/purple-del
- LinkedIn: https://www.linkedin.com/in/aayesha-pirkhan-6b49b2369

