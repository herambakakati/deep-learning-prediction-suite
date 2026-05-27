# 🚀 Customer Churn Prediction & Accident Detection AI Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep_Learning-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-yellow)
![License](https://img.shields.io/badge/License-Educational-green)

## 📌 Overview

Customer Churn Prediction & Accident Detection AI Platform is a premium AI-powered web application built using Streamlit, Machine Learning, and Deep Learning.

This application combines two intelligent systems in one platform:

- **Customer Churn Prediction** for business analytics
- **Road Accident Detection** using image classification

The project is designed for academic demonstration, portfolio showcase, and real-world AI deployment concepts.

---

## ✨ Features

### Customer Churn Prediction
✔ Predict customer churn risk  
✔ Interactive user input form  
✔ Instant prediction results  
✔ Probability score display  
✔ Business retention insights  

### Accident Detection
✔ Upload accident images  
✔ CNN-based image classification  
✔ Accident / No Accident detection  
✔ Fast inference results  
✔ Real-time extension ready  

### UI Features
✔ Premium responsive Streamlit interface  
✔ Modern dashboard design  
✔ Attractive custom HTML/CSS styling  
✔ Easy navigation between modules  

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### Machine Learning / Deep Learning
- TensorFlow
- Keras
- Scikit-learn
- NumPy
- Pandas

### Visualization
- Matplotlib
- Seaborn

### Image Processing
- OpenCV
- Pillow

---

## 📂 Project Structure

```bash
customer-churn-accident-detection-app/
│
├── app.py
├── home.py
├── churn.py
├── accident.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── churn_model.h5
│   └── accident_model.h5
│
├── assets/
│   ├── banner.jpg
│   ├── logo.png
│   ├── churn_bg.jpg
│   └── accident_samples/
```

---

## ⚙ Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-accident-detection-app.git
```

### 2. Open Project Folder

```bash
cd customer-churn-accident-detection-app
```

### 3. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run Application

```bash
streamlit run app.py
```

Application URL:

```bash
http://localhost:8501
```

---

## 📊 Customer Churn Prediction Module

This module predicts whether a customer is likely to leave the company.

### Input Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

### Output

- Churn Prediction
- Churn Probability
- Risk Category

---

## 🚗 Accident Detection Module

Upload road traffic images for classification.

### Supported Formats

- JPG
- JPEG
- PNG

### Output

- Accident Detected
- No Accident Detected
- Confidence Score

### Future Scope

- Live webcam detection
- CCTV integration
- Smart traffic surveillance
- Emergency alert system

---

## 📦 requirements.txt

Create a file named `requirements.txt` and add:

```txt
streamlit
tensorflow
keras
numpy
pandas
scikit-learn
matplotlib
seaborn
opencv-python
Pillow
```

---

## 📸 Screenshots

Add project screenshots here.

Example:

```markdown
![Home](assets/home.png)
![Churn](assets/churn.png)
![Accident](assets/accident.png)
```

---

## 🚀 Deployment

Deploy on:

- Streamlit Community Cloud
- Render
- Railway
- Hugging Face Spaces

Deployment command:

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Heramba Kakati**

Machine Learning | Deep Learning | Streamlit Projects

---

## 📚 Educational Purpose

This project is developed for:

- Academic assignments
- Portfolio showcase
- AI deployment practice
- Deep learning demonstration

---

## 🔮 Future Improvements

- User login authentication
- Database integration
- Prediction history tracking
- API deployment with FastAPI
- Live video accident detection
- Admin analytics dashboard

---

## License

This project is intended for educational and learning purposes.
