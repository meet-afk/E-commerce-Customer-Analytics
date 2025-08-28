import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import datetime as dt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

st.set_page_config(page_title='Data Analysis', layout='wide')

st.title("📊 Data Analysis")

df = pd.read_csv(r"C:/Users/gurme/Desktop/Codes/Python/e-com_project/cleaned_e-comm.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

if df is not None:
    # --- Sidebar Filters ---
    st.sidebar.header("Filters")
    selected_country = st.sidebar.selectbox(
        "Select Country",
        options=['All'] + sorted(df['Country'].unique().tolist())
    )

    # Filter data based on selection
    if selected_country != 'All':
        filtered_df = df[df['Country'] == selected_country].copy()
    else:
        filtered_df = df.copy()

    st.header(f"Displaying Data for: {selected_country}")

    # --- Sales Over Time ---
    st.subheader("Sales Trend Over Time")
    filtered_df['YearMonth'] = filtered_df['InvoiceDate'].dt.to_period('M').astype(str)
    monthly_sales = filtered_df.groupby('YearMonth')['Sales'].sum().reset_index()
    fig_sales_time = px.line(monthly_sales, x='YearMonth', y='Sales', title='Monthly Sales Revenue', markers=True)
    fig_sales_time.update_layout(xaxis_title='Month', yaxis_title='Total Sales')
    st.plotly_chart(fig_sales_time, use_container_width=True)

    # --- Top Products and Customers ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 10 Best-Selling Products")
        top_products = filtered_df.groupby('Description')['Quantity'].sum().nlargest(10).reset_index()
        fig_top_products = px.bar(top_products, x='Quantity', y='Description', orientation='h', title='Top 10 Products by Quantity Sold')
        fig_top_products.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_top_products, use_container_width=True)

    with col2:
        st.subheader("Top 10 Customers by Sales")
        top_customers = filtered_df.groupby('CustomerID')['Sales'].sum().nlargest(10).reset_index()
        top_customers['CustomerID'] = top_customers['CustomerID'].astype(str)
        fig_top_customers = px.bar(top_customers, y='Sales', x='CustomerID', orientation='v', title='Top 10 Customers by Total Sales')
        fig_top_customers.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_top_customers, use_container_width=True)


    # --- Sales by Country ---
    st.subheader("Sales Distribution by Country")
    country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False).reset_index()
    fig_country_sales = px.choropleth(country_sales,
                                      locations="Country",
                                      locationmode='country names',
                                      color="Sales",
                                      hover_name="Country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Total Sales by Country")
    st.plotly_chart(fig_country_sales, use_container_width=True)

else:
    st.warning("Please go to the main page to load the data first.")

st.title("🧩 K-Means Customer Segmentation")

if df is not None:
    # --- Prepare Data for Clustering ---
    # Create a customer-level dataset
    customer_df = df.groupby('CustomerID').agg(
        total_sales=('Sales', 'sum'),
        order_count=('InvoiceNo', 'nunique'),
        total_quantity=('Quantity', 'sum')
    ).reset_index()

    # Impute missing values if any (though cleaned data shouldn't have them)
    imputer = SimpleImputer(strategy='mean')
    customer_df_imputed = imputer.fit_transform(customer_df.drop('CustomerID', axis=1))

    # Scale the data
    scaler = StandardScaler()
    customer_df_scaled = scaler.fit_transform(customer_df_imputed)

    # --- Sidebar for K-Means ---
    st.sidebar.header("K-Means Controls")
    n_clusters = st.sidebar.slider("Select number of clusters (k)", 2, 10, 4)

    # --- Perform K-Means Clustering ---
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42, n_init=10)
    customer_df['Cluster'] = kmeans.fit_predict(customer_df_scaled)
    customer_df['Cluster'] = customer_df['Cluster'].astype('category')

    st.success(f"Successfully segmented customers into {n_clusters} clusters.")

    # --- Visualize Clusters ---
    st.subheader("Customer Segments Visualization")
    fig_clusters = px.scatter(
        customer_df,
        x='total_sales',
        y='order_count',
        color='Cluster',
        hover_data=['CustomerID', 'total_quantity'],
        title=f'Customer Segments (k={n_clusters})'
    )
    fig_clusters.update_layout(
        xaxis_title='Total Sales',
        yaxis_title='Number of Orders'
    )
    st.plotly_chart(fig_clusters, use_container_width=True)

    # --- Cluster Profiles ---
    st.subheader("Cluster Profiles")
    cluster_summary = customer_df.groupby('Cluster').agg({
        'total_sales': ['mean', 'min', 'max'],
        'order_count': ['mean', 'min', 'max'],
        'CustomerID': 'count'
    }).reset_index()
    cluster_summary.columns = ['Cluster', 'Mean Sales', 'Min Sales', 'Max Sales', 'Mean Orders', 'Min Orders', 'Max Orders', 'Number of Customers']
    st.dataframe(cluster_summary)

else:
    st.warning("Please go to the main page to load the data first.")
