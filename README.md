# [Project name]
Bubble (Budgeting app)

## Project description

Helps the everyday person keep track of their bills, spendings, and credit

## Author

Cameron Kendrick (GH: Cameron-T-Kendrick)

## Environment setup

Bubble requires Python 3.10 or newer
python --version
python -m venv venv
venv\Scripts\Activate.ps1

## Dependencies

Explain how to install any packages your project needs.

There will be a read me in said repo or website to downlad it, but since this is 
bare bones, we will start through the command promt and work out way up to a application with a GUI.


Give the command to start the program and one example of how to use it.
pip install -r requirements.txt

it should contain stuff like streamlit and a pytest

## Running the tests

Give the command to run the unit tests.

Ill start with streamlit run app.py

(Streamlit opens Bubble in your browser, usually at http://localhost:8501)

and then after youll run the tests to see if it functions.

Here is my discription of what i want in the app:
(I Only used AI to make it look more pretty and not gain the project idea or functions/ libraries I needed)

===========================================================================================================
===========================================================================================================

EXPENSES / BUDGET / CREDIT SCORE APP


Goal: An app that shows where my money is going, with secure data and easy-to-read visuals.



1. SECURITY

- Encrypt all stored information

- Add-on: Secure login with strong password and two-factor authentication

- Add-on: Bank connection through a service like Plaid, so I never store raw card numbers

- Add-on: Auto-logout after inactivity



2. ACCOUNT SETUP

- Add debit and credit card accounts

- Manually enter bills (what they are and when they're due)

- Add-on: Enter income sources (paychecks, side income)



3. TRACKING

- Track where money is being spent

- Record accurate dates for payments and bills

- Detect spending patterns automatically

- Add-on: Reminders before bills are due

- Add-on: Flag duplicate or unusual charges



4. CATEGORIZATION

- Groceries, Wants, Needs, Bills

- Add-on: Custom categories (subscriptions, gas, dining out)

- Add-on: Auto-sorting that learns from my corrections



5. BUDGETING & ALERTS

- Calculate total monthly bills and find patterns

- Danger-area warnings when spending nears or passes the budget

- Add-on: Set budget limits per category

- Add-on: Savings goals with progress tracking



6. CREDIT SCORE

- Add-on: Score tracking over time

- Add-on: Tips for improving it (credit utilization, on-time payments)

- Add-on: Utilization tracker per credit card



7. REPORTS & STATEMENTS

- Monthly: income vs. spending, category breakdown, budget vs. actual

- Quarterly: trends, comparison to last quarter, bill changes

- Annual: yearly totals, biggest changes, savings, credit score movement

- Add-on: Export to PDF or CSV

- Add-on: Automatic generation with a notification when ready



8. VISUALS & DESIGN

- User-friendly and easy to read

- Interactive pie/donut charts, line and bar graphs, bubble charts

- Add-on: Sunburst or treemap to drill from "Needs" down into rent and utilities

- Add-on: Animated month-by-month spending view

- Add-on: Dark mode and mobile-friendly layout



AIS Recomendations:


Tech stack:

- Streamlit + Plotly to start (fastest way to get interactive charts)

- Move to Dash or Flask later if I outgrow it


Build order:

1. Charts with sample data

2. Manual entry (transactions, bills, categories)

3. Budgets and danger alerts

4. Reports and exports (monthly first, then quarterly and annual)

5. Login and encryption

6. Bank connection (Plaid)

7. Credit score features






