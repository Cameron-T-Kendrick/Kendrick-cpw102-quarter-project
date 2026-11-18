# Product Requirements Document

    # -Apps information for users-
        Bubble:
            Its a website/App that will be able to help anyone of any ages to easily understand their finaces,
            current spending habits, and see where they stand overall in there goals with money. It will also let the 
            user be able to modify what they want in a secure matter. The website will not hide anything nor hold any important 
            information, track locations, or sell your cookies/privacy to gain finacial gain. It will purely to help those 
            who want a easier way to finace their bills or keep track of their spending habits.
        # -Requirements-
            - encryption of the information on Bubble so have a scure enviorment
            - Have a walk through to help users understand basic finances 
            - Be able to input Debit and Credit banking accounts 
            - Track where money is being spent
            - Give accurate dates of when payments or bills are made
            - Have patterns in where cash is being spent
            - Have a place where you can put in already known bills
            - Piles spending into categories such as groceries, wants, needs, bills
            - Calculates monthly bills, spending, and then make it a quarterly and yearly calculation 
            - Make a setting where the user can delete all information that is after 2 years
            - Will give visual danger areas for set budget and spending
            - Be user friendly and easy to understand for all ages

## Problem

    - I've seen a lot of young people not being able to finance in a healthy way or even older people. I believe this would help be a  visual aid to help not just myself have a easier time tracking my bills, but to help people start to learn financial literancy.

## Desired outcome

    - To be able to understand how finace works at a basic level and then help see how to become stronger financialy. 
    - To teach people baisc in finance and how to budget for their goals.

## Scope

The users: Individuals managing their own personal finances. No finance background is needed.

Cases:

    - Add accounts and enter bills with due dates and or auto pays in place.
    - Record and categorize spending.
    - Check monthly spending against a budget.
    - Review monthly, quarterly, and annual summaries.
    - Monitor credit health over time.

Hopping to add as features:

    - Account setup (debit and credit cards)
    - Transaction and bill tracking
    - Categorization (Groceries, Wants, Needs, Bills)
    - Budgeting and danger-area alerts
    - Interactive charts and reports
    - Security (encryption, login)
    - Credit score features, added later

## Out of Scope

    - A native, installable phone app for IOS/android/Linux (the web app covers mobile through the browser)
    - Only to track where money is going and not to used as a outlet to pay bills
    - Investment, retirement, or tax-filing tools
    - Shared or multi-user household budgets
    - Storing raw card numbers (bank connections go through a service like Plaid instead)
    - Real bank or credit score data in the early prototype (fake data only until security is in place)

## Requirements


### The product must

    - client-side zero-knowledge encryption (The app/web dosent have accsess to your information, just you)
    - Let users add debit and credit card accounts.
    - Let users manually enter bills, including what each one is and when it is due.
    - Track spending and record accurate dates for payments and bills.
    - Sort transactions into the categories Groceries, Wants, Needs, and Bills.
    - Calculate total monthly bills and show spending patterns.
    - Warn users (danger-area alerts) when spending nears or passes their budget.
    - Show spending in easy-to-read, interactive charts (Bubbles in a jar/pie).
    - Generate a monthly report: income vs. spending, category breakdown, and budget vs. actual.
    - Encrypt all stored information (Thinking of useing Bitwardens Library).
    - Use fake data only until security is in place, with no real card or bank details in an unsecured prototype.

### The product should

    - Provide secure login with a strong password and two-factor authentication.
    - Log users out automatically after a period of inactivity.
    - Let users enter income sources (paychecks, side income).
    - Let users set budget limits per category.
    - Send reminders before bills are due (3-5 days in advance since if its a bank withdraw itll take a bit).
    - Flag duplicate or unusual charges.
    - Detect spending patterns automatically. (Will be bigger or smaller bubbles inside said bubble)
    - Support custom categories (subscriptions, gas, dining out).
    - Generate quarterly reports (trends, comparison to last quarter, bill changes) and annual reports (yearly totals, biggest changes, savings, credit score movement).
    - Export reports to PDF or CSV.

### The product could

    - Connect to bank accounts through a service like Plaid.
    - Auto-sort transactions and learn from the user's corrections.
    - Track credit score over time, with tips for improving it and a utilization tracker per credit card. (Will be using the Three Credit buearues)
    - Offer savings goals with progress tracking.
    - Include sunburst or treemap charts to drill from "Needs" down into rent and utilities, and bubble charts.
    - Show an animated month-by-month spending view.
    - Offer dark mode and a mobile-friendly layout.
    - Generate reports automatically and notify the user when they are ready.
    - Have fluid animation for moving bubbles out of their respective area.
