import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.set_page_config(
    page_title="E-commerce Customer Analytics Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🛒 E-commerce Customer Analytics Dashboard")

df= pd.read_csv(r"C:/Users/gurme/Desktop/Codes/Python/e-com_project/cleaned_e-comm.csv")

if df is not None:
    st.success("Dataset loaded successfully!")

    # --- Display Data Preview ---
    if st.checkbox("Show Raw Data Preview", value=True):
        st.subheader("Raw Data Preview")
        st.dataframe(df.head())

    # --- Key Metrics ---
    st.subheader("High-Level Metrics")
    col1, col2, col3, col4 = st.columns(4)

    total_revenue = df['Sales'].sum()
    total_orders = df['InvoiceNo'].nunique()
    total_customers = df['CustomerID'].nunique()
    total_products = df['StockCode'].nunique()

    with col1:
        st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
    with col2:
        st.metric(label="Total Orders", value=f"{total_orders:,}")
    with col3:
        st.metric(label="Total Unique Customers", value=f"{total_customers:,}")
    with col4:
        st.metric(label="Total Unique Products", value=f"{total_products:,}")

    st.info("Select the 'Analysis' tab from the sidebar for more detailed view")

else:
    st.warning("Data could not be loaded. Please check the file path and integrity.")
