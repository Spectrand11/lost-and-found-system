# Lost and Found System

A command-line Lost and Found management system built with Python. It allows users to record found items, search existing records, update item information, and delete records.

## Features

- **Report Items:** Record found items with their name, description, location, and date found.
- **View Items:** Display all recorded items.
- **Search Items:** Search for items using their name or description.
- **Update Items:** Modify an item's name, description, location, date, or claim status.
- **Delete Items:** Remove records using their unique IDs.
- **Claim Status:** Track whether an item is claimed or unclaimed.
- **Input Validation:** Handle invalid menu choices and other unexpected inputs.

## Project Structure

```text
lost-and-found-system/
├── main.py
├── item.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3

No external packages are required.

## How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd lost-and-found-system
```

Run the application:

```bash
python3 main.py
```

## Storage

Records are stored in memory using a list of dictionaries. Consequently, all recorded data is lost when the application exits.

## Concepts Practised

- Python variables and data types
- Lists and dictionaries
- Loops and conditional statements
- Functions and modular programming
- String manipulation
- Exception handling
- CRUD operations
- Basic input validation

## Limitations

- Data is not persistent between application runs.
- Date inputs are not validated against a specific date format.
- The application is designed for single-user, local terminal use.

## License

This project is open for educational and learning purposes.
```
