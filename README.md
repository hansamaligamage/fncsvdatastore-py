# Azure function (Python) to store csv data in Cosmos DB - Table API

This is a http trigger function written in Python in Visual Studio Code. It processes a csv file and store the data on Cosmos DB Table API

## Technology stack  
* Python version 3.8.2 64 bit version https://www.python.org/downloads/release/python-382/
* Azure functions for python version 1.2 *(azure-functions 1.2.0)* https://pypi.org/project/azure-functions/
* Azure Cosmos DB Table 1.0.6 *(azure-cosmosdb-table 1.0.6)* to connect to the Cosmos DB Table API https://pypi.org/project/azure-cosmosdb-table/

## How to run the solution
 * You have to create a Cosmos DB account with Table API and go to the Connection String section and get the connectionstring to connect to the database
 * Open the solution from Visual Studio code, create a virtual environment to isolate the environment to the project by running, *py -m venv .venv* command. It will install all the required packages mentioned in the *requirements.txt* file

## Code snippets
### Create Azure Table service
