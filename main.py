from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import mysql.connector
import uvicorn

#Define model
class UserInfo(BaseModel):
    user_id: int
    age: int
    weight: float
    height: float
    gender: int
    bmr: float
    activity_level: float

#Buat Koneksi ke database mysql
def db_connection():
    conn = mysql.connector.connect(
        host='23.236.58.16',
        user='root',
        password='development21',
        database='Backend_Dietin'
    )
    return conn

#Load Model H5
def load_model():
    model = tf.keras.models.load_model('Model/model_1_linear.h5')
    return model

app = FastAPI()

#Endpoint
@app.get("/")
def index():
    return "Hello world from ML endpoint!"

@app.post("/predict")
def predict_calories(user_info: UserInfo):
    #periksa apakah field kosong
    if None in user_info.dict().value():
        raise HTTPException(status_code=400, detail="mohon isi")
    
    try:
        #connect database
        conn = db_connection()
        cursor = conn.cursor()

        #Ambil data pengguna dari database
        query = "SELECT * From dataUser WHERE user_id = %s"
        cursor.execute(query, (UserInfo.user_id))
        result = cursor.fetchcone()

        if result is None:
            raise HTTPException(status_code=404, detail="Pengguna dengan ID tersebut tidak ditemukan.")
        
        # Ambil informasi pengguna dari hasil query
        _, age, weight, height, gender, bmr, activity_level = result

        #predict
        model = load_model()
        input_data = [[age, weight, height, gender, bmr, activity_level]]
        predicted_calories = model.predict(input_data)[0]

        #Save data
        update_query = "UPDATE dataUser SET idealCalories = %s WHERE id_user = %s"
        cursor.execute(update_query, (predicted_calories, user_info.id_user))
        conn.commit()

        #close db
        cursor.close()
        conn.close()

        return {"predicted_calories": predicted_calories}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Terjadi kesalahan dalam melakukan prediksi kalori.")
        
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

