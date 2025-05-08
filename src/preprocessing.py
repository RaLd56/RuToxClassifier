import pymorphy2
import string
import emoji
import pandas as pd

morph = pymorphy2.MorphAnalyzer()
punctuation = string.punctuation

char_map = {
    'a': 'а', 'A': 'А',
    'e': 'е', 'E': 'Е',
    'o': 'о', 'O': 'О',
    'p': 'р', 'P': 'Р',
    'c': 'с', 'C': 'С',
    'y': 'у', 'Y': 'У',
    'x': 'х', 'X': 'Х',
    'B': 'В', 'H': 'Н', 'M': 'М', 'K': 'К',
}

def normalize_chars(text: str) -> str:
    return ''.join([char_map.get(ch, ch) for ch in text])

def lemmatize_text(text: str) -> str:
    return ' '.join([morph.parse(word)[0].normal_form for word in text.split()])

def _preprocess_single(text: str) -> str:
    text = text.lower()
    text = normalize_chars(text)
    text = text.translate(str.maketrans('', '', punctuation))
    text = emoji.replace_emoji(text, replace='')
    text = lemmatize_text(text)
    return text

def preproc(text):
    if isinstance(text, pd.Series):
        return text.apply(_preprocess_single)
    elif isinstance(text, str):
        return _preprocess_single(text)
    else:
        raise ValueError("Expected a string or pandas Series")
