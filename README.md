# Machine_Learning

**Prediksi kalori harian (Linear Regression)**

1. Input data diri sesuai data yang di training (umur, jenis kelamin, berat, tinggi badan, aktivitas)
2. Pilih prioritas => gemukin, standar, kurusin
3. Prediksi kebutuhan kalori berdasarkan prioritas user
    - Misal, jika ingin gemukin, maka input gemukin nya berapa kg, kemudian lakukan prediksi kalori berdasarkan data yang diinputkan + data berat tambahannya
4. Output : jumlah kalori dalam sehari dan kebutuhan kalori per 3 sesi (pagi, siang dan malam) berdasarkan prioritas user
5. Cari rekomendasi resep sesuai selera user

**Pipeline untuk prediksi kalori harian**

1. Cari dataset yang berhubungan dengan kalori
2. Preprocessing dataset
3. Create model
4. Training model
5. Evaluate model
6. Retrain model
7. Deploy model
