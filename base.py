from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local").setAppName
sc = SparkContext(conf=conf)