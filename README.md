# Expense Tracker

A simple command-line expense tracking application built with Python. It allows users to record, manage, search, and analyze their expenses while storing data locally in JSON files.

## Features

- **Add Expenses:** Record expenses with a name, amount, and category.
- **Manage Expenses:** Edit expense names, amounts, and categories, or delete existing expenses.
- **View All Expenses:** Display all recorded expenses.
- **Calculate Total Expenses:** Calculate the total amount of all expenses.
- **Search by Category:** Display expenses belonging to a specific category.
- **Calculate Expenses by Category:** Calculate the total amount spent in a selected category.
- **Calculate Average Expenses:** Calculate the average expense amount.
- **Identify Highest Expense:** Find the most expensive recorded transaction.
- **Identify Lowest Expense:** Find the least expensive recorded transaction.
- **Custom Currency:** Set and save your preferred currency.
- **Data Persistence:** Store expenses and currency settings locally using JSON files.
- **Input Validation:** Handle invalid inputs and validate expense information.

## Technologies Used

- Python 3
- JSON
- Built-in Python modules:
  - `json`
  - `os`
  - `math`

## Project Structure

```text
expenses_tracker/
│
├── ExpensesCalculator.py
├── expenses.json
├── settings.json
├── README.md
├── .gitignore
└── LICENSE
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MohamedKhaledGitSeries/expenses_tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd expenses_tracker
```

### 3. Run the Application

```bash
python ExpensesCalculator.py
```

No external Python packages are required.

## Data Storage

The application uses JSON files to store information locally.

**expenses.json**

Stores expense records using the following structure:

```json
[
    {
        "name": "Groceries",
        "amount": 45.50,
        "category": "Food"
    },
    {
        "name": "Bus Ticket",
        "amount": 2.00,
        "category": "Transportation"
    }
]
```

**settings.json**

Stores the selected currency:

```json
{
    "currency": "USD"
}
```

## Main Menu

The application provides the following options:

1. Add an Expense
2. Manage Expenses
3. Show All Expenses
4. Calculate Total Expenses
5. Show Expenses by Category
6. Calculate Expenses by Category
7. Calculate Average Expenses
8. Show Highest Expense
9. Show Lowest Expense
10. Exit

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Mohamed Khaled Boulksibat**

GitHub: [@MohamedKhaledGitSeries](https://github.com/MohamedKhaledGitSeries)

---

*This project was developed as part of my journey in learning Python programming and building practical software applications.*