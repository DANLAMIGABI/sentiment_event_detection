from blaze.compute.tests.test_spark import pyspark
from pyspark.mllib.fpm import FPGrowth
from pyspark import SparkContext
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("building a warehouse")
sc =pyspark.SparkContext("local")
data = sc.textFile("results/tweets title.txt")
transactions = data.map(lambda line: line.strip().split(' '))
model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
result = model.freqItemsets().collect()


for fi in result:
    print(fi)
