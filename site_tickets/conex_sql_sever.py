import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-Q3ICRR3\SQLEXPRESS;'
                      'Database=Teste;'
                      'UID=sa;'
                      'PWD=03042003')

def consulta_sqlserver(consulta):
    cursor = conn.cursor()
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados
