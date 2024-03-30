# Intuitive Care Tests

All tests are in a directory whose name is related to the activity.

All tests where written in Python (3.12.0) or SQL and/or use a Dockerfile and docker-compose.yml.

Everything needed to run all the tests is on the
requirements.txt file.

In your machine, you can run

```{sh}
$ pip install -r requirements.txt
```

to install everything locally.


## Web Scrapper

It can bu run in root, in solutions.py

```{sh}
$ python solution.py
```


## Data from PDF

Here, it is better to follow a restrict file organization: inside the folder (data_from_pdf)
you have to include the folder <em>data</em>. Inside this folder, you include the pdf file.

Also, you can change the path and the filename (pdf) in the python code and run:

```{sh}
$ python pdf.py
```

The file "see.py", is only to test the results with a pandas dataframe.

## SQL Tests

Here, you must have docker installed to test. All the files are copied to a container
where postgres BULK INSERT in the tables.
The answers queries are the files: query1.sql and query2.sql

Expect file structure:

```
sql_tests
│   
│   docker-compose.yml
|   query1.sql
|   query2.sql
|   schema.sql    
│
└───data
│   │   relatorio.csv
│   │
│   └───2022
│   |   │   1T2022.csv
│   |   │   2T2022.csv
|   |   |   3T2022.csv
|   |   |   4T2022.csv
│   └───2023
│       │   1T2023.csv
│       │   2T2023.csv
|       |   3T2023.csv
```

## API

Here, you will only find the API in python, with a docker-compose to build a container
with everything.

The "requirements.txt" are also differents (without pandas and pypdf).

It was made using FastAPI.

Expect file structure:

```
api
│   
└───backend
│   │   ...
│   │
│   └───data
│   |   │   relatorio.csv
```
