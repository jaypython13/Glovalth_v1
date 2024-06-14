import streamlit as st
import pandas as pd

def calculate_difference(df, employee_name):
    employee = df[df['Employee_number'] == employee_number]
    current_month_net_pay = employee['Net Pay March'].iloc[0]
    previous_month_net_pay = employee['Net Pay Feb'].iloc[0]
    difference = current_month_net_pay - previous_month_net_pay
    return difference

def suggest_reason(difference):
    if difference > 0.01:
        return "The increase in net pay may be due to a raise, overtime pay, or a bonus."
    elif difference < 0.05:
        return "The decrease in net pay may be due to a deduction, such as taxes or insurance."
    else:
        return "The net pay has not changed."

def main():
    st.title("Net Pay Difference Finder")

    df = pd.read_csv('netpaydata.csv')
    employee_number = st.text_input("Enter the employee number")

    if st.button("Calculate Difference"):
        difference = calculate_difference(df, employee_number)
        reason = suggest_reason(difference)
        st.write("The net pay difference is", difference)
        st.write("Reason:", reason)

if __name__ == '__main__':
    main()

