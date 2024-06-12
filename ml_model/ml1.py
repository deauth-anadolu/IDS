import dask.dataframe as dd
from dask_ml.model_selection import train_test_split
from xgboost import XGBClassifier
from dask.distributed import Client
from constants import *
from multiprocessing import freeze_support
from dask.diagnostics.progress import ProgressBar
ProgressBar().register()


def main():

    # Create a Dask distributed client
    client = Client()

    # Assuming you have a Dask DataFrame named df
    df = dd.read_csv("deneme6.csv", dtype=dtypes, blocksize="100mb")  # type: ignore

    # Splitting the data into features (X) and target variable (y)
    X = df.drop('Label', axis=1)
    y = df['Label']

    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

    # Convert Dask DataFrame to Pandas DataFrame for XGBoost
    X_train = X_train.compute()
    X_test = X_test.compute()
    y_train = y_train.compute()
    y_test = y_test.compute()

    # Initialize XGBoost classifier
    model = XGBClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Predictions on the test set
    y_pred = model.predict(X_test)

    # Optionally, you can evaluate the model using appropriate metrics
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Shutdown the Dask client
    client.shutdown()

if __name__ == "__main__":
    freeze_support()
    main()

