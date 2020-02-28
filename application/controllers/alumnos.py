import web  # pip install web.py
import csv  # CSV parser
import json  # json parser

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la
    URL: http://localhost:8080/alumnos?action=get&token=1234

    Control de Busqueda por matricula que es invocado cuando el usuario ingresa a la 
    URL: 
'''
class Alumnos:
    app_version = "0.03"
    file = 'static/csv/alumnos.csv'
    def __init__(self):
        pass  

#GET
    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234": 
                if data['action'] == 'get': 
                    result = self.actionGet(self.app_version,self.file) 
                    return json.dumps(result) 
                elif data['action'] == 'search':
                    matricula = data['matricula']
                    result = self.actionSearch(self.app_version, self.file, matricula)
                    return json.dumps(result)
                elif data['action'] == 'put':
                    matricula = int(data['matricula'])
                    nombre = str(data['nombre'])
                    primer_apellido = str(data['primer_apellido'])
                    segundo_apellido = str(data['segundo_apellido'])
                    carrera = str(data['carrera'])
                    alumno=[]
                    alumno.append(matricula)
                    alumno.append(nombre)
                    alumno.append(primer_apellido)
                    alumno.append(segundo_apellido)
                    alumno.append(carrera)
                    result = self.actionPut(self.app_version, self.file, alumno)
                    return json.dumps(result)
                elif data['action'] == 'delete':
                    matricula = data['matricula']
                    result = self.actionDelete(self.app_version, self.file, matricula)
                    return json.dumps(resul)
                else:
                    result = {} 
                    result['app_version'] = self.app_version 
                    result['status'] = "Command not found"
                    return json.dumps(result) 
            else:
                result = {} 
                result['app_version'] = self.app_version 
                result['status'] = "Invalid Token"
                return json.dumps(result) 
        except Exception as e:
            print("Error" + str(e.args(e)))
            result = {} 
            result['app_version'] = self.app_version 
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result) 
#GET
    @staticmethod
    def actionGet(app_version, file):
        try:
            result = {} 
            result['app_version'] = app_version 
            result['status'] = "200 ok" 
            result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n¨"
            with open(file, 'r') as csvfile: 
                reader = csv.DictReader(csvfile) 
                alumnos = [] 
                for row in reader: 
                    fila = {} 
                    fila['matricula'] = row['matricula']  
                    fila['nombre'] = row['nombre'] 
                    fila['primer_apellido'] = row['primer_apellido'] 
                    fila['segundo_apellido'] = row['segundo_apellido'] 
                    fila['carrera'] = row['carrera'] 
                    alumnos.append(fila) 
                result['alumnos'] = alumnos 
            return result 
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args))
            result['app_version'] = app_version 
            result['status'] = "Error " 
            return result 
#SEARCH BUSQUEDA
    @staticmethod
    def actionSearch(app_version, file, matricula):
        try:
            result = {} 
            result['app_version'] = app_version 
            result['status'] = "200 ok" 

            with open(file, 'r') as csvfile: 
                reader = csv.DictReader(csvfile) 
                alumnos = [] 
                for row in reader: 
                    if (row['matricula'] == matricula):
                        fila = {}
                        fila['matricula'] = row['matricula']
                        fila['nombre'] = row['nombre']
                        fila['primer_apellido'] = row['primer_apellido']
                        fila['segundo_apellido'] = row['segundo_apellido']
                        fila['carrera'] = row['carrera']
                        alumnos.append(fila)
                    result['alumnos'] = alumnos
            return result 
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args))
            result['app_version'] = app_version 
            result['status'] = "Error " 
            return result
#PUT NUEVO REGISTRO
    @staticmethod
    def actionPut(app_version, file, alumno):
        try:
            result = {} 
            result['app_version'] = app_version 
            result['status'] = "200 ok" 
            result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n¨"
            with open(file, 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(alumno)
            with open(file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                alumno = []
                for row in reader:
                    fila = {}
                    fila['matricula'] = row['matricula']
                    fila['nombre'] = row['nombre']
                    fila['primer_apellido'] = row['primer_apellido']
                    fila['segundo_apellido'] = row['segundo_apellido']
                    fila['carrera'] = row['carrera']
                    alumnos.append(fila)
                result['alumnos'] = alumnos
            return result
        except Exception as e:
            result = {}
            result['app_version'] = app_version
            print("Error {}".format(e.args))
            result['status'] = "Error"
            return result
##DELETE
    @staticmethod
    def actionDelete(app_version, file):
        try:
            result = {} 
            result['app_version'] = app_version 
            result['status'] = "200 ok" 
            with open(file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                alumno = []
                for row in reader:
                    fila = {}
                    fila['matricula'] = row['matricula']
                    fila['nombre'] = row['nombre']
                    fila['primer_apellido'] = row['primer_apellido']
                    fila['segundo_apellido'] = row['segundo_apellido']
                    fila['carrera'] = row['carrera']
                    alumnos.append(fila)
                result['alumnos'] = alumnos
            return result
        except Exception as e:
            result = {}
            print("Error {}".format(e.args))
            result['app_version'] = app_version
            result['status'] = "Error"
            return result