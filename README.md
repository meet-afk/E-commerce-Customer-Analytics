# E-commerce Customer Analytics Dashboard 🛒

This project is an interactive e-commerce customer analytics dashboard built with Streamlit. It transforms a transactional dataset into actionable business insights by analyzing customer behavior.

![Dashboard Screenshot](https://drive.google.com/file/d/18ip6tY9jxF1NLavNlGJOQPS4K384DpfJ/view?usp=drive_link) <!-- Add a screenshot of your app here later! -->

## 📋 About The Project

The dashboard allows users to explore customer data dynamically through several analytical modules:

* **Exploratory Data Analysis (EDA)**: Visualizes key metrics like sales trends over time, top-selling products, and revenue distribution across different countries.
* **K-Means Clustering**: Segments customers into distinct groups based on their purchasing patterns, helping to identify different customer personas.
* **RFM Analysis**: Scores and segments customers based on their **R**ecency, **F**requency, and **M**onetary value to identify high-value customers and those at risk.
* **Customer Lifetime Value (CLTV) Prediction**: Uses statistical models to forecast the future revenue a customer is expected to generate, enabling strategic marketing and retention efforts.

### 🛠️ Built With

This project was built using the following technologies:

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Plotly](https://plotly.com/python/)
* [Scikit-learn](https://scikit-learn.org/)
* [Lifetimes](https://lifetimes.readthedocs.io/en/latest/)

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation

1.  Clone the repo
    ```sh
    git clone [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
    ```
2.  Navigate to the project directory
    ```sh
    cd your_repository_name
    ```
3.  Install the required Python packages
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To run the Streamlit dashboard locally, use the following command in your terminal:

```sh
streamlit run Home.py

