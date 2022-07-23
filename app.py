from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    try:
        raise Exception("We are testing exception module")
    except Exception as e:
        housing=HousingException(e,sys) from e
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI/CD pipeline has been established"


if __name__=="__main__":
    app.run(debug=True)