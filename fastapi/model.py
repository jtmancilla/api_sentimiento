import dill
import numpy as np
from pysentimiento.preprocessing import preprocess_tweet



## Carga de Modelos entrenados
    # es_nlp_model = joblib.load("utils/es_nlp1.pkl")
    # Load the saved model from the file
with open("utils/es_nlp1.pkl", "rb") as f:
        es_nlp_model = dill.load(f)

# sentiment_analyzer_model = joblib.load("utils/sentiment_analyzer.pkl")
with open("utils/sentiment_analyzer.pkl", "rb") as f:
        sentiment_analyzer_model = dill.load(f)


# emotion_analyzer_model = joblib.load('utils/emotion_analyzer.pkl')
with open("utils/emotion_analyzer.pkl", "rb") as f:
        emotion_analyzer_model = dill.load(f)

# hate_speech_analyzer_model = joblib.load('utils/hate_speech_analyzer.pkl')
with open("utils/hate_speech_analyzer.pkl", "rb") as f:
        hate_speech_analyzer_model = dill.load(f)


def analize1(text1):
    
    result = {}
    initial_text = text1
    text = preprocess_tweet(initial_text)
    es_doc = es_nlp_model(text)

    # Process each sentence in the input text
    for idx, sentence in enumerate(es_doc.sentences):
        sentence_dict = {}
        sentence_dict['text'] = sentence.text
        sentence_dict['sentiment'] = {k: round(v, 3) for k, v in sentiment_analyzer_model.predict(sentence.text).probas.items()}
        sentence_dict['emotion'] = {k: round(v, 3) for k, v in emotion_analyzer_model.predict(sentence.text).probas.items()}
        sentence_dict['hate'] = {k: round(v, 3) for k, v in hate_speech_analyzer_model.predict(sentence.text).probas.items()}
        result[idx] = sentence_dict
  

    return result
