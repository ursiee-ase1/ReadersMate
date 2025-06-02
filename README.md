# ReadersMate

ReadersMate is a Django-based web application for tracking books and personal reflections on reading.

## Features

- Add books you are reading
- Log entries about things you relate to in each book
- View and manage your reading log

## Models

- **Title**: Represents a book being read.
- **Entry**: Represents a personal note or reflection related to a book.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ReadersMate.git
   cd ReadersMate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Visit `http://127.0.0.1:8000/` in your browser.
   - Visit `http://127.0.0.1:8000/admin/` for the admin interface.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
