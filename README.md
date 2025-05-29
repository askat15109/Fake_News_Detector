# 📰 Fake News Detector

A machine learning-based web app that detects fake news using Natural Language Processing (NLP) and a trained Support Vector Machine (SVM) model. It allows users to input news text and returns whether the content is likely **Real** or **Fake**.
![Fake News Detector Screenshot](assets/demo.png)

---

## 🗂️ Project Structure

```
fake-news-detector/
├── templates/           # HTML templates (Flask frontend)
│   └── index.html
├── app.py               # Main Flask application
├── svm_model.pkl        # Trained SVM classification model
├── vectorizer.pkl       # Fitted TF-IDF vectorizer
├── requirements.txt     # Required Python packages
└── README.md
```

---

## 🚀 Features

- ✅ Detects fake news using machine learning
- 🧠 SVM model trained on labeled news dataset
- ✍️ Accepts user input text for analysis
- 🖥️ Simple and intuitive web interface (Flask)
- 📊 Displays results with classification output

---

## 🛠️ Tech Stack

- **Frontend**: HTML (Jinja2 via Flask)
- **Backend**: Python, Flask
- **ML/NLP**: 
  - `scikit-learn` (SVM Classifier, TF-IDF Vectorizer)
  - `nltk` for text preprocessing
- **Model Files**: `svm_model.pkl`, `vectorizer.pkl`

---

## 🧪 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask App**

```bash
python app.py
```

4. **Access the App**

Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📚 Dataset Used

- [Fake and Real News Dataset – Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

---

## 🧠 Model Training (Optional)

To train your own model:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news_texts)

# Model Training
model = LinearSVC()
model.fit(X, labels)

# Save Model and Vectorizer
joblib.dump(model, 'svm_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
```

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Akshat Choubey**  
📫 Email: [akshatchoubey2@gmail.com]  
🔗 GitHub: [@yourusername](https://github.com/askat15109)
