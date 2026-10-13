import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load cleaned dataset
df=pd.read_csv("clean_logistics_data.csv")
print("Dataset Shape:", df.shape)

# 2. Define target and features
target = "Days for shipping (real)"

numeric_features = [
    "Days for shipment (scheduled)",
    "Product Price",
    "Order Item Quantity",
    "Order Item Discount"
]

categorical_features = [
    "Shipping Mode",
    "Order Priority",
    "Market",
    "Order Region",
    "Category Name"
]

# Keep only available columns

numeric_features=[c for c in numeric_features if c in df.columns]
categorical_features=[c for c in categorical_features if c in df.columns]

features=numeric_features+categorical_features

# Prepare data

model_df=df[features + [target]].dropna(subset=[target])

X=model_df[features]
y=model_df[target]

#split data 

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

#Preprocessing

#Numerical 
numeric_pipeline=Pipeline([(
    "imputer",SimpleImputer(strategy="median")
)])

categorical_pipeline=Pipeline([(
    "imputer",SimpleImputer(strategy="most_frequent")),
    ("encoder",OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])


model=Pipeline([
    ("preprocessor",preprocessor),
    ("regressor",RandomForestRegressor(
        n_estimators=100,
        max_depth=18,
        min_samples_split=2,
        random_state=42,
        n_jobs=-1
    ))
])



#Training the model

model.fit(X_train,y_train)
print("\nModel Traing Completed")

#making predictions

y_pred=model.predict(X_test)

#evaluating model performance

mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mean_squared_error(y_test,y_pred))
r2=r2_score(y_test,y_pred)

print("\n===== REGRESSION MODEL RESULTS =====")
print(f"MAE: {mae:.3f} days")
print(f"RMSE: {rmse:.3f} days")
print(f"R2 Score: {r2:.3f}")

#compare actual & prediction values

results=pd.DataFrame({
    "Actual_Shipping_Days":y_test,
    "Predicted_Shipping_Days":y_pred
})

print("\n===== ACTUAL VS PREDICTED =====")
print(results.head(10).round(2))

#saving the predictions
results.to_csv("regression_predictions.csv", index=False)

print("\nPredictions saved successfully.")

# ===== FEATURE IMPORTANCE ANALYSIS =====

# Get the trained Random Forest model
rf_model = model.named_steps["regressor"]

# Get the transformed feature names
feature_names = model.named_steps[
    "preprocessor"
].get_feature_names_out()

# Get feature importance values
importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": rf_model.feature_importances_
})

# Display top 10 important features
importance_df = importance_df.sort_values(
    by="Importance", ascending=False
)

print("\n===== TOP 10 IMPORTANT FEATURES =====")
print(importance_df.head(10).round(4).to_string(index=False))

# Save feature importance results
importance_df.to_csv(
    "feature_importance.csv", index=False
)

print("\nFeature importance saved successfully.")