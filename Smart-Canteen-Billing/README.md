# Smart Canteen Billing and Order Analyzer

## About the Project
Smart Canteen Billing and Order Analyzer is a beginner-friendly Python command-line project. It helps users order food items from a canteen menu, calculate the total bill, apply discounts, and generate a final receipt.

The project uses Python control flow concepts such as conditional statements and loops.

## Features
- Display food menu with prices.
- Select food items using item numbers.
- Enter item quantities.
- Validate item numbers and quantities.
- Calculate individual item costs.
- Add multiple items to one order.
- Apply discounts automatically.
- Calculate subtotal and final bill.
- Generate a final receipt.
- Handle empty orders.

## Menu and Prices

| Item No. | Food Item | Price |
|---|---|---|
| 1 | Veg Sandwich | ₹60 |
| 2 | Masala Dosa | ₹80 |
| 3 | Chole Rice | ₹90 |
| 4 | Paneer Roll | ₹100 |
| 5 | Tea | ₹20 |

## Discount Rules
- ₹500 or more: 10% discount.
- ₹250 to ₹499.99: 5% discount.
- Below ₹250: No discount.

## Technologies Used
- Python
- Command Line Interface (CLI)

## Python Concepts Used
- if statement
- if-else statement
- if-elif-else
- Nested if
- for loop
- while loop
- range()
- break
- continue
- pass
- Nested loops
- Arithmetic operators
- Input and output

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python main.py
```

## Example Output

```text
========== SMART CANTEEN ==========

1. Veg Sandwich - ₹60
2. Masala Dosa - ₹80
3. Chole Rice - ₹90
4. Paneer Roll - ₹100
5. Tea - ₹20

Choose item number: 4
Enter quantity: 2

Added: Paneer Roll x 2 = ₹200.00

Add another item? (y/n): n

========== RECEIPT ==========

Paneer Roll x 2: ₹200.00
Subtotal: ₹200.00
Discount: ₹0.00
Final Total: ₹200.00

Thank you!
```

## Project Purpose
The main purpose of this project is to understand Python control flow concepts and practise decision-making and looping statements through a real-life canteen billing system.

## Author
Md Wajaullah

## Project Level
Beginner to Intermediate – Python Control Flow