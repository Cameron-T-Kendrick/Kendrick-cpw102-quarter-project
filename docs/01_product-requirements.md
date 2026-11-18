# Product Requirements Document
- encrypted the information on said website for secure data
- be able to input Debit and Credit card accounts
- Takes note of where money is going
- Give accurate dates of when payments or bills are made and will see patterns or you can put in when and what your bills are
- Piles it into categories such as groceries, wants, needs, bills
- Calculates monthly bills and find patterns
- Will give me danger areas for set budget and spending
- Be user friendly and easy to read

## Problem

I've seen a lot of young peeps not being able to finance in a healthy way or even older peeps and I think this would help 
be a visual aid in seeing if you are ok

## Desired outcome

Be better at managing there bills, not overspending and seeking more help if they are too far deep

## Scope

The users: Individuals managing their own personal finances. No finance background is needed.

Cases:

- Add accounts and enter bills with due dates.
- Record and categorize spending.
- Check monthly spending against a budget.
- Review monthly, quarterly, and annual summaries.
- Monitor credit health over time.

Hopping to add as fetures:

- Account setup (debit and credit cards)
- Transaction and bill tracking
- Categorization (Groceries, Wants, Needs, Bills)
- Budgeting and danger-area alerts
- Interactive charts and reports
- Security (encryption, login)
- Credit score features, added later


## Out of Scope

- A native, installable phone app (the web app covers mobile through the browser)
- Moving money, paying bills, or making transfers from within the app
- Investment, retirement, or tax-filing tools
- Shared or multi-user household budgets
- Storing raw card numbers (bank connections go through a service like Plaid instead)
- Real bank or credit score data in the early prototype (fake data only until security is in place)

## Requirements



### The product must


- Let users add debit and credit card accounts.
- Let users manually enter bills, including what each one is and when it is due.
- Track spending and record accurate dates for payments and bills.
- Sort transactions into the categories Groceries, Wants, Needs, and Bills.
- Calculate total monthly bills and show spending patterns.
- Warn users (danger-area alerts) when spending nears or passes their budget.
- Show spending in easy-to-read, interactive charts (pie/donut, line, and bar).
- Generate a monthly report: income vs. spending, category breakdown, and budget vs. actual.
- Encrypt all stored information.
- Use fake data only until security is in place, with no real card or bank details in an unsecured prototype.




### The product should

- Provide secure login with a strong password and two-factor authentication.
- Log users out automatically after a period of inactivity.
- Let users enter income sources (paychecks, side income).
- Let users set budget limits per category.
- Send reminders before bills are due.
- Flag duplicate or unusual charges.
- Detect spending patterns automatically.
- Support custom categories (subscriptions, gas, dining out).
- Generate quarterly reports (trends, comparison to last quarter, bill changes) and annual reports (yearly totals, biggest changes, savings, credit score movement).
- Export reports to PDF or CSV.


### The product could

-  Connect to bank accounts through a service like Plaid.
- Auto-sort transactions and learn from the user's corrections.
- Track credit score over time, with tips for improving it and a utilization tracker per credit card.
- Offer savings goals with progress tracking.
- Include sunburst or treemap charts to drill from "Needs" down into rent and utilities, and bubble charts.
- Show an animated month-by-month spending view.
- Offer dark mode and a mobile-friendly layout.
- Generate reports automatically and notify the user when they are ready.

