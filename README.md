# Airflow_flow
Learning Airflow


Docker Run:

docker-compose -f docker-compose.yml up -d --force-recreate

Spark 

We need Hadoop Cluster to Run Spark -- Seattle Data Guy 

We Can Do fine with just local server 
Data Ingestion - Spark ( Pyspark ) 
Data Processing (ETL)- Pyspark Or PySpark in DataBricks Or Hive 
Data Orchestration - Airflow Or DataBricks Or Autosys 
Data Report - Tableau


Design Data Pipeline : Transfer Data from Producer to Consumer 

1) ETL 
2) ELT 


- Data Source : Database, Csv, Json files 
- ETL : Extract, Transform, Load ( Pyspark, Pandas, SQL's, Hive etc)
- Data Target/ Warehouse : Transformed Data Gets Stored 
- Data report : Reporting Tool on Top of Transformed Data


Data Ingestion : Unchanged Data Insert from Raw to Target ** better to take as Last 

* Airflow with pyspark seems to be Bad Idea, But Airflow with Pandas looks good -- Deep Dive 

Airflow is an Orchestrater - What Alternate incase of Pyspark ? DataBricks, Autosys etc 

# Mistakes in Airflow 

# Design of the Workflows 

- Dags and Docker containers should be in seperate CI/CD 

- Ex: in Shopify, 
    - Git Repo -> Dev Repo -> Dev S3 Bucket -> CI/CD -> Airflow Server Dev 
    - Git Repo -> Test Repo -> Test S3 Bucket -> CD/CD -> Airflow Server Test 
    - Git Repo -> Prod Repo -> Prod S3 Bucket -> CI/CD -> Airflow Server PROD 

# learn about hooks & Variables  in Airflow and implement them 

# Hooks 
- Custom Connection Interface to connect to variable platforms like Big Query, Hive, etc 
- Can Store these Connection in a hook, and pull the hook instead of having connection string in each DAG 

# Variables

- Environmental Variables for airflow

# Scaling Airflow 

- Learn about MWAA architecture 


# If Docker to be used for Pyspark 

https://medium.com/@mehmood9501/using-apache-spark-docker-containers-to-run-pyspark-programs-using-spark-submit-afd6da480e0f