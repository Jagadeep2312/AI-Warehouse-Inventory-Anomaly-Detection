📦 AI-Based Smart Warehouse Inventory Anomaly Detection System
Project Title

AI-Based Smart Warehouse Inventory Anomaly Detection System Using Machine Learning

Problem Statement

Warehouses often face inventory-related challenges that directly affect operational efficiency and profitability.

Some of the major problems include:

Inventory mismatches between expected and actual stock.
Missing or misplaced products inside the warehouse.
Overstocking due to poor inventory monitoring.
Manual inventory auditing is slow, expensive, and prone to human error.
Lack of real-time visibility into inventory movement.
Difficulty identifying abnormal inventory behavior before it impacts operations.

Traditional warehouse management systems rely heavily on manual monitoring and periodic audits, making it difficult to detect anomalies in real time.

Proposed Solution

This project introduces an AI-powered Smart Warehouse Inventory Anomaly Detection System that continuously monitors inventory movement using Machine Learning.

The system automatically:

Monitors stock movement.
Calculates inventory differences.
Detects missing inventory.
Detects overstock conditions.
Identifies unusual inventory behavior.
Predicts anomalies using Isolation Forest.
Generates AI recommendations.
Displays real-time warehouse analytics on a Streamlit dashboard.

The prototype simulates a real Industry 4.0 warehouse environment where inventory updates are continuously monitored and analyzed.

Technologies Used
Technology	Purpose
Python	Programming Language
Pandas	Data Processing
NumPy	Numerical Computation
Scikit-Learn	Machine Learning (Isolation Forest)
SQLite	Inventory Database
Streamlit	Interactive Dashboard
Plotly	Data Visualization
Pickle	Saving Trained AI Model
VS Code	Development Environment
Git & GitHub	Version Control
Machine Learning Model

Algorithm Used

Isolation Forest

Reason:

Works well for anomaly detection
Learns normal inventory behaviour
Detects abnormal inventory patterns automatically
Suitable for real-time warehouse monitoring
Project Architecture
                         Warehouse

                              │

                              ▼

                  Inventory Transactions

                              │

                              ▼

                  Data Preprocessing

                              │

                              ▼

               Feature Engineering

                              │

                              ▼

          Isolation Forest AI Model

                              │

                              ▼

             Inventory Prediction

                              │

                              ▼

                SQLite Database

                              │

                              ▼

         Live Inventory Simulator

                              │

                              ▼

          Streamlit Dashboard

                              │

                              ▼

      Warehouse Manager / Admin
Project Workflow
Dataset Creation

↓

Data Cleaning

↓

Feature Engineering

↓

Machine Learning Model

↓

Prediction

↓

SQLite Database

↓

Inventory Simulator

↓

Live Dashboard

↓

AI Alerts

↓

Inventory Recommendation
Dashboard Features

The dashboard provides the following features:

📊 KPI Cards
Total Products
Missing Inventory
Overstock
AI Anomalies
Warehouse Health Score
Inventory Risk Score
📈 Data Visualization
Inventory Status Pie Chart
AI Prediction Pie Chart
Warehouse Distribution Chart
Product Movement Histogram
Supplier Analysis
Category Analysis
Top Moving Products
🤖 AI Features
AI Anomaly Detection
Low Stock Detection
Inventory Risk Analysis
Warehouse Health Analysis
AI Recommendations
Live Alert Panel
📋 Inventory Monitoring
Latest Inventory Transactions
Product Search
Download CSV Report
Auto Refresh
Real-Time Monitoring
Project Folder Structure
AI_Warehouse_Project

│
├── dashboard
│      └── app.py
│
├── data
│      ├── inventory.csv
│      ├── inventory_clean.csv
│      └── inventory_predictions.csv
│
├── database
│      └── warehouse.db
│
├── models
│      └── anomaly_model.pkl
│
├── scripts
│      ├── create_dataset.py
│      ├── preprocess.py
│      ├── train_model.py
│      ├── database_setup.py
│      ├── inventory_simulator.py
│      └── check_database.py
│
├── screenshots
│
├── requirements.txt
│
└── README.md
Screenshots

Add screenshots after running the dashboard.

Suggested screenshots:

Screenshot 1

Dashboard Home

screenshots/dashboard_home.png
Screenshot 2

Warehouse KPI Cards

screenshots/kpi_cards.png
Screenshot 3

Inventory Status Chart

screenshots/inventory_chart.png
Screenshot 4

AI Prediction Chart

screenshots/ai_prediction.png
Screenshot 5

AI Alerts

screenshots/alerts.png
Screenshot 6

Latest Inventory Table

screenshots/latest_inventory.png
How to Run the Project
Step 1

Clone Repository

git clone https://github.com/YourUsername/AI_Warehouse_Project.git
Step 2

Open Project

cd AI_Warehouse_Project
Step 3

Create Virtual Environment

python -m venv .venv
Step 4

Activate Virtual Environment

Windows

.venv\Scripts\activate
Step 5

Install Requirements

pip install -r requirements.txt
Step 6

Generate Dataset

python scripts/create_dataset.py
Step 7

Preprocess Dataset

python scripts/preprocess.py
Step 8

Train AI Model

python scripts/train_model.py
Step 9

Create Database

python scripts/database_setup.py
Step 10

Start Live Inventory Simulator

python scripts/inventory_simulator.py
Step 11

Open Dashboard

streamlit run dashboard/app.py
Future Scope

This prototype can be enhanced further by integrating real warehouse hardware and cloud technologies.

Possible future improvements include:

RFID Integration
Barcode Scanner Integration
IoT-Based Smart Shelves
Raspberry Pi Gateway
Cloud Database (MySQL/PostgreSQL)
Email Alert System
SMS Notifications
WhatsApp Notifications
Predictive Inventory Forecasting
Deep Learning-Based Demand Prediction
Warehouse Heat Maps
Mobile Application
CCTV-Based Inventory Detection using YOLO
SAP ERP Integration
AWS/Azure Cloud Deployment
Benefits
Reduces inventory loss.
Detects anomalies automatically.
Improves stock accuracy.
Saves manual audit time.
Supports Industry 4.0 warehouse automation.
Provides real-time inventory visibility.
Enables proactive inventory management.
Helps warehouse managers make informed decisions.
Industry Applications

This project can be implemented in:

Warehouses
Logistics Centers
E-Commerce Fulfillment Centers
Retail Chains
Manufacturing Industries
Pharmaceutical Warehouses
Food Distribution Centers
Supply Chain Management Companies
Author

Gunde Jagadeep

B.Tech Artificial Intelligence & Data Science

St. Joseph's College of Engineering, Chennai

License

This project is developed for educational and research purposes as an Industry 4.0 AI Warehouse Inventory Anomaly Detection System Prototype.
