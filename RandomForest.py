#%%
#Importing required python packages
from sklearn.linear_model import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
print("libraries imported")
#%%
# import dataset
my_data = pd.read_cv("video_game_data.csv")
 
X = data_for_model[["input_var1","input_var2", "input_var3"]]
y = data_for_model["output_var"]
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
 
regressor = LinearRegression()
 
regressor.fit(X_train, y_train) #train the regressor on the training data only
 
y_pred = regressor.predict(X_test) # use the model to predict values
 
print(r2_score(y_test, y_pred))