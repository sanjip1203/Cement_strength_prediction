# 🧱 Concrete Compressive Strength Prediction



A machine learning project aimed at predicting the compressive strength of cement based on its ingredients and composition using various regression techniques.



---


## 📌 Problem Statement

Predict the **compressive strength of concrete** based on its ingredients and curing age using machine learning and cloud deployment.

---

## 📊 Dataset Overview

| Feature                          | Type    | Unit  | Description              |
| -------------------------------- | ------- | ----- | ------------------------ |
| Cement (component 1)             | Numeric | kg/m³ | Cement content           |
| Blast Furnace Slag (component 2) | Numeric | kg/m³ | Slag content             |
| Fly Ash (component 3)            | Numeric | kg/m³ | Fly ash content          |
| Water (component 4)              | Numeric | kg/m³ | Water content            |
| Superplasticizer (component 5)   | Numeric | kg/m³ | Additive content         |
| Coarse Aggregate (component 6)   | Numeric | kg/m³ | Coarse aggregate         |
| Fine Aggregate (component 7)     | Numeric | kg/m³ | Fine aggregate           |
| Age                              | Numeric | Days  | Age of concrete          |
| **Compressive Strength**         | Target  | MPa   | Strength to be predicted |

---

## 🏗️ Project Architecture

```
Start
│
├── 📥 Data (Batches) for Training
│   └── ✅ Data Validation
│       ├── 🔍 File Name / Column / Data Type Check
│       └── ❌ Null Columns Removal
│
├── 📂 Good Data → "Good_Data_Folder"
├── 🚫 Bad Data → "Bad_Data_Folder"
│
├── 🗃️ Insert Good Data into Database
├── 📤 Export DB Data to CSV for Training
│
├── 🧹 Data Preprocessing
│   ├── 🤖 KNN Imputation
│   ├── 🔁 Log Transformation
│   └── 📏 Feature Scaling
│
├── 🔀 Data Clustering (KMeans + KneeLocator)
│
├── 🧠 Model Training (for each cluster)
│   ├── 🤖 Linear Regression
│   └── 🌲 Random Forest
│       └── 🛠️ GridSearchCV for tuning
│
├── 💾 Save Best Model (per cluster)
├── ☁️ Cloud Setup & Deployment (🚀 PWS)
├── 🖥️ Application Start
│
├── 🔮 Client Prediction Flow
│   ├── 📥 Input CSV → Validation → DB Insert
│   ├── 📤 Export DB to CSV
│   ├── 🧹 Preprocessing
│   ├── 🔀 Cluster Prediction
│   ├── 📈 Predict using cluster-specific model
│   └── 📦 Export Predictions to CSV
│
END
```

---

## 📁 Project Structure

```

```

---

## 🔄 Workflow Summary

1. **📥 Upload Batch Data**
2. **✅ Schema Validation**
3. **🗃️ Store Valid Data in SQLite DB**
4. **📤 Export → 🧹 Preprocess → 🔀 Cluster**
5. **🧠 Train Models**
6. **☁️ Deploy to Cloud**
7. **🌐 Receive New Client Data → Predict Cluster → Predict Output**
8. **📦 Return Results as CSV**

---

## 🛠️ Tech Stack

* 🐍 Python (pandas, NumPy, scikit-learn)
* 🧠 Machine Learning (KMeans, RandomForest, LinearRegression)
* 📦 SQLite3 Database
* 🌐 Django and Django Rest framework (for deployment)
* ☁️ Cloud: **Pivotal Web Services (PWS)**
* 🔍 GridSearchCV (for hyperparameter tuning)

---

## 🚀 Deployment

* 🐳 Optional: Docker support
* ☁️ Deployed via **Pivotal Web Services**
* 🔗 API Endpoint: `/predict`
* 📄 Input: CSV | 📊 Output: CSV with Predictions

---

## ✅ Output

Final CSV contains:

* Original input features
* Cluster label
* 🔮 Predicted **Compressive Strength (MPa)**

---

