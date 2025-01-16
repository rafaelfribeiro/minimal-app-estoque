# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using Flask. The application allows users to manage records in a database.

## Project Structure

```
```
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── create.html
│   │   ├── read.html
│   │   └── update.html
│   └── static
│       ├── css
│       │   └── styles.css
│       ├── img
│       │   ├── logo.png
│       │   └── background.jpg
│       └── js
│           └── scripts.js
├── run.py
├── requirements.txt
└── README.md
```

## Features

- Create new records
- Read existing records
- Update existing records
- Delete records

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-crud-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```
The application will be available at `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License.