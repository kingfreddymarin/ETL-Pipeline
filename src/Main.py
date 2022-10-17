from Extract import extract

if __name__ == '__main__':
    print("-------------------------")
    print("DATOS INICIALES SSMS!!! ")
    print("-------------------------")
    SSMS_SERVER = input("Ingrese el servidor (localhost, etc): ")
    # This is the source database
    SSMS_DB = input("Ingrese el nombre de la base de datos de origen: ")
    # SQL Server user id and password
    SSMS_USER = input("Ingrese el usuario: ")
    SSMS_PW = input("Ingrese la contraseña: ")
    # POSTGRESQL CREDENTIALS
    print("-------------------------")
    print("DATOS INICIALES PSQL!!!")
    print("-------------------------")
    PSQL_SERVER = input("Ingrese el servidor (localhost, etc): ")
    PSQL_DB = input("Ingrese el nombre de la base de datos de destino: ")
    PSQL_USER = input("Ingrese el usuario administrador de la base: ")
    PSQL_PW = input("Ingrese la contraseña: ")
    try:
        extract(SSMS_DB, SSMS_PW, SSMS_SERVER, SSMS_USER,
                PSQL_DB, PSQL_PW, PSQL_SERVER, PSQL_USER)
    except Exception as e:
        print("Error: " + str(e))
