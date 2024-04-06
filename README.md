# sample-data-contracts-py

Sample data contracts for data integration with Python

## about

- This repo is for demonstrating how to create and validate data contracts using python & openapi.
- It is written aside blogs described below.

## blog related

- [EN] [Data contracts in (real-time) action (with Python)]()
- [TH] [สัญญา(ไม่)ปากเปล่า - data contracts in action (Python)]()
- [Medium] [Data contracts in (real-time) action (with Python)]()

## How to run

### Prerequisites

- [python](https://www.python.org/downloads/)

### Executions

1. install packages via
  
    ```shell
    cd sample-data-contracts-py/src
    pip install --no-cache-dir -r requirements.txt
    ```

1. start Flask using

    ```shell
    python3 app.py
    ```

1. the api will be ready on port 4001
1. try call the api using tools e.g. postman or curl

    ```shell
    curl --location 'localhost:4001/people' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        "name": "Michael",
        "age": 18,
        "email": "test@email.com"
        }'
    ```

    ```shell
    curl --location 'localhost:4001/pets' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        {
        "name":"rocky",
        "age": 2,
        "ownerName": "Richard"
        }'
    ```

### Test result examples

- `/people`: ok
![ok](./resources/01-call-ok.png)
- `/people`: wrong types
![wrong type](./resources/02-call-failed-wrong-types.png)
- `/people`: missing required fields
![wrong type](./resources/03-call-failed-missing-req-field.png)
- `/pets`: missing required fields
![wrong type](./resources/04-call-failed-pets.png)
