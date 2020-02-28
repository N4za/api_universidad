import web
import app
import json
import csv


class Update:
    file = "/static/csv/alumnos.csv"

    def __init__(self):
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                if data['action'] == "update":
                    matricula = data['matricula']
                    matriculaNueva = data['matriculaNueva']
                    nombre = data['nombre']
                    primer_apellido = data['apellido1']
                    segundo_apellido = data['apellido2']
                    carrera = data['carrera']
                    resultB = self.actionUpdate(
                        self.file, matricula, matriculaNueva, nombre, primer_apellido, segundo_apellido, carrera)
                    return json.dumps(resultB)
                else:
                     = {}
                    resultB['status'] = "Command not found"
                    return json.dumps(resultB)
            else:
                result = {}
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            result = {}
            result['status'] = "Values missing"
            return json.dumps(result)

    @staticmethod
    def actionUpdate(file, matricula, matriculaNueva, nombre, primer_apellido, segundo_apellido, carrera):
        try:
            result = []
            resultB = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if(row['matricula'] != matricula):
                        resultB['status'] = "200 Ok"
                        result.append(row)
                        resultB['alumnos'] = result

            longi = (len(result))
            with open('static/csv/alumnos.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                b = []
                b.append("matricula")
                b.append("nombre")
                b.append("primer_apellido")
                b.append("segundo_apellido")
                b.append("carrera")
                writer.writerow(b)
                data = []
                for x in range(0, longi):
                    data.append(result[x]['matricula'])
                    data.append(result[x]['nombre'])
                    data.append(result[x]['primer_apellido'])
                    data.append(result[x]['segundo_apellido'])
                    data.append(result[x]['carrera'])
                    writer.writerow(data)
                    data = []
                c = []
                c.append(matriculaNueva)
                c.append(nombre)
                c.append(primer_apellido)
                c.append(segundo_apellido)
                c.append(carrera)
                writer.writerow(c)

            result = []
            resultB = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    result.append(row)
                    resultB['status'] = "200 Ok"
                    resultB['alumnos'] = result
            return resultB
        except Exception as e:
            result = {}
            result['status'] = "Error"
        return result
    

    #UPDATE
    @staticmethod
    def actionUpdate(app_version, file):
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