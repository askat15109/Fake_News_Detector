from flask import Flask, request, render_template
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model and vectorizer
svm_model = joblib.load('svm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the news text from the form
        news_text = request.form['news_text']

        # Check if the input is not empty
        if not news_text.strip():
            return render_template('index.html', prediction='Please enter some text to analyze.')

        # Transform the input text using the vectorizer
        news_vector = vectorizer.transform([news_text])

        # Predict using the SVM model
        svm_prediction = svm_model.predict(news_vector)[0]

        # Prepare the result
        result = "Real" if svm_prediction == 1 else "Fake"
        return render_template('index.html', prediction=f'The news is likely: {result}')

if __name__ == '__main__':
    app.run(debug=True)
