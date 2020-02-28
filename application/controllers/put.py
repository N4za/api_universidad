import web
import app
import csv
import json


class Put:
    file = "/static/csv/alumnos.csv"

    def __init__(self):se
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                if data['action'] == "put":
                    matricula = data['matricula']
                    nombre = data['nombre']
                    primer_apellido = data['primer_apellido']
                    segundo_apellido = data['segundo_apellido']
                    carrera = data['carrera']
                    resultB = self.actionPut(
                        self.file, matricula, nombre, primer_apellido, segundo_apellido, carrera)
                    return json.dumps(resultB)

        except Exception as e:
            result = {}
            result['status'] = "Values missing"
            return json.dumps(result)

    @staticmethod
    def actionPut(file, matricula, nombre, primer_apellido, segundo_apellido, carrera):
        try:
            result = []
            resultA = []
            resultB = {}
            resultA.append(matricula)
            resultA.append(nombre)
            resultA.append(primer_apellido)
            resultA.append(segundo_apellido)
            resultA.append(carrera)
            with open('static/csv/alumnos.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(resultR)
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