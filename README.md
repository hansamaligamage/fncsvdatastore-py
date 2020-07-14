# A HTTP trigger written in Python to process a CSV file and store data into CosmosDB using Table API 

This is a http trigger function written in Python in Visual Studio Code. It processes a csv file and store the data on Cosmos DB Table API

## Technology stack  
* Python version 3.8.2 64 bit version https://www.python.org/downloads/release/python-382/
* Azure functions for python version 1.2 *(azure-functions 1.2.0)* https://pypi.org/project/azure-functions/
* Azure Cosmos DB Table 1.0.6 *(azure-cosmosdb-table 1.0.6)* to connect to the Cosmos DB Table API https://pypi.org/project/azure-cosmosdb-table/

## How to run the solution
 * You have to create a Cosmos DB account with Table API and go to the Connection String section and get the connectionstring to connect to the database
 * Open the solution from Visual Studio code, create a virtual environment to isolate the environment to the project by running, *py -m venv .venv* command. It will install all the required packages mentioned in the *requirements.txt* file

## Code snippets
### Package references in the code file
```
import logging
import json
import csv
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
```

### Create Azure Table service
```
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    connectionstring = config_data["connectionstring"]
    table_service = TableService(connection_string=connectionstring)
```

### Create Table
```
    table = config_data["table"]
    tableExists = table_service.create_table(table)
```

### Read the csv file
```
def readcsv () :
    list = []
    with open('courses.csv') as file:
        reader = csv.DictReader(file)
        for line in reader :
            list.append(course(line["Subject"], line["Instructor"], line["Lectures"], line["Labs"]
              , line["Points"], line["Weekend"]))
        return list

class course :
    def __init__(self, subject, instructor, lectures, labs, points, isWeekend) :
        self.subject = subject
        self.instructor = instructor
        self.lectures = lectures
        self.labs = labs
        self.points = points
        self.isWeekend = isWeekend
```

### Insert a row
```
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
   ```
