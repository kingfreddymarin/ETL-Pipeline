import pandas as pd
import pyodbc

from Load import load


def extract(SSMS_DB, SSMS_PW, SSMS_SERVER, SSMS_USER,
            PSQL_DB, PSQL_PW, PSQL_SERVER, PSQL_USER):
    try:
        # Setup the connection
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER=' +
                                  SSMS_SERVER + ';DATABASE=' + SSMS_DB + ';UID='+SSMS_USER+';PWD='+SSMS_PW)
        crs = conexion.cursor()
        # Verifying all the tables we want to use in the package
        crs.execute(f"""
            select t.name as table_name
            from sys.tables t 
        """)  # //LEGACY -> where t.name in ('FACT_MXvideos', 'DIM_Comments', 'DIM_Dates', 'DIM_Ratings', 'DIM_VideoStatus')
        # Fetching tables to be modified
        src_tables = crs.fetchall()
        # Looping through the tables in src_tables in order to clean and load data
        for table in src_tables:
            # Creating and loading data into dataframe
            df = pd.read_sql_query(f"SELECT * FROM {table[0]}", conexion)
            # cleaning process
            df = df[df.video_id != '#NAME?']
            # Removing rows where views are null || none
            if table[0] == 'DIM_VideoStatus':
                df = df[df.views != None]
            # Removing useless columns
            if table[0] == 'FACT_MXvideos':
                to_drop = ['title', 'thumbnail_link', 'description']
                df.drop(to_drop, axis=1, inplace=True)
            # formatting dates into datetime
            if table[0] == 'DIM_Dates':
                df['publish_time'] = pd.to_datetime(
                    df['publish_time'], errors="coerce")
                df['trending_date'] = pd.to_datetime(
                    df['trending_date'], errors="coerce")
            # TRANSFORMING DATATYPES
            for col in df:
                # FROM OBJECT TO STRING
                if df[col].dtypes == object:
                    df[col] = df[col].astype(pd.StringDtype())
                    # FROM [none] to NA
                    cond = df[col] == '[none]'
                    df.loc[cond, col] = 'NA'
                # FROM None to 0
                if df[col].dtypes == int:
                    # cond = df[col] == None
                    # df.loc[cond, col] = 0
                    df[col].fillna(value=0)
            # Loading process
            load(df, table[0], PSQL_DB, PSQL_PW,
                 PSQL_SERVER, PSQL_USER)

            print(df.info())
    except Exception as e:
        print(f'Error...\n datos: '+str(e))
    finally:
        conexion.close()
