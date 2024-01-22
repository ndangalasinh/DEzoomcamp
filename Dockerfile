FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 pyarrow fastparquet argparse
WORKDIR /app

COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python","ingest_data.py" ]