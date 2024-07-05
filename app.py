from flask import Flask #,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy


from flask_marshmallow import Marshmallow

app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userpython24178:34697923m@userpython24178.mysql.pythonanywhere-services.com/userpython24178$default'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://luisguerra:prueba1234@luisguerra.mysql.pythonanywhere-services.com/luisguerra$lacocinadejuan'

# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none

db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow
from controladores.usuario_controlador import *
from controladores.producto_controlador import *



# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  


