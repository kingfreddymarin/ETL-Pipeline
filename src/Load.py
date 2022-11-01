import pandas as pd
from sqlalchemy import create_engine


def load(df, table, PSQL_DB, PSQL_PW, PSQL_SERVER, PSQL_USER):
    try:
        # Creating engine with my PostgreSQL credentials [username, password, server, port and objective database (respectively)]
        engine = create_engine(
            f'postgresql://{PSQL_USER}:{PSQL_PW}@{PSQL_SERVER}:5432/{PSQL_DB}'
        )
        print(
            f' Importando {len(df)} filas en la tabla {table}... '
        )
        # Loading transformed data to PostgreSQL
        df.to_sql(f'{table}', engine, if_exists='replace', index=False)
        print("Datos importados con exito")
    except Exception as e:
        print(f'Error: ' + str(e))
