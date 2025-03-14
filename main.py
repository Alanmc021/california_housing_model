from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Carregar o modelo salvo
try:
    model = joblib.load("california_housing_model.pkl")
except Exception as e:
    raise RuntimeError(f"Erro ao carregar o modelo: {e}")

# Criar a aplicação FastAPI
app = FastAPI()

# Definir o modelo de dados de entrada usando Pydantic
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Rota para previsões
@app.post("/predict")
def predict(features: HouseFeatures):
    try:
        # Converter os dados de entrada em um array numpy
        input_data = np.array([
            features.MedInc,
            features.HouseAge,
            features.AveRooms,
            features.AveBedrms,
            features.Population,
            features.AveOccup,
            features.Latitude,
            features.Longitude
        ]).reshape(1, -1)

        # Fazer a previsão
        prediction = model.predict(input_data)

        # Retornar a previsão
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Rodar a API com Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)