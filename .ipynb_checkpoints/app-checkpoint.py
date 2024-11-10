{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "915ed6c5-ae84-4c01-9fc9-64276b74c61e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import pickle\n",
    "import pandas as pd\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "import re\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the trained model and vectorizer\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))\n",
    "\n",
    "# Text preprocessing function\n",
    "def wordopt(text):\n",
    "    # Lowercase and clean text\n",
    "    text = text.lower()\n",
    "    text = re.sub(r'https?://\\S+|www\\.\\S+', '', text)\n",
    "    text = re.sub(r'<.*?>', '', text)\n",
    "    text = re.sub(r'[^\\w\\s]', '', text)\n",
    "    text = re.sub(r'\\d', '', text)\n",
    "    text = re.sub(r'\\n', ' ', text)\n",
    "    return text\n",
    "\n",
    "# Classification function\n",
    "def classify_news(text):\n",
    "    processed_text = wordopt(text)\n",
    "    # Transform the processed text using the loaded vectorizer\n",
    "    vectorized_text = vectorizer.transform([processed_text])\n",
    "    prediction = model.predict(vectorized_text)\n",
    "    return \"Fake News\" if prediction[0] == 1 else \"Real News\"\n",
    "\n",
    "# Home route to render HTML template\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "# Predict route to handle form submission and display result\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    if request.method == 'POST':\n",
    "        news_article = request.form['news_article']\n",
    "        prediction = classify_news(news_article)\n",
    "        return render_template('index.html', prediction=prediction)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b82df4d4-45e6-4ae8-b19a-08f3c56d222d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
