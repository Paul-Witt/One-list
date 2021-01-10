from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

#from config import Config # good practice TOOO install


# Content needed through out our app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theApp.db'
Bootstrap(app) # Add bootstrap blueprint
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
print(db)



#app.config.from_object(Config) # good practice, don't hardcode secrets
app.config['SECRET_KEY'] = "UPDATE ME 89723489790234785708923497" # TODO


from theApp import routes