import os
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


# Configurar SPARK_HOME y añadir el directorio bin al PATH
spark_home = r"C:\Python312\Scripts"
os.environ["SPARK_HOME"] = spark_home
os.environ["PATH"] += os.pathsep + os.path.join(spark_home, "bin")