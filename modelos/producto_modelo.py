from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table , String
from sqlalchemy.orm import declarative_base, relationship

# defino las tablas
class Producto(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    tipo=db.column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,precio,stock,tipo,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.stock=stock
        self.tipo=tipo
        self.imagen=imagen

with app.app_context():
    db.create_all()
