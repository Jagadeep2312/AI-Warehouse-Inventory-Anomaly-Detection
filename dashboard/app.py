import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import time

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Smart Warehouse Dashboard",
    page_icon="📦",
    layout="wide"
)

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("📦 AI-Based Smart Warehouse Inventory Dashboard")

st.markdown("""
Real-Time Inventory Monitoring using
**Machine Learning + SQLite + Streamlit**
""")

# -------------------------------------------------------
# DATABASE CONNECTION
# -------------------------------------------------------

@st.cache_data(ttl=5)
def load_data():

    conn = sqlite3.connect("database/warehouse.db")

    df = pd.read_sql(
        "SELECT * FROM Inventory",
        conn
    )

    conn.close()

    return df

df = load_data()

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("Dashboard Controls")

warehouse = st.sidebar.selectbox(
    "Warehouse Location",
    ["All"] + sorted(df["Warehouse_Location"].unique().tolist())
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

supplier = st.sidebar.selectbox(
    "Supplier",
    ["All"] + sorted(df["Supplier"].unique().tolist())
)

# -------------------------------------------------------
# FILTERS
# -------------------------------------------------------

filtered_df = df.copy()

if warehouse != "All":
    filtered_df = filtered_df[
        filtered_df["Warehouse_Location"] == warehouse
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

if supplier != "All":
    filtered_df = filtered_df[
        filtered_df["Supplier"] == supplier
    ]

# -------------------------------------------------------
# KPI CALCULATIONS
# -------------------------------------------------------

total_products = len(filtered_df)

missing = len(
    filtered_df[
        filtered_df["Inventory_Status"] == "Missing Inventory"
    ]
)

overstock = len(
    filtered_df[
        filtered_df["Inventory_Status"] == "Overstock"
    ]
)

anomalies = len(
    filtered_df[
        filtered_df["AI_Prediction"] == "Anomaly"
    ]
)

health_score = (
    (total_products - anomalies)
    / total_products
) * 100 if total_products > 0 else 0

risk_score = (
    (missing + overstock)
    / total_products
) * 100 if total_products > 0 else 0

# -------------------------------------------------------
# KPI DISPLAY
# -------------------------------------------------------

st.subheader("📊 Warehouse Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Products",
        total_products
    )

    st.metric(
        "Warehouse Health",
        f"{health_score:.2f}%"
    )

with col2:

    st.metric(
        "Missing Inventory",
        missing
    )

    st.metric(
        "Inventory Risk",
        f"{risk_score:.2f}%"
    )

with col3:

    st.metric(
        "Overstock",
        overstock
    )

    st.metric(
        "AI Anomalies",
        anomalies
    )

st.divider()

# -------------------------------------------------------
# INVENTORY STATUS & AI PREDICTION
# -------------------------------------------------------

st.subheader("📈 Inventory Analytics")

col1, col2 = st.columns(2)

with col1:

    inventory_count = (
        filtered_df["Inventory_Status"]
        .value_counts()
        .reset_index()
    )

    inventory_count.columns = [
        "Inventory Status",
        "Count"
    ]

    fig1 = px.pie(
        inventory_count,
        names="Inventory Status",
        values="Count",
        title="Inventory Status Distribution",
        hole=0.4
    )

    st.plotly_chart(
        fig1,
        width="stretch"
    )

with col2:

    ai_count = (
        filtered_df["AI_Prediction"]
        .value_counts()
        .reset_index()
    )

    ai_count.columns = [
        "AI Prediction",
        "Count"
    ]

    fig2 = px.pie(
        ai_count,
        names="AI Prediction",
        values="Count",
        title="AI Prediction Results",
        hole=0.4
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

# -------------------------------------------------------
# WAREHOUSE DISTRIBUTION
# -------------------------------------------------------

st.subheader("🏢 Warehouse Distribution")

warehouse_count = (
    filtered_df.groupby(
        "Warehouse_Location"
    )
    .size()
    .reset_index(name="Products")
)

fig3 = px.bar(

    warehouse_count,

    x="Warehouse_Location",

    y="Products",

    text="Products",

    title="Products Stored in Each Warehouse"

)

st.plotly_chart(
    fig3,
    width="stretch"
)

# -------------------------------------------------------
# MOVEMENT RATE HISTOGRAM
# -------------------------------------------------------

st.subheader("📦 Inventory Movement Rate")

fig4 = px.histogram(

    filtered_df,

    x="Movement_Rate",

    nbins=25,

    title="Distribution of Product Movement Rate"

)

st.plotly_chart(
    fig4,
    width="stretch"
)

# -------------------------------------------------------
# CATEGORY ANALYSIS
# -------------------------------------------------------

st.subheader("📂 Product Categories")

category_df = (

    filtered_df.groupby("Category")

    .size()

    .reset_index(name="Products")

)

fig5 = px.bar(

    category_df,

    x="Category",

    y="Products",

    text="Products",

    title="Products by Category"

)

st.plotly_chart(
    fig5,
    width="stretch"
)

# -------------------------------------------------------
# SUPPLIER ANALYSIS
# -------------------------------------------------------

st.subheader("🚚 Supplier Analysis")

supplier_df = (

    filtered_df.groupby("Supplier")

    .size()

    .reset_index(name="Products")

)

fig6 = px.bar(

    supplier_df,

    x="Supplier",

    y="Products",

    text="Products",

    title="Products by Supplier"

)

st.plotly_chart(
    fig6,
    width="stretch"
)

# -------------------------------------------------------
# TOP MOVING PRODUCTS
# -------------------------------------------------------

st.subheader("🔥 Top Moving Products")

top_products = (

    filtered_df.groupby(

        "Product_Name"

    )["Movement_Rate"]

    .mean()

    .reset_index()

    .sort_values(

        by="Movement_Rate",

        ascending=False

    )

    .head(10)

)

fig7 = px.bar(

    top_products,

    x="Product_Name",

    y="Movement_Rate",

    text="Movement_Rate",

    title="Top 10 Fast Moving Products"

)

st.plotly_chart(
    fig7,
    width="stretch"
)

st.divider()

# -------------------------------------------------------
# WAREHOUSE HEALTH PANEL
# -------------------------------------------------------

st.subheader("🏥 Warehouse Health Analysis")

col1, col2 = st.columns(2)

with col1:

    st.progress(int(health_score))

    st.success(
        f"Warehouse Health Score : {health_score:.2f}%"
    )

with col2:

    st.progress(int(100-risk_score))

    st.warning(
        f"Inventory Risk Score : {risk_score:.2f}%"
    )

st.divider()

# -------------------------------------------------------
# LIVE AI ALERTS
# -------------------------------------------------------

st.subheader("🚨 AI Live Alerts")

alerts = filtered_df[
    filtered_df["AI_Prediction"] == "Anomaly"
]

if len(alerts) == 0:

    st.success("✅ No AI anomalies detected.")

else:

    st.error(
        f"⚠ {len(alerts)} anomalies detected!"
    )

    st.dataframe(
        alerts.tail(10),
        width="stretch"
    )

st.divider()

# -------------------------------------------------------
# LOW STOCK PRODUCTS
# -------------------------------------------------------

st.subheader("📦 Low Stock Products")

low_stock = filtered_df[
    filtered_df["Current_Stock"] < 20
]

if len(low_stock) == 0:

    st.success("No low-stock products.")

else:

    st.dataframe(
        low_stock[
            [
                "Product_Name",
                "Current_Stock",
                "Warehouse_Location",
                "Supplier"
            ]
        ],
        width="stretch"
    )

st.divider()

# -------------------------------------------------------
# AI RECOMMENDATIONS
# -------------------------------------------------------

st.subheader("🤖 AI Recommendations")

if len(low_stock) == 0:

    st.success("Inventory levels are healthy.")

else:

    for _, row in low_stock.head(10).iterrows():

        st.warning(
            f"""
📦 **{row['Product_Name']}**

Current Stock : **{row['Current_Stock']}**

Location : **{row['Warehouse_Location']}**

Recommendation :
Increase stock immediately.
"""
        )

st.divider()

# -------------------------------------------------------
# INVENTORY STATUS SUMMARY
# -------------------------------------------------------

st.subheader("📋 Inventory Status Summary")

summary = pd.DataFrame({

    "Metric":[
        "Total Products",
        "Missing Inventory",
        "Overstock",
        "AI Anomalies",
        "Warehouse Health",
        "Risk Score"
    ],

    "Value":[
        total_products,
        missing,
        overstock,
        anomalies,
        f"{health_score:.2f} %",
        f"{risk_score:.2f} %"
    ]

})

st.table(summary)

st.divider()

# -------------------------------------------------------
# CRITICAL INVENTORY
# -------------------------------------------------------

st.subheader("⚠ Critical Inventory Records")

critical = filtered_df[
    filtered_df["Inventory_Status"] != "Normal"
]

st.dataframe(

    critical.tail(20),

    width="stretch"

)

st.divider()

# -------------------------------------------------------
# ANOMALY COUNTER
# -------------------------------------------------------

st.subheader("📊 AI Prediction Count")

prediction_count = (

    filtered_df["AI_Prediction"]

    .value_counts()

    .reset_index()

)

prediction_count.columns = [

    "Prediction",

    "Count"

]

fig8 = px.bar(

    prediction_count,

    x="Prediction",

    y="Count",

    text="Count",

    title="AI Prediction Count"

)

st.plotly_chart(

    fig8,

    width="stretch"

)

st.divider()

# -------------------------------------------------------
# SEARCH PRODUCT
# -------------------------------------------------------

st.subheader("🔍 Search Product")

search = st.text_input(
    "Enter Product Name"
)

if search:

    result = filtered_df[
        filtered_df["Product_Name"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        result,
        width="stretch"
    )

st.divider()

# -------------------------------------------------------
# DOWNLOAD CSV
# -------------------------------------------------------

st.subheader("⬇ Download Inventory Report")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    label="Download CSV",

    data=csv,

    file_name="warehouse_inventory_report.csv",

    mime="text/csv"

)

st.divider()

# -------------------------------------------------------
# RECENT INVENTORY
# -------------------------------------------------------

st.subheader("🕒 Latest Inventory Transactions")

st.dataframe(

    filtered_df.tail(20),

    width="stretch"

)

st.divider()

# -------------------------------------------------------
# LAST DATABASE UPDATE
# -------------------------------------------------------

latest_time = filtered_df["Date"].max()

st.info(
    f"📅 Latest Database Update : {latest_time}"
)

st.divider()

# -------------------------------------------------------
# AUTO REFRESH
# -------------------------------------------------------

refresh = st.sidebar.checkbox(
    "Enable Auto Refresh"
)

if refresh:

    refresh_rate = st.sidebar.slider(

        "Refresh Every (Seconds)",

        5,

        60,

        10

    )
from streamlit_autorefresh import st_autorefresh

refresh = st.sidebar.checkbox("Enable Auto Refresh")

if refresh:
    interval = st.sidebar.slider(
        "Refresh Every (Seconds)",
        5,
        60,
        10
    )

    st_autorefresh(
        interval=interval * 1000,
        key="warehouse_refresh"
    )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown("---")

st.markdown(
"""
### ✅ System Status

🟢 Database Connected

🟢 AI Model Loaded

🟢 Warehouse Monitoring Active

🟢 Inventory Simulator Running

🟢 Dashboard Online
"""
)

st.success(
    "AI-Based Smart Warehouse Inventory Anomaly Detection System"
)

st.caption(
"""
Developed using

• Python

• Streamlit

• SQLite

• Plotly

• Scikit-Learn

• Machine Learning

Industry 4.0 Smart Warehouse Prototype
"""
)