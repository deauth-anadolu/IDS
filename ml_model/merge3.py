import dask.dataframe as dd
from dataset_functions import *
from constants import *
from dask.diagnostics.progress import ProgressBar
ProgressBar().register()


# df = dd.read_csv("/media/hsrv/data/merged_deauth.csv", dtype=dtypes) # type: ignore
# df = dd.read_csv("deneme.csv", dtype=dtypes) # type: ignore

# print(ddf.npartitions)
# print(ddf.dtypes)

# ddf = ddf.astype(dtype)

# print(ddf.shape)
# print(len(ddf))


# Drop the columns where all elements are missing.
# ddf = ddf.loc[:, ~ddf.isna().all().compute()]
# print(len(ddf))
# print(ddf.shape)

# # Drop the rows where all elements are missing.
# ddf.dropna(how='all')
# print(len(ddf))


# Dataset'te zaten Deuath veya Normal dışında bir Label değeri yok, o yüzden aşağıdakilerden birini çalıştırmaya gerek yok.
# df = df[(df['Label'] == 'Deauth') | (df['Label'] == 'Normal')]
# ya da
# df = df[df["Label"].isin(["Deauth", "Normal"])]

# df = df.loc[:, ~df.isnull().all()]
# df.fillna(value="?üşçığö?")
# print(df.shape)
# df.to_csv("deneme2.csv", single_file=True, index=False)
# print(len(df))



# # Check for missing values before filling
# print(df.isnull().sum().compute())

# df = df.fillna(value="?")

# # Check for missing values after filling (should be zero)
# print(df.isnull().sum().compute())

# # Inspect the DataFrame
# print(df.head().compute())  # Or use df.head() for a Dask-aware preview



# # Check for missing values before filling
# print("AAA")
# print(df.isnull().sum().compute())

# df = df.fillna("?")

# # Check for missing values after filling (should be zero)
# print("BBB")
# print(df.isnull().sum().compute())

# # Inspect the DataFrame (using compute())
# print("CCC")
# print(df.head())  # Or use df.head() for a Dask-aware preview


# df = df.fillna("?")
# print(len(df))
# df = df.dropna(thresh=253)
# print(len(df))ş
# df.to_csv("deneme2.csv", single_file=True, index=False)

# df = df.drop(columns=columns_to_drop)
# df = df.fillna("?")
# print(df.shape)
# df.to_csv("deneme3.csv", index=False, single_file=True)


df = dd.read_csv("deneme6.csv", dtype=dtypes)  # type: ignore
print(df.shape)
print(df.npartitions)


from ml_model.columns_to_delete import *
columns_to_drop_final = make(columns_to_delete, df.columns)
df = df.drop(columns=columns_to_drop_final)
df.to_csv("clean1.csv", index=False, single_file=True)

