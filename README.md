

# 🧱 Cement Compressive Strength Prediction

A full-stack machine learning project that predicts the **compressive strength of concrete** based on its composition and curing age. Built using **Python**, **Django**, **Scikit-learn**, and **Matplotlib**.

---



## 📁 Project Structure

<details>
<summary><strong>📂 Data_Preprocessing and hyperparameter tuning</strong></summary>

* [best\_model.pkl](Data_Preprocessing%20and%20hyperparameter%20tuning/best_model.pkl)
* [clean\_data.csv](Data_Preprocessing%20and%20hyperparameter%20tuning/clean_data.csv)
* [data\_preprocessing.ipynb](Data_Preprocessing%20and%20hyperparameter%20tuning/data_preprocessing.ipynb)
* [minmax\_scaler.pkl](Data_Preprocessing%20and%20hyperparameter%20tuning/minmax_scaler.pkl)

</details>

<details>
<summary><strong>📂 EDA</strong></summary>

* [Cement.ipynb](EDA/Cement.ipynb)
* [Concrete\_Data.csv](EDA/Concrete_Data.csv)

</details>

* [README.md](README.md)
* [requirements.txt](requirements.txt)

<details>
<summary><strong>📂 cement_strength</strong></summary>

<details>
<summary><strong>📂 cement_strength (Django Project)</strong></summary>

* [\_\_init\_\_.py](cement_strength/cement_strength/__init__.py)
* [asgi.py](cement_strength/cement_strength/asgi.py)
* [settings.py](cement_strength/cement_strength/settings.py)
* [urls.py](cement_strength/cement_strength/urls.py)
* [wsgi.py](cement_strength/cement_strength/wsgi.py)


</details>

* [db.sqlite3](cement_strength/db.sqlite3)
* [manage.py](cement_strength/manage.py)

<details>
<summary><strong>📂 modelrunner (Django App)</strong></summary>

* [\_\_init\_\_.py](cement_strength/modelrunner/__init__.py)
* [admin.py](cement_strength/modelrunner/admin.py)
* [apps.py](cement_strength/modelrunner/apps.py)
* [models.py](cement_strength/modelrunner/models.py)
* [tests.py](cement_strength/modelrunner/tests.py)
* [urls.py](cement_strength/modelrunner/urls.py)
* [views.py](cement_strength/modelrunner/views.py)




</details>

<details>
<summary>📂 models (saved ML assets)</summary>

* [best\_model.pkl](cement_strength/modelrunner/models/best_model.pkl)
* [minmax\_scaler.pkl](cement_strength/modelrunner/models/minmax_scaler.pkl)

</details>

<details>
<summary>📂 templates</summary>

* [predict.html](cement_strength/modelrunner/templates/predict.html)

</details>

</details>
</details>





## 📊 Dataset Overview

| Feature                          | Type    | Unit  | Description              |
| -------------------------------- | ------- | ----- | ------------------------ |
| Cement                          | Numeric | kg/m³ | Cement content           |
| Blast Furnace Slag              | Numeric | kg/m³ | Slag content             |
| Fly Ash                         | Numeric | kg/m³ | Fly ash content          |
| Water                           | Numeric | kg/m³ | Water content            |
| Superplasticizer                | Numeric | kg/m³ | Additive content         |
| Coarse Aggregate                | Numeric | kg/m³ | Coarse aggregate         |
| Fine Aggregate                  | Numeric | kg/m³ | Fine aggregate           |
| Age                             | Numeric | Days  | Age of concrete          |
| **Compressive Strength**        | Target  | MPa   | Strength to be predicted |

---

### 🔄 End-to-End Machine Learning Workflow

```
📤 Upload CSV Data
   ⬇️
🧪 Validate Schema
   ⬇️
🧹 Preprocess Data (Impute, Scale, Transform)
   ⬇️
📊 Cluster with KMeans
   ⬇️
🤖 Train ML Models per Cluster
   ⬇️
🧠 Save Best Models with GridSearchCV
   ⬇️
🚀 Deploy via Django + PWS
   ⬇️
🌐 User Uploads New Data via Web
   ⬇️
🔎 Predict Cluster → Predict Strength
   ⬇️
📄 Return CSV with Predictions
```

---

## 🧠 ML Pipeline Summary

* ✅ **Data Preprocessing**: KNN Imputation, Log Transform, MinMax Scaling
* 🔁 **Clustering**: KMeans + KneeLocator
* 🤖 **Model Training**: Linear Regression & Random Forest (per cluster)
* 🛠️ **Tuning**: GridSearchCV for best hyperparameters
* 💾 **Model Saving**: `best_model.pkl`, `minmax_scaler.pkl`

---

## 🌐 Web Deployment (Django)

* Django Views render HTML form for input
* CSV Upload triggers:

  1. Preprocessing
  2. Cluster detection
  3. Strength prediction
* Returns **downloadable output CSV**

---

## 🛠️ Tech Stack

* **Python**: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
* **Web Framework**: `Django`, `Django REST framework`
* **Data Handling**: `SQLite3`
* **Cloud Deployment**: Pivotal Web Services (PWS)
* **Visualization**: Jupyter, Seaborn, Matplotlib
* **Others**: `joblib`, `GridSearchCV`, `MinMaxScaler`

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Key packages used:

* Django
* scikit-learn
* matplotlib
* pandas
* seaborn
* ipykernel, jupyter
* django-filter

---

## ✅ Final Output

Final result is a **CSV file** containing:

* Original Input
* Cluster Label
* 🔮 Predicted **Compressive Strength (MPa)**

---

## 📬 API Endpoint

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| POST   | `/predict` | Uploads CSV, returns predictions |

---

## 🙌 Author

**Sandip Man Singh Mahat**\
*Data Science and Backend Enthusiast*

