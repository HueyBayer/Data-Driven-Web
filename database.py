from sqlalchemy import create_engine, text

database_connection = "mysql+pymysql://sc9al75jcwv5ggdf7e0f:pscale_pw_GXIc7myc3G7qmIxWjq6UHa1p93wGQIjbA3FO0oxdadb@aws.connect.psdb.cloud/databasedrivenwebsite?charset=utf8mb4"

engine = create_engine(database_connection, connect_args={"ssl": {"ssl_ca":"/etc/ssl/cert.pem"}})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs