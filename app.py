import streamlit as st
import math

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Calculator")

# Sidebar for calculator mode
mode = st.sidebar.selectbox(
    "Choose Calculator Mode",
    ["Basic", "Scientific", "Financial", "Unit Conversion"]
)

if mode == "Basic":
    st.header("Basic Calculator")
    num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter second number:", value=0.0, step=1.0)
    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Division by zero not allowed!")

elif mode == "Scientific":
    st.header("Scientific Calculator")
    num = st.number_input("Enter number:", value=0.0, step=1.0)
    operation = st.selectbox(
        "Operation", 
        ["Square", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]
    )
    if st.button("Calculate"):
        if operation == "Square":
            st.success(f"Result: {num**2}")
        elif operation == "Square Root":
            st.success(f"Result: {math.sqrt(num)}")
        elif operation == "Logarithm":
            if num > 0:
                st.success(f"Result: {math.log(num)}")
            else:
                st.error("Logarithm not defined for non-positive values!")
        elif operation == "Sine":
            st.success(f"Result: {math.sin(math.radians(num))}")
        elif operation == "Cosine":
            st.success(f"Result: {math.cos(math.radians(num))}")
        elif operation == "Tangent":
            st.success(f"Result: {math.tan(math.radians(num))}")

elif mode == "Financial":
    st.header("Financial Calculator")
    principal = st.number_input("Principal Amount:", value=1000.0, step=100.0)
    rate = st.number_input("Annual Interest Rate (%):", value=5.0, step=0.1)
    time = st.number_input("Time (years):", value=1.0, step=1.0)
    calc_type = st.radio("Choose Calculation:", ["Simple Interest", "Compound Interest"])
    
    if st.button("Calculate"):
        if calc_type == "Simple Interest":
            si = (principal * rate * time) / 100
            st.success(f"Simple Interest: {si}")
        else:
            ci = principal * ((1 + rate/100)**time - 1)
            st.success(f"Compound Interest: {ci}")

elif mode == "Unit Conversion":
    st.header("Unit Conversion")
    conversion = st.selectbox("Choose Conversion", ["Meters to Kilometers", "Kilograms to Grams", "Celsius to Fahrenheit"])
    value = st.number_input("Enter value:", value=0.0, step=1.0)
    
    if st.button("Convert"):
        if conversion == "Meters to Kilometers":
            st.success(f"{value} m = {value/1000} km")
        elif conversion == "Kilograms to Grams":
            st.success(f"{value} kg = {value*1000} g")
        elif conversion == "Celsius to Fahrenheit":
            st.success(f"{value} °C = {(value*9/5)+32} °F")
