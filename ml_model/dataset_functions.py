import dask.dataframe as dd
import numpy as np  

def split_dataset_by_percentage(df, percentage: float):
    total_rows = len(df)
    # toplam satırların kaç tanesini almak istediğimizi belirliyoruz
    n_ = int(total_rows * percentage)

    # head'in, dask'ın dataset'ten ürettiği kaç partition'u içereceğini ve bu değerin en fazla max(npartitions) kadar olacağını belirliyoruz.
    n_partitions = np.clip(int(percentage)+1, 0, df.npartitions)

    splitted_data = df.head(n=n_, npartitions=n_partitions)
    return splitted_data