# 📰 Fake News Detection App | Machine Learning + Streamlit

An interactive Fake News Detection web app that classifies news headlines or articles as **Real** or **Fake** using machine learning — with a **dynamic UI built using Streamlit, enhanced with JavaScript & CSS animations**.

![image](https://github.com/user-attachments/assets/0343d044-f1df-437b-bc62-ff2d2388b638)


---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Web App UI](#web-app-ui)
- [Installation](#installation)
- [Results](#results)
- [Future Scope](#future-scope)
- [Credits](#credits)

---

## 🚀 Overview

Fake news is a widespread problem affecting public opinion and democracy. This project aims to detect fake news using NLP + ML models in Python, with an intuitive Streamlit web app enhanced by JavaScript and CSS effects for better UX.

---

## ✨ Features

✅ Detect whether the input news is real or fake  
✅ Custom JavaScript & CSS animations for headlines, buttons, and alerts  
✅ Clean & responsive Streamlit UI  
✅ Real-time prediction  
✅ Accuracy ~93% (Logistic Regression)  
✅ Supports both title-based and full-text predictions  

---

## 🛠️ Tech Stack

| Component          | Technology Used              |
|--------------------|------------------------------|
| Machine Learning   | Python, scikit-learn          |
| Data Handling      | Pandas, Numpy                 |
| NLP                | NLTK, RegEx, TF-IDF           |
| Web App            | Streamlit                     |
| UI Enhancements    | HTML, CSS, JavaScript (Streamlit components) |

---

## 📂 Dataset

Dataset Source: [Fake and Real News Dataset - Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)  
- `Fake.csv` – Fake news articles  
- `True.csv` – Real news articles  

---

## ⚙️ How It Works

1. Preprocess and clean the text (lowercase, remove stopwords, punctuations)
2. Use TF-IDF vectorizer to convert text to numerical vectors
3. Train Logistic Regression classifier
4. Build interactive UI using Streamlit
5. Inject animations using HTML + JS + CSS inside Streamlit components

---

## 🌐 Web App UI

**Homepage Highlights:**
- Animated headline effect (JavaScript)
- Hover effects on Predict button (CSS)
- Real-time results with color-coded alert banners (e.g., ✅ Real / ❌ Fake)
- Clean layout with expandable "How it Works" section

### 🔥 Sample Animations:
- Typing animation for the title using JS
- Button glow with CSS on hover
- Result banner slide-in effect
  
### Future Scope
- Integrate BERT or Transformer-based models
- Real-time fact-checking via news API
- Browser extension for detecting fake headlines instantly
- Add multilingual support (Hindi, Bengali, etc.)

### 👥 Credits
👤 Rammani Pandey
💻 UI & ML support: ChatGPT
📦 Dataset: Kaggle
