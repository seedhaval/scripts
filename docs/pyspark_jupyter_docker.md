# PySpark and Jupyter on docker in Desktop system

Step 1 - Install docker from https://docs.docker.com/desktop/install/windows-install/

Step 2 - Open docker desktop and ensure that the docker engine is in running state

Step 3 - Pull the bitnami spark docker container. Run below command on terminal

    docker pull bitnami/spark

Step 4 - Run spark container interactively

    docker run -it -p 4040:4040 -p 8888:8888 --name spark-container --hostname spark bitnami/spark /bin/bash

Step 5 - Install and start Jupyter notebook in the container

    pip install jupyter
    pip install py4j
    export PATH="$PATH:/.local/bin"
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

Take a note of the token as it will be required in next step.

Step 6 - Access Jupyter notebook at http://localhost:8888
Create a notebook in /tmp from UI

Step 7 - Run sample PySpark commands in Jupyter cell

```python
from pyspark.sql import SparkSession
    
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
sc = spark.sparkContext

nums = sc.parallelize([1,2,3,4])
print(nums.map(lambda x: x*x).collect())
```
