import web
import app
import csv
import json


class Search:
    file = "/static/csv/alumnos.csv"

    def __init__(self):
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                if data['action'] == 'search':
                    matricula = data['matricula']
                    a1 = self.actionSearch(self.file, matricula)
                    return json.dumps(a1)
                else:
                    a1 = {}
                    a1['status'] = "Command not found"
                    return json.dumps(a1)
            else:
                a = {}
                a['a'] = "Invalid Token"
                return json.dumps(a)
        except Exception as e:
            a = {}
            a['status'] = "Values missing"
            return json.dumps(a)

    @staticmethod
    def actionSearch(file, matricula):
        try:
            a = []
            a1 = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if(matricula == row['matricula']):
                        a.append(row)
                        a1['status'] = "200 Ok"
                        a1['alumnos'] = a
                        break
                    else:
                        a1 = {}
                        a1['status'] = "No esta registrado"
            return a1
        except Exception as e:
            a = {}
            a['status'] = "Error"
            return a