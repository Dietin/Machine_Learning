from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import tensorflow as tf
import mysql.connector
import numpy as np
import os
import uvicorn


# Definisikan model pengguna
class UserInfo(BaseModel):
    age: int
    weight: float
    height: float
    gender: int
    bmr: float
    activity_level: float

# Buat koneksi ke database MySQL
def create_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    return conn

# Load model H5
def load_model():
    model = tf.keras.models.load_model('Model_2_linear.h5')
    return model

app = FastAPI()

@app.get("/dataUser/{user_id}")
def get_user_info(user_id: int = Path(..., description="ID Pengguna")):
    try:
        # Buat koneksi ke database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Ambil data pengguna dari database
        query = "SELECT age, weight, height, gender, bmr, activity_level FROM dataUser WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result is None:
            return {"error": True,
                    "message": "User ID tidak ditemukan"}

        # Tutup koneksi ke database
        cursor.close()
        conn.close()

        # Mengembalikan data pengguna
        age, weight, height, gender, bmr, activity_level = result
        return {
            "error": False,
            "message": "Berhasil mendapatkan data pengguna",
            "data": {
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "bmr": bmr,
                "activity_level": activity_level
            }
        }

    except Exception as e:
        return {
            "error": True,
            "message": "Terjadi kesalahan dalam mengambil data pengguna."
        }

@app.post("/predict/{user_id}")
def predict_calories(user_info: UserInfo, user_id: int = Path(..., description="ID Pengguna")):
    # Periksa apakah ada field yang kosong
    if None in user_info.dict().values():
        return {"error": True, "message": "Data Pengguna belum diisi"}

    try:
        # Buat koneksi ke database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Ambil data pengguna dari database
        query = "SELECT age, weight, height, gender, bmr, activity_level FROM dataUser WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result is None:
            return {"error": True, "message": "User ID tidak ditemukan"}

        # Tutup koneksi ke database
        cursor.close()
        conn.close()

        # Ambil informasi pengguna dari hasil query
        age, weight, height, gender, bmr, activity_level = result

        height_in_m = height / 100.0

        # Gunakan informasi pengguna untuk memprediksi kalori
        input_data = [age, weight, height_in_m, gender, bmr, activity_level]

        model = load_model()
        prediction = model.predict(np.expand_dims(input_data, axis=0))
        predicted_calories = float(prediction[0].item())

        try:
            # Simpan hasil prediksi ke dalam tabel dataUser
            conn = create_db_connection()
            cursor = conn.cursor()

            update_query = "UPDATE dataUser SET idealCalories = %s WHERE user_id = %s"
            cursor.execute(update_query, (predicted_calories, user_id))
            conn.commit()

            # Tutup koneksi ke database
            cursor.close()
            conn.close()

            # Check predicted calories and update response message accordingly
            if predicted_calories < 0:
                message = "Kalori yang diprediksi berlebihan"
            elif predicted_calories > 0:
                message = "Kalori yang diprediksi kurang"
            else:
                message = "Kalori yang diprediksi tepat"

            response = {
                "error": False,
                "message": "Prediksi Kalori Berhasil",
                "data": {
                    "user_id": user_id,
                    "age": age,
                    "weight": weight,
                    "height": height,
                    "gender": gender,
                    "bmr": bmr,
                    "activity_level": activity_level,
                    "predicted_calories": predicted_calories,
                    "message": message
                }
            }

            return response

        except Exception as e:
            raise HTTPException(status_code=500, detail="Database Connection Tidak Bekerja")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Terjadi kesalahan dalam melakukan prediksi kalori.")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
