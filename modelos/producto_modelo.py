from app import app, db   #,ma
from sqlalchemy import Column, Integer, String

class Producto(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id = db.Column(db.Integer, primary_key=True)   # define los campos de la tabla
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(400), nullable=True)

    def __init__(self, nombre, precio, stock, color, imagen): # crea el constructor de la clase
        self.nombre = nombre  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio = precio
        self.stock = stock
        self.color = color
        self.imagen = imagen

with app.app_context():
    db.create_all()