import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df=spark.read.csv("C:/Users/singh/Desktop/ML_Practice/Titanic.csv",inferSchema=True,header=True)

df.show()