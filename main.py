from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import tensorflow as tf
import mysql.connector
import numpy as np
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
        host="34.101.233.133",
        user="root",
        password="development21",
        database="Backend_Dietin"
    )
    return conn

# Load model H5
def load_model():
    model = tf.keras.models.load_model('something3 (1).h5')
    return model

app = FastAPI()

# Endpoint untuk mendapatkan data pengguna berdasarkan ID pengguna
@app.get("/predict/{user_id}/{dataUser_id}")
def get_user_info(user_id: int = Path(..., description="ID Pengguna"), dataUser_id: int = Path(..., description="ID Data Pengguna")):
    try:
        # Buat koneksi ke database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Ambil data pengguna dari database
        query = "SELECT age, weight, height, gender, bmr, activity_level FROM dataUser WHERE user_id = %s AND dataUser_id = %s"
        cursor.execute(query, (user_id, dataUser_id))
        result = cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Pengguna dengan ID tersebut tidak ditemukan.")

        # Tutup koneksi ke database
        cursor.close()
        conn.close()

        # Mengembalikan data pengguna
        age, weight, height, gender, bmr, activity_level = result
        return {"age": age, "weight": weight, "height": height, "gender": gender, "bmr": bmr, "activity_level": activity_level}

    except Exception as e:
         raise HTTPException(status_code=500, detail="Terjadi kesalahan dalam mengambil data pengguna.")

# Endpoint untuk melakukan prediksi kalori berdasarkan data pengguna
@app.post("/predict/{user_id}/{dataUser_id}")
def predict_calories(user_info: UserInfo, user_id: int = Path(..., description="ID Pengguna"), dataUser_id: int = Path(..., description="ID Data Pengguna")):
    # Periksa apakah ada field yang kosong
    if None in user_info.dict().values():
        raise HTTPException(status_code=400, detail="Mohon isi semua field terlebih dahulu.")

    try:
        # Buat koneksi ke database
        conn = create_db_connection()
        cursor = conn.cursor()

        # Ambil data pengguna dari database

        print("before")
        query = "SELECT age, weight, height, gender, bmr, activity_level FROM dataUser WHERE user_id = %s AND dataUser_id = %s"
        cursor.execute(query, (user_id, dataUser_id))
        result = cursor.fetchone()
        

        if result is None:
            raise HTTPException(status_code=404, detail="Pengguna dengan ID tersebut tidak ditemukan.")

        # Ambil informasi pengguna dari hasil query
        age, weight, height, gender, bmr, activity_level = result  # Tidak digunakan pada saat prediksi
        print(result)  # Tambahkan baris ini

  
        # Gunakan informasi pengguna untuk memprediksi kalori

        input_data = [age, weight, height, gender, bmr, activity_level]

        model = load_model()

        prediction = model.predict(np.expand_dims(input_data, axis=0))


        predicted_calories = float(prediction[0].item())
        print(predicted_calories)
        try:
            # Simpan hasil prediksi ke dalam tabel user_info
            update_query = "UPDATE dataUser SET idealCalories = %s WHERE user_id = %s AND dataUser_id = %s"
            cursor.execute(update_query, (predicted_calories, user_id, dataUser_id))
            conn.commit()

            # Tutup koneksi ke database
            cursor.close()
            conn.close()
            response = {
                "user_id": user_id,
                "dataUser_id": dataUser_id,
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "bmr": bmr,
                "activity_level": activity_level,
                "predicted_calories": predicted_calories
            }

            return response

        except Exception as e:
            raise HTTPException(status_code=500, detail="Database Connection Tidak Bekerja")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Terjadi kesalahan dalam melakukan prediksi kalori.")

port = 8000

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port)