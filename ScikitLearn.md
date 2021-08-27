# Scikit Learn
It's a ML library for Python which contains algorithms for supervised/unsupervised learning 
and data processing. An overview of algorithm cas be described as follows:
- **Supervised regression:** Linear Regression, Regression Tree, Random Forest + more
- **Supervised classification:** Logistic Regression, Classification Tree, Random Forest + more
- **Unsupervised clustering:** k-means, hierarchical clustering + more
- **Unsupervised dimensionality reduction:** PCA + more
- **Data preprocessing:** Feature selection (which are important), feature scaling, one hot encoding (take values into numerical)+ more
- **Model Refinement:** Validation splitting, parameter tuning, model selection

## BareBone
 ```Python
 # Importing model type, techniques and evaluation metrics
 from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import r2_score
 
 data_for_model = pd.read_cv("data_for_model.csv")
 
 X = data_for_model[["input_var1","input_var2", "input_var3"]]
 y = data_for_model["output_var"]
 
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
 
 regressor = LinearRegression()
 
 regressor.fit(X_train, y_train) #train the regressor on the training data only
 
 y_pred = regressor.predict(X_test) # use the model to predict values
 
 print(r2_score(y_test, y_pred))
 ```
More about [Scikit Learn](https://scikit-learn.org/stable/user_guide.html)
