# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:56:16 2020

@author: esol
"""


from pyspark.sql.functions import *
from pyspark import *

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


import numpy as np
import pandas as pd

# Enable Arrow-based columnar data transfers
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

# Generate a Pandas DataFrame
pdf = pd.DataFrame(np.random.rand(100, 3))
df = spark.createDataFrame(pdf)