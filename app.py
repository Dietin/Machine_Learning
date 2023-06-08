from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import uvicorn

# load model
model = tf.keras.models.load_model("something3 (1).h5")

# define input schema
class InputData(BaseModel):
    age: int
    weight: float
    height: float
    gender: int
    bmr: float
    activity_level: float

# create FastAPI instance
app = FastAPI()


@app.get('/')
def index():
    return {'message': " Hello, World"}

# define endpoint for prediction
@app.post("/predict")
def predict(data: InputData):
    # convert input data to numpy array
    test = np.array(
        [
           data.age,
           data.weight,
           data.height,
           data.gender,
           data.bmr,
           data.activity_level
        ],
        dtype=float,
    )

    # test = np.expand_dims(test, axis=0)

    # make prediction using the loaded model
    prediction = model.predict(test)

    # return prediction as JSON response
    return {"prediction": float(prediction[0].item())}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=1200)