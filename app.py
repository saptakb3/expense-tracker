import streamlit as st
from database import init_db, add_expense, get_expenses
from ai_model import categorize_expense
import pandas as pd

# --- Hardcoded credentials (secure with Streamlit Secrets in production) ---
VALID_USERNAME = "saptak001"
VALID_PASSWORD = "exptracker001"

# --- Login page ---
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password.")

# --- Expense Tracker page ---
def expense_tracker():
    init_db()
    st.title("🧠 AI-Powered Expense Tracker")

    with st.form("expense_form"):
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0)
        description = st.text_input("Description")
        submitted = st.form_submit_button("Add Expense")

        if submitted:
            category = categorize_expense(description)
            add_expense(date.strftime("%Y-%m-%d"), amount, description, category)
            st.success(f"Added {description} under {category}")

    # Fetch and display data
    expenses = get_expenses()
    df = pd.DataFrame(expenses, columns=["ID", "Date", "Amount", "Description", "Category"])
    st.dataframe(df)

    if not df.empty:
        # 📊 Expense by Category
        st.subheader("📊 Expense Summary by Category")
        st.bar_chart(df.groupby("Category")["Amount"].sum())

        # 📈 Expense Over Time
        st.subheader("📈 Expense Trend Over Time")
        df["Date"] = pd.to_datetime(df["Date"])
        daily_totals = df.groupby("Date")["Amount"].sum().reset_index()
        st.line_chart(daily_totals.set_index("Date"))

# --- App flow ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    expense_tracker()
