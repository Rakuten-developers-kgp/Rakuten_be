import logging
import typing 
from fastapi import FastAPI, routing
# from pydantic.fields import FieldInfo, Undefined
import database.mysqldb as db
import database.basemodels as bm


logging.basicConfig(
    level=logging.INFO,
    # format="{asctime} {name} {levelname:<8} log:{message}",
    format= '%(asctime)s %(name)s %(levelname)s:%(message)s',

    # style="{",
    filename="sample_logs_app.log",
    filemode='w'
    )


app = FastAPI()


@app.get("/get_data")
def scan():
    try:
        listt = db.get_data()
        logging.info("endpoint: '/get_data' , Task executed succesfully")
    except:
        error_statement = "Something went wrong with endpoint: /get_data"
        logging.error(error_statement)
        return error_statement
    return listt


@app.post("/input_name")
def input(data: bm.data):
    data = dict(data)

    try:
        name = data.get('name')
        db.input_data(name)
        logging.info("endpoint: '/input_name' , added name succesfully")

    except:
        error_statement = "Something is wrong with your input at endpoint: /input_name"
        logging.error(error_statement)
        return error_statement

@app.delete("/delete_data")
def input(data: bm.data):
    data = dict(data)
    try:
        name = data.get('name')
        db.delete_data(name)
        logging.info("endpoint: '/delete_data' , deleted name succesfully")
    except:
        error_statement = "Something is wrong with your input at endpoint: /delete_data"
        logging.error(error_statement)
        return error_statement