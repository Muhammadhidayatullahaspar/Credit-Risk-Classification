# Background Project
The background for the Credit Profiling System project is to assist financial institutions such as banks or financing companies in determining the credit risk of their customers. This project is crucial because credit is one of the main sources of income for financial institutions. Before granting credit, financial institutions need to perform credit risk analysis on potential customers.

To perform credit risk analysis, financial institutions must evaluate the financial capability and eligibility of potential customers. To do this, they need accurate and complete data on customers' credit history, income, employment, and assets. This data can be very large and complex, especially if the financial institution has many customers.

Therefore, the use of big data in the Credit Profiling System project can greatly assist financial institutions in determining the credit risk of their customers. However, this big data may have many errors and deficiencies (dirty data) that need to be cleaned and processed before use. In addition, data processing, such as feature engineering and feature scaling, is necessary to improve data quality and increase model accuracy.

After the data is clean and processed, the next step is to perform modeling using machine learning techniques. In this stage, label/target variables and data preprocessing need to be done to prepare the data for machine learning models. The model can then be tested and evaluated by performing exploratory data analysis and visual analysis to determine its performance.

Once the model is successfully created, it can be deployed using Flask on a local host server. This will enable financial institutions to use it in their daily activities and expedite the credit risk analysis process.

![credit risk profilling](https://user-images.githubusercontent.com/100209360/235268497-183874d7-ce87-452d-a4f2-440d443ddca7.png)
# Deployment
# Jika Hasilnya good credit maka akan menghasilkan tampilan berikut
![hasil good](https://user-images.githubusercontent.com/100209360/234748358-f348fadd-6f6b-4d4a-a4a1-e899b19027a8.PNG)

# Jika hasilnya bad credit maka akan menghasilkan tampilan berikut
![hasil bad](https://user-images.githubusercontent.com/100209360/234748665-a9fbc408-01c3-44d4-9d08-2742eac584af.PNG)

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
