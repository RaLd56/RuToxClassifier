Классификатор токсичных комментариев на русском языке.
Использует лемматизацию, замену латинских символов, TF-IDF и XGBoost с кастомным порогом.
Имеет API-интерфейс на FastAPI.
Установка:
git clone https://github.com/RaLd56/RuToxClassifier.git
cd RuToxClassifier
pip install -r requirements.txt
Пример запроса:
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Это позитивный комментарий"}'
Ответ:
{
  "label": 0
}
