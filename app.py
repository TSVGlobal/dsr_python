from flask import Flask
from database.database import db
import csv
import os
from routes.routes import main_bp
from models.air_dsr import AIRDSR
from models.sea_dsr import SEADSR


app=Flask(__name__)
app.secret_key="gdjidhakkjhwwknjcoih"
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:@localhost/dsr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)



app.register_blueprint(main_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()#create a table if it does not exist
    app.run()


