# 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
import pandas as pd
from sqlalchemy import create_engine
import argparse


def main(params):
    user = params.user
    password = params.password
    table_name = params.table_name
    port = params.port
    url = params.url
    db = params.db
    host = params.host
    file_type = params.file
    
    #load the file into dataframe depending on the type of file we are passing
    if file_type=="parquet":
        df = pd.read_parquet(url)
    elif file_type=="csv":
        df = pd.read_csv(url)
    else:
        raise ValueError('The file type being uploaded is not csv or parquet which are the only supported')
    
    #Create connection to the database
    engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user,password,host,port,db))

    #change the datetime columns from text to datetime format if they are not converted
    if table_name=="green_taxi_data" and file_type=="csv":
        df["lpep_pickup_datetime"] = pd.to_datetime(df.lpep_pickup_datetime)
        df["lpep_dropoff_datetime"] = pd.to_datetime(df.lpep_dropoff_datetime)

    if table_name=="yellow_taxi_data" and file_type=="csv":
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(0).to_sql(name=table_name, con=engine, if_exists="replace")

   


    for i in range(0, len(df), 1000000):
        chunk = df[i : i + 1000000]
        chunk.to_sql(name=table_name, con=engine, if_exists="append", index=False)
        print("Batch{} has been uploaded into the database".format(i))

    print('Data upload done Succesfully into {}'.format(table_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest parquet data into postgress")
    # user
    # password
    # table name
    # port
    # database
    # url to the parquet file

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--table_name", help="Name of the target table in the database")
    parser.add_argument("--port", help="database port")
    parser.add_argument("--url", help="url for the parquet file")
    parser.add_argument("--db", help="target database name")
    parser.add_argument("--host", help="host")
    parser.add_argument("--file",help="The type of file you are ingesting")


    args = parser.parse_args()

    main(args)
