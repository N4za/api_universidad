import web
import app
import csv
import json


class Delete:
    file = "/static/csv/alumnos.csv"

    def __init__(self):
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                if data['action'] == "delete":
                    matricula = data['matricula']
                    resultC = self.actionDelete(self.file, matricula)
                    return json.dumps(resultC)
            else:
                result = {}
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            result = {}
            result['status'] = "Values missing"
            return json.dumps(result)

    @staticmethod
    def actionDelete(file, matricula):
        try:
            result = []
            resultC = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if(row['matricula'] != matricula):
                        resultC['status'] = "200 Ok"
                        result.append(row)
                        resultC['alumnos'] = result
            longitud = (len(result))
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
                for x in range(0, longitud):
                    data.append(result[x]['matricula'])
                    data.append(result[x]['nombre'])
                    data.append(result[x]['primer_apellido'])
                    data.append(result[x]['segundo_apellido'])
                    data.append(result[x]['carrera'])
                    writer.writerow(data)
                    data = []
            results = []
            resultsC = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    results.append(row)
                    resultsC['status'] = "200 Ok"
                    resultsC['alumnos'] = result
            return resultsC
        except Exception as e:
            result = {}
            result['status'] = "Error"
        return result
