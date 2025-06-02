# YOUR SUNSET LIBRARY V1

Your Sunset Library is a Django-based web application for managing and reading digital books online.
Users can:
- browse,
- search, and
- read
PDF books directly in their browser with features like:
- page navigation,
- text selection, and
- responsive design.

## Features

- Upload and manage books (PDF to be enforced in my next version)
- Categorize books by author and category
- Read books online with a PDF.js-powered viewer
- Flip pages, jump to a specific page
<!-- - Select and copy text from books -->
- Responsive design for mobile and desktop
- Simple navigation between book list and detail views

## Requirements

- Python 3.8+ (these basic requirements shoould do)
- Django 3.2+
- pip

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone git@github.com:lawalTheWest/mylib.git
    cd mylib
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python3 manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**
    ```bash
    python3 manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python3 manage.py runserver
    ```

7. **Access the app:**
    - Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Upload Books:** Using the Django admin (v1) to add new books.
- **Browse Books:** The homepage lists all available books.
- **Read Online:** Click on a book to open the detail page and read it online.
- **Navigation:** Use the Previous/Next buttons or jump to a specific page.
<!-- - **Text Selection:** Select and copy text directly from the PDF viewer. -->

## Project Structure

```
mylib/
├── books/                # Django app for book management
│   ├── migrations/
│   ├── templates/books/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── mylib/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── media/                # This hollds the uploaded book files
├── manage.py
└── README.md
```

## Dependencies

- Django
- pdf.js (via CDN for frontend PDF rendering)

## License

This project is for educational purposes.

---

**Enjoy your digital library!**