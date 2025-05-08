import joblib
from preprocessing import preproc
import pandas as pd

vectorizer = joblib.load('models/vectorizer.pkl')
model = joblib.load('models/xgb_model.pkl')
THRESHOLD = 0.284
text = 'нахуй'
def predict(text):
    processed_text = preproc(text)
    processed_text_pd = pd.array([processed_text])
    text_vec = vectorizer.transform(processed_text_pd)
    prob = model.predict_proba(text_vec)[0][1]
    return int(prob >= THRESHOLD)
print(predict(text))