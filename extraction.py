from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask import make_response
import mysql.connector
import pandas as pd
import time
from pprint import pprint

class DownloadCSVData:
    def __init__(self):
        try:
            mydb = mysql.connector.connect(host="host",user="user", passwd="password", database="db")
            mycursor = mydb.cursor()
            sql = "SELECT * FROM goxipdb.members"
            mycursor.execute(sql)
            self.data = pd.DataFrame(mycursor.fetchall())
            self.columns = mycursor.column_names

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        finally:
            mycursor.close()
            mydb.close()

    def __call__(self):
        df = self.data
        df.columns = self.columns
        #pprint(df)
        file_name = time.strftime('%Y%m%d', time.localtime(time.time())) + '.csv'
        response = make_response(df.to_csv(index = False))
        response.headers["Content-Disposition"] = "attachment; filename=%s" %file_name
        response.headers["Content-type"] = "text/csv"
        return response

class Submit(FlaskForm):
    submit = SubmitField('')
