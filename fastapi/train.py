# Libraries for sentiment analysis.
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import stanza
from pysentimiento import create_analyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stanza.download("es")

from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet

import dill


# NLP model for Spanish (ES): text handling and analyzers
es_nlp = stanza.Pipeline(lang='es')

# Sentiment (positive, negative, neutral)
sentiment_analyzer = create_analyzer(task="sentiment", lang="es")
# Emotions (joy, surprise, disgust, sadness, fear, anger, others)
emotion_analyzer = create_analyzer(task="emotion", lang="es")
# Hate Speech (hateful, targeted, aggressive)
hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")



# Save the trained model as a file using dill
with open("utils/es_nlp1.pkl", "wb") as f:
    dill.dump(es_nlp, f)
# Load the saved model from the file
with open("utils/es_nlp1.pkl", "rb") as f:
    es_nlp_model = dill.load(f)


with open("utils/sentiment_analyzer.pkl", "wb") as f:
    dill.dump(sentiment_analyzer, f)
# Load the saved model from the file
with open("utils/sentiment_analyzer.pkl", "rb") as f:
    sentiment_analyzer_model = dill.load(f)

# Save the trained model as a file using dill
with open("utils/emotion_analyzer.pkl", "wb") as f:
    dill.dump(emotion_analyzer, f)
# Load the saved model from the file
with open("utils/emotion_analyzer.pkl", "rb") as f:
    emotion_analyzer_model = dill.load(f)

# Save the trained model as a file using dill
with open("utils/hate_speech_analyzer.pkl", "wb") as f:
    dill.dump(hate_speech_analyzer, f)
    
# Load the saved model from the file
with open("utils/hate_speech_analyzer.pkl", "rb") as f:
    hate_speech_analyzer_model = dill.load(f)