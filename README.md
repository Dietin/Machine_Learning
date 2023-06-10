
# API Model-Diet!n-Prediction Calories
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_HOST` = "localhost"

`DB_USER` = "user"

`DB_PASSWORD` = "password"

`DB_DATABASE` = "database"



## How to use

install the requirments

```bash
  pip install -r requirments.txt
```

run uvicorn

```bash
  uvicorn main:app 
```



## API-Documentation
- [Get User](#user)
- [Prediction](#prediction)


## API Reference

## User
- Endpoint :
    - /dataUser/{user_id}
- Method :
    - GET {user_id}
- Header :
    - Content-Type: application/json
- Response :
```json 
{
  "error": false,
  "message": "Berhasil mendapatkan data pengguna",
  "data": {
    "age": int,
    "weight": float,
    "height": float,
    "gender": int,
    "bmi": float,
    "bmr": float,
    "activity_level": float,
  }
}
```

## Prediction
- Endpoint :
    - /predict/{user_id}
- Method :
    - POST {user_id}
- Header :
    - Content-Type: application/json

- Body :
```json 
{
  "age": int, required,
  "weight": float, required,
  "height": float, required,
  "gender": int, required,
  "bmi" : float, required,
  "bmr": float, required,
  "activity_level": float, required
}
```
- Response :
```json 
{
  "error": false,
  "message": "Prediksi Kalori Berhasil",
  "data": {
    "user_id": int,
    "age": int,
    "weight": float,
    "height": float,
    "gender": int,
    "bmi": float,
    "bmr": float,
    "activity_level": float,
    "predicted_calories": float,
    "message": "Kalori yang diprediksi kurang" or "Kalori yang diperediksi berlebihan"
  }
}
```


