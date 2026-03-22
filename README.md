# 🔍 URLiar — URL Lie Detector

> *"Is That URL a Liar? We'll Find Out."*

A machine learning–powered phishing website detection system built as a Final Year Project by students of **United College of Engineering and Research, Prayagraj**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-Academic-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Pages & Routes](#-pages--routes)
- [Contributors](#-contributors)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)

---

## 🛡️ About the Project

**URLiar** is a real-time phishing URL detection web application. Users paste any suspicious URL and the system analyzes its structure using a trained Machine Learning model to classify it as **Safe** or **Phishing** — instantly.

Phishing attacks are one of the most common forms of cybercrime. Attackers create fake websites that impersonate trusted brands like banks, payment platforms, and social media to steal credentials and financial data. URLiar helps everyday users identify these threats before it's too late.

This project was developed as a **Final Year B.Tech Computer Science** project at **United College of Engineering and Research, Prayagraj (2025)**.

---

## ✨ Features

- 🔍 **Real-time URL scanning** — paste any URL and get an instant result
- 🤖 **ML-powered detection** — Logistic Regression model trained on 550,000+ URLs
- ⚠️ **Phishing alert popup** — full-screen warning when a phishing site is detected
- 📊 **Live stats counter** — tracks total scans, phishing detected, and safe URLs
- 🌙 **Dark mode** — toggle between light and dark themes
- 📩 **Contact support** — built-in support form for bug reports and feedback
- 📰 **Newsletter subscription** — users can subscribe for updates
- 📋 **Legal pages** — Terms of Service, Privacy Policy, Cookie Settings
- 👥 **About page** — meet the team behind the project
- 📱 **Fully responsive** — works on desktop and mobile

---

## 🎬 Demo

```
1. Run Flask app       →   python app.py
2. Open browser        →   http://localhost:10000
3. Paste any URL       →   e.g. http://paypal-login-secure.tk
4. Click Scan Now      →   Get instant result ✅ or ⚠️
```

**Test URLs:**

| URL | Expected Result |
|-----|----------------|
| `https://google.com` | ✅ Safe |
| `https://github.com` | ✅ Safe |
| `http://paypal-secure-login.tk/verify` | ⚠️ Phishing |
| `http://amazon-prize-winner.xyz/claim` | ⚠️ Phishing |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **ML Model** | Scikit-learn, Logistic Regression |
| **Vectorizer** | TF-IDF (Character N-grams) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Styling** | Tailwind CSS, Bootstrap 5 |
| **Fonts** | Plus Jakarta Sans, DM Mono (Google Fonts) |
| **Dataset** | Kaggle — Phishing Site URLs (~550K URLs) |
| **Deployment** | Render / Any Python host |

---

## 📁 Project Structure

```
urliar/
│
├── app.py                  # Flask backend — routes & ML inference
├── vectorizer.pkl          # Trained TF-IDF vectorizer
├── phishing.pkl            # Trained Logistic Regression model
├── subscribers.txt         # Newsletter email storage
├── train_model.py          # Script to retrain the model (optional)
│
├── static/
│   ├── rkml.jpg            # Rishi Kant profile photo
│   └── robo.jpg            # Riya Yadav profile photo
│
└── templates/
    ├── index.html          # Main page — URL scanner + stats
    ├── about.html          # About the team & project
    ├── contact.html        # Contact/support form
    ├── footer.html         # Shared footer (Jinja include)
    ├── terms.html          # Terms of Service
    ├── privacy.html        # Privacy Policy
    └── cookies.html        # Cookie Settings
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/rishi-002/urliar.git
cd urliar
```

**2. Install dependencies**
```bash
pip install flask scikit-learn pandas
```

**3. Add your trained model files**

Make sure these two files are in the root directory:
```
vectorizer.pkl
phishing.pkl
```

> If you don't have them yet, see [Training the Model](#-how-it-works) below.

**4. Add profile photos to static folder**
```
static/rkml.jpg     ← Rishi's photo
static/robo.jpg     ← Riya's photo
```

**5. Run the app**
```bash
python app.py
```

**6. Open in browser**
```
http://localhost:10000
```

---

## ⚙️ How It Works

```
User submits URL
      ↓
URL is cleaned (strip https://, www.)
      ↓
TF-IDF Vectorizer converts URL to feature vector
      ↓
Logistic Regression model predicts: 'good' or 'bad'
      ↓
Result displayed: ✅ Safe  or  ⚠️ Phishing
```

### Training the Model (Optional)

If you want to retrain the model yourself:

**1. Download the dataset from Kaggle:**
```
https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls
```

**2. Rename the CSV file:**
```
phishing_site_urls.csv
```

**3. Run the training script:**
```bash
python train_model.py
```

This generates `vectorizer.pkl` and `phishing.pkl` in the current directory.

---

## 📊 Dataset

| Property | Details |
|----------|---------|
| **Source** | [Kaggle — Phishing Site URLs](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls) |
| **Total URLs** | ~549,346 |
| **Good URLs** | ~345,738 (63%) |
| **Bad URLs** | ~203,608 (37%) |
| **Labels** | `good` / `bad` |

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | ~97% |
| **Vectorizer** | TF-IDF Character N-grams (3–5) |
| **Model** | Logistic Regression |
| **Max Features** | 75,000 |
| **Train/Test Split** | 80% / 20% |

---

## 🗺️ Pages & Routes

| Route | Page | Description |
|-------|------|-------------|
| `GET /` | Home | URL scanner + live stats |
| `POST /` | Home | Scans submitted URL |
| `GET /about` | About | Team & project info |
| `GET /contact` | Contact | Support form |
| `POST /contact` | Contact | Submits support request |
| `GET /terms` | Terms | Terms of Service |
| `GET /privacy` | Privacy | Privacy Policy |
| `GET /cookies` | Cookies | Cookie Settings |
| `GET /stats` | API | Returns live JSON stats |
| `POST /subscribe` | API | Newsletter subscription |

---

## 👥 Contributors

<table>
  <tr>
    <td align="center">
      <b>Rishi Kant</b><br>
      <sub>ML Engineer & Full Stack Developer</sub><br>
      <a href="https://www.linkedin.com/in/rishi-kant-433b35287">LinkedIn</a> ·
      <a href="https://x.com/_rishi02">Twitter</a> ·
      <a href="https://github.com/rishi-002">GitHub</a>
    </td>
    <td align="center">
      <b>Riya Yadav</b><br>
      <sub>Frontend Developer & UI Designer</sub><br>
      <a href="#">LinkedIn</a>
    </td>
  </tr>
</table>

**Institution:** United College of Engineering and Research, Prayagraj
**Degree:** B.Tech — Computer Science & Engineering
**Batch:** 2025

---

## 🙏 Acknowledgements

- [Kaggle — Tarun Tiwari](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls) for the phishing URL dataset
- [Scikit-learn](https://scikit-learn.org/) for the ML framework
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) & [Tailwind CSS](https://tailwindcss.com/) for UI components
- [Google Fonts](https://fonts.google.com/) for typography

---

## 📄 License

This project is developed for **academic purposes only** as part of a Final Year B.Tech project at United College of Engineering and Research, Prayagraj.

Not intended for commercial use. All rights reserved © 2025 Rishi Kant & Riya Yadav.

---

<div align="center">

**URLiar** — *Because every liar URL deserves to be exposed.* 🔍

Made with ❤️ at UCER, Prayagraj

</div>
