import streamlit as st
from database import init_db, add_expense, get_expenses
from ai_model import categorize_expense
import pandas as pd

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

# Show table
expenses = get_expenses()
df = pd.DataFrame(expenses, columns=["ID", "Date", "Amount", "Description", "Category"])
st.dataframe(df)

# Show summary
if not df.empty:
    st.subheader("📊 Expense Summary")
    st.bar_chart(df.groupby("Category")["Amount"].sum())
