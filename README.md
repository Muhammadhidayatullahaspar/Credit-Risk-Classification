![credit risk](https://user-images.githubusercontent.com/100209360/234351220-e2ac340e-83f9-48d6-b5d3-7a647f9c66b6.PNG)

# Credit-Risk-Classification
This project developed a classification model to predict loan credit risk. Debt consolidation was the most common loan purpose, with good credit being prevalent. Imbalanced data was addressed using SMOTE oversampling. The model achieved high accuracy and validation scores, with suggestions for variable importance and model evaluation.

# Kesimpulan
Berdasarkan hasil analisis dari project kredit risk untuk klasifikasi credit baik dan buruk, dapat disimpulkan bahwa sebagian besar peminjam memiliki kredit dengan grade yang baik, kepemilikan rumah yang terbanyak adalah 'MORTGAGE', tujuan pinjaman paling banyak adalah untuk debt consolidation, dan sebagian besar peminjam memiliki rasio utang terhadap pendapatan yang rendah. Selain itu, terdapat ketidakseimbangan pada data yang bisa menjadi masalah dalam analisis data, sehingga dilakukan oversampling smote untuk menyeimbangkan data. Model yang telah dibangun memiliki akurasi yang tinggi pada data train dan test, serta validasi yang baik, yaitu kc 0.99, ks 0.93, dan cross validation 0.92. Dengan demikian, model ini dapat digunakan untuk memprediksi kredit baik atau buruk dengan tingkat akurasi yang tinggi.

# Saran 
Beberapa hal lain yang dapat dilakukan untuk project ini:

- Loan amount distribution: Sebaiknya dilakukan analisis lebih lanjut terkait pinjaman dengan jumlah tinggi yang mungkin berpotensi menjadi risiko kredit yang lebih tinggi, seperti dengan melihat rasio utang terhadap pendapatan dan seberapa besar pembayaran bulanan yang harus dilakukan oleh peminjam.

- Distribution credit grade: Analisis ini dapat membantu untuk memahami profil risiko peminjam yang berbeda dan menentukan strategi kredit yang sesuai dengan profil risiko tersebut.

- Distribution of home ownership: Dapat dilakukan analisis lebih lanjut untuk memahami bagaimana kepemilikan rumah dapat mempengaruhi risiko kredit. Hal ini dapat membantu untuk menentukan strategi kredit yang sesuai dengan profil risiko peminjam yang berbeda.

- Loan purpose distribution: Perlu dilakukan pemantauan terhadap pinjaman dengan tujuan 'other', 'major purpose', 'small business', 'car', 'medical', 'moving', 'vacation', 'wedding', 'house', 'educational', dan 'renewable energy' karena memiliki jumlah pinjaman yang lebih sedikit dibandingkan dengan tiga tujuan pinjaman teratas.

- Distribution of dti: Perlu dilakukan analisis lebih lanjut untuk memahami bagaimana rasio utang terhadap pendapatan mempengaruhi risiko kredit dan apakah terdapat rentang nilai DTI tertentu yang memiliki risiko kredit yang lebih tinggi.

- Distribution bad flag: Oversampling SMOTE dapat membantu menyeimbangkan data dan memperbaiki kinerja model dalam memprediksi kasus yang tidak dominan.

- Model evaluation: Perlu dilakukan pengujian model secara berkala untuk memastikan kinerja model yang konsisten dan sesuai dengan tujuan analisis. Selain itu, dapat dilakukan analisis lebih lanjut terkait faktor-faktor yang mempengaruhi kinerja model, seperti pemilihan fitur yang tepat atau penggunaan algoritma yang lebih kompleks untuk meningkatkan akurasi model.
