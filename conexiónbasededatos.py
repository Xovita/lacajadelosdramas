from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fullstack'
app.config['MYSQL_DB'] = 'lacaja'
mysql = MySQL(app)

@app.route('/mensajes', methods=['POST'])	
@cross_origin()	
def mensajes():
		if request.method == 'POST':
			request_data = request.get_json()
			nombre = request_data['nombre']
			email =request_data['email']
			mensaje=request_data['mensaje']
			cur = mysql.connection.cursor()
			cur.execute('INSERT INTO Mensajes (Nombre,Mail,Mensaje) VALUES (%s, %s, %s)', (nombre,email,mensaje) )			
			mysql.connection.commit()
			return "Guardado OK"
					
			
if __name__	== '__main__':
			app.run(host='0.0.0.0',port=4022)
			
