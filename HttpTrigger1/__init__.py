import logging
import json
import csv
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    connectionstring = config_data["connectionstring"]
    table_service = TableService(connection_string=connectionstring)

    table = config_data["table"]
    tableExists = table_service.create_table(table)

    courses = readcsv();
    
    for item in courses:
        # print(item)
        task = Entity()
        task.PartitionKey = item.subject
        task.RowKey = item.instructor
        task.lectures = item.lectures
        task.labs = item.labs
        task.points  = item.points
        task.isWeekend = item.isWeekend
        table_service.insert_entity(table, task)

    return func.HttpResponse("Cosmos DB - Table API example database is created.")
    
def readcsv () :
    list = []
    with open('courses.csv') as file:
        reader = csv.DictReader(file)
        for line in reader :
            list.append(course(line["Subject"], line["Instructor"], line["Lectures"], line["Labs"], line["Points"], line["Weekend"]))
        return list

class course :
    def __init__(self, subject, instructor, lectures, labs, points, isWeekend) :
        self.subject = subject
        self.instructor = instructor
        self.lectures = lectures
        self.labs = labs
        self.points = points
        self.isWeekend = isWeekend
