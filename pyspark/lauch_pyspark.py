import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

spark = SparkSession.builder \
    .master("yarn") \
    .appName("demo pyspark job") \
    .config('spark.blacklist.enabled', "true") \
    .config('spark.driver.cores', "8") \
    .config('spark.driver.memory', "4g") \
    .config('spark.executor.cores', "2") \
    .config('spark.executor.memory', "4g") \
    .config('spark.executor.instances', "32") \
    .config('spark.serializer', "org.apache.spark.serializer.KryoSerializer") \
    .config('spark.yarn.queue', "rat") \
    .config('spark.driver.maxResultSize', "2g") \
    .config('spark.sql.orc.enableVectorizedReader', "true") \
    .config('spark.sql.orc.filterPushdown', "true") \
    .config('spark.sql.caseSensitive', "true") \
    .config('mapreduce.fileoutputcommitter.marksuccessfuljobs', "false") \
    .enableHiveSupport() \
    .getOrCreate()

spark
