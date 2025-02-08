https://delhi-house-price-predictor-ifmaadydpsrkbafskjliof.streamlit.app/
---

## 🏠 Delhi House Price Prediction  

### 📌 **Project Overview**  
This project predicts house prices in **Delhi** using **machine learning models**. It includes:  
✅ **Data ingestion & preprocessing**  
✅ **Feature engineering & transformation**  
✅ **Model training & evaluation**  
✅ **REST API using Flask**  
✅ **Frontend with Streamlit**  

---

## 📂 **Project Structure**  
```
Delhi_House_Price_Predictor/
│── artifacts/               # Stores trained models & outputs  
│── logs/                    # Logging outputs  
│── notebook/                # Jupyter notebooks for EDA  
│── src/                     # Source code  
│   ├── components/          # Core ML components  
│   │   ├── data_ingestion.py        # Splits data into train/test  
│   │   ├── data_transformation.py   # Standardizes & encodes data  
│   │   ├── model_trainer.py         # Trains models  
│   ├── pipeline/            # Prediction pipeline  
│   │   ├── predict_pipeline.py           
│   │── exception.py # Cutom Exception Handling
│   │── logger.py #Custom logging program
|   |── utils.py # Helper function
│── app.py                    # Flask API backend  
│── streamlit_app.py           # Streamlit frontend  
│── Dockerfile                 # Docker containerization  
│── docker-compose.yml         # Docker multi-service setup  
│── requirements.txt           # Dependencies  
│── setup.py                   # Package setup  
│── Readme.md                  # Project documentation  
```

---

## 📊 **Dataset**  
- Imported from **Kaggle**  
- Contains **area, location, bedrooms, bathrooms, building type, furnishing status**, etc.  

---

## 🔧 **Implementation Steps**  

### **1️⃣ Data Handling**  
- **Custom Logging & Exception Handling**: Ensures robust error tracking.  
- **Exploratory Data Analysis (EDA)**: Data visualization and feature selection.  
- **Feature Engineering**: Handling missing values, feature scaling, and categorical encoding.  

### **2️⃣ Model Training**  
Implemented in `model_trainer.py`, the models include:  
✔ **Linear Regression**  
✔ **Ridge Regression**  
✔ **Lasso Regression**  
✔ **Decision Tree**  
✔ **Random Forest**  
✔ **XGBoost Regressor**  

### **3️⃣ API Development**  
- **Flask Backend (`app.py`)** serves predictions via a REST API.  

### **4️⃣ Frontend Development**  
- **Streamlit App (`streamlit_app.py`)** provides an interactive UI to input house details and get predictions.  

### **5️⃣ Deployment**  
- **Dockerized the application** (`Dockerfile`, `docker-compose.yml`).  
- **Deployed on Render & Streamlit** for API and UI hosting.  

---

## 🚀 **How to Run the Project Locally**  

### **🔹 Step 1: Clone Repository**  
```bash
git clone https://github.com/MoB-369/Delhi-House-Price-Predictor.git
cd Delhi_House_Price_Predictor
```

### **🔹 Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **🔹 Step 3: Run Flask API**  
```bash
python app.py
```
API will be available at: **http://127.0.0.1:5000**

### **🔹 Step 4: Run Streamlit Frontend**  
```bash
streamlit run streamlit_app.py
```
UI will be available at: **http://localhost:8501**

---

## 🐳 **Run with Docker**  
Build and run the containerized application:  
```bash
docker build -t delhi-house-price-predictor .
docker run -p 5000:5000 -p 5001:5001 delhi-house-price-predictor
```

---

## 🛠️ **Tech Stack Used**  
- **Python** (pandas, NumPy, scikit-learn)  
- **Flask** (for API)  
- **Streamlit** (for UI)  
- **Docker** (for containerization)  
- **Gunicorn** (for production-ready Flask deployment)  

---

## 🤝 **Contributions**  
Feel free to fork, raise issues, or contribute to this project!  

🚀 **Happy Coding!** 😊  

---
