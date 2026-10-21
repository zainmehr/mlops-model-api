from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Chargé une seule fois au démarrage du serveur
model = joblib.load("regression.joblib")

# Décrit le JSON attendu dans la requête
class House(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.post("/predict")
def predict(house: House):
    features = [[house.size, house.nb_rooms, house.garden]]
    y_pred = model.predict(features)
    return {"y_pred": float(y_pred[0])}