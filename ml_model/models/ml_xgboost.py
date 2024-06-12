import os
import xgboost as xgb
import dask.dataframe as dd
from dask_ml.model_selection import train_test_split
from dask.distributed import Client
# from constants import *
from multiprocessing import freeze_support

from sklearn.metrics import accuracy_score

from dask.diagnostics.progress import ProgressBar
ProgressBar().register()


def main():
    # Create a Dask distributed client
    client = Client(memory_limit="5.5GB")

    # Assuming you have a Dask DataFrame named df
    df = dd.read_csv("datasets/transformed.csv")  # type: ignore


    # df = df.astype('category')

    # Splitting the data into features (X) and target variable (y)
    X = df.drop('Label', axis=1)
    y = df['Label']

    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

    # # Convert Dask DataFrame to Pandas DataFrame for XGBoost
    # X_train = X_train.compute()
    # X_test = X_test.compute()
    # y_train = y_train.compute()   
    # y_test = y_test.compute()

    dtrain = xgb.dask.DaskDMatrix(client, X_train, y_train, enable_categorical=True)
    dtest = xgb.dask.DaskDMatrix(client, X_test, y_test, enable_categorical=True)

    params = {
        "max_depth": 6,
        "gamma": 0,
        "eta": 0.3,
        "min_child_weight": 30,
        "objective": "req:squarederror",
        "grow_policy": "depthwise",
        'objective': 'reg:squarederror',
    }

    output = xgb.dask.train(
        client, params, dtrain, num_boost_round=4,
        evals=[(dtrain, 'train')]
    )

    y_pred = xgb.dask.predict(client, output, dtest)
    print(y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print("---xgboost---")

    print("Accuracy:", accuracy)

if __name__ == "__main__":
    freeze_support()
    main()

