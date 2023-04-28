# Background Project
The background for the Credit Profiling System project is to assist financial institutions such as banks or financing companies in determining the credit risk of their customers. This project is crucial because credit is one of the main sources of income for financial institutions. Before granting credit, financial institutions need to perform credit risk analysis on potential customers.

To perform credit risk analysis, financial institutions must evaluate the financial capability and eligibility of potential customers. To do this, they need accurate and complete data on customers' credit history, income, employment, and assets. This data can be very large and complex, especially if the financial institution has many customers.

Therefore, the use of big data in the Credit Profiling System project can greatly assist financial institutions in determining the credit risk of their customers. However, this big data may have many errors and deficiencies (dirty data) that need to be cleaned and processed before use. In addition, data processing, such as feature engineering and feature scaling, is necessary to improve data quality and increase model accuracy.

After the data is clean and processed, the next step is to perform modeling using machine learning techniques. In this stage, label/target variables and data preprocessing need to be done to prepare the data for machine learning models. The model can then be tested and evaluated by performing exploratory data analysis and visual analysis to determine its performance.

Once the model is successfully created, it can be deployed using Flask on a local host server. This will enable financial institutions to use it in their daily activities and expedite the credit risk analysis process.

# Deployment
![credit risk profilling](https://user-images.githubusercontent.com/100209360/235268497-183874d7-ce87-452d-a4f2-440d443ddca7.png)

# If the result is good credit it will produce the following display
![hasil good](https://user-images.githubusercontent.com/100209360/234748358-f348fadd-6f6b-4d4a-a4a1-e899b19027a8.PNG)

# If the result is bad credit it will produce the following display
![hasil bad](https://user-images.githubusercontent.com/100209360/234748665-a9fbc408-01c3-44d4-9d08-2742eac584af.PNG)

# Conclusion
Based on the analysis results of the credit risk project for classifying good and bad credit, it can be concluded that most borrowers have good credit grades, the most common home ownership status is 'MORTGAGE', the most common loan purpose is for debt consolidation, and most borrowers have a low debt-to-income ratio. Additionally, there is an imbalance in the data, which can pose a problem in data analysis, so oversampling SMOTE was performed to balance the data. The built model has a high accuracy on both the training and testing data, as well as good validation, with kc 0.95, ks 0.93, and cross-validation of 0.92. Therefore, this model can be used to predict good or bad credit with a high level of accuracy.

# Some other things that can be done for this project include:
Beberapa hal lain yang dapat dilakukan untuk project ini:

- Loan amount distribution: Further analysis should be done regarding high loan amounts, which may pose a higher credit risk, by looking at the debt-to-income ratio and how much monthly payments borrowers have to make.

- Distribution credit grade: This analysis can help understand the different borrower risk profiles and determine appropriate credit strategies for each risk profile.

- Distribution of home ownership: Further analysis can be done to understand how home ownership affects credit risk. This can help determine appropriate credit strategies for different borrower risk profiles.

- Loan purpose distribution: Monitoring is needed for loans with the purpose of 'other', 'major purpose', 'small business', 'car', 'medical', 'moving', 'vacation', 'wedding', 'house', 'educational', and 'renewable energy' because they have fewer loans compared to the top three loan purposes.

- Distribution of dti: Further analysis is needed to understand how the debt-to-income ratio affects credit risk and whether there are specific DTI values that pose a higher credit risk.
- Distribution bad flag: Oversampling SMOTE can help balance data and improve model performance in predicting non-dominant cases.

- Model evaluation: Regular model testing is needed to ensure consistent model performance and alignment with analysis objectives. Additionally, further analysis can be done regarding factors that affect model performance, such as selecting appropriate features or using more complex algorithms to improve model accuracy.
