import pandas as pd
from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .getOrCreate()

data = {'nome': ['fulanoA de tal', 'fulanoB de tal', 'fulanoC de mal'], 'idade': [15, 20, 12]}

df = pd.DataFrame(data)

spark_df = spark.createDataFrame(df)

spark_df.show()
