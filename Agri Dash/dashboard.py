import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Loading DataFrame
df = pd.read_csv('Agriculture-survey-from-2008-to-2021.csv')

# Set the title of your dashboard
st.title("Crop Sales Analysis Dashboard")

# Add a sidebar for user input
st.sidebar.header("User Selection")
selected_chart = st.sidebar.selectbox("Select a Chart", ["Correlation Heatmap", "Line Chart", "Percentage Increase: Selected Crops"])

# Define crops globally
crops = df['H06'].unique()

# Add charts based on user input
if selected_chart == "Correlation Heatmap":
    # Correlation Heatmap
    st.header("Correlation Heatmap")
    correlation_data = df[['Y2008', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2019', 'Y2020', 'Y2021']]
    correlation_matrix = correlation_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    cax = ax.matshow(correlation_matrix, cmap='coolwarm')
    plt.xticks(range(correlation_matrix.shape[1]), correlation_matrix.columns, fontsize=10, rotation=45)
    plt.yticks(range(correlation_matrix.shape[1]), correlation_matrix.columns, fontsize=10)
    plt.title("Correlation Heatmap")
    fig.colorbar(cax, shrink=0.8, aspect=5)
    st.pyplot(fig)

elif selected_chart == "Line Chart":
    # Line Chart
    st.header("Line Chart")
    selected_crops = st.multiselect("Select Items for Comparison", crops)

    # Plot the selected crop sales over the years
    fig, ax = plt.subplots(figsize=(12, 6))

    for selected_crop in selected_crops:
        selected_crop_sales = df[df['H06'] == selected_crop].iloc[0, 9:]
        ax.plot(df.columns[9:], selected_crop_sales, marker='o', linestyle='-', label=f"{selected_crop} Sales")

    plt.title("Crop Sales Comparison Over The Years")
    plt.xlabel('Year')
    plt.ylabel('Sales (R\'000)')
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)

# ... (your existing code above)

elif selected_chart == "Percentage Increase: Selected Crops":
    # Percentage Increase Bar Chart
    st.header("Percentage Increase: Selected Crops")
    selected_crops = st.multiselect("Select Crops for Comparison", crops)

    # Calculate percentage increase for selected crops
    fig, ax = plt.subplots(figsize=(12, 6))

    for selected_crop in selected_crops:
        selected_crop_sales = df[df['H06'] == selected_crop].iloc[0, 9:]
        percentage_increase = selected_crop_sales.pct_change() * 100  # Calculate percentage change
        ax.bar(df.columns[10:], percentage_increase[1:], label=f"{selected_crop} % Increase")

    plt.title("Percentage Increase Over The Years")
    plt.xlabel('Year')
    plt.ylabel('Percentage Increase')
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)
