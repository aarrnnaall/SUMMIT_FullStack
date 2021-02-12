import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import json
#AGREGAR USUARIO
@app.route('/api/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		_fullname = _json['fullname']
		# validate the received values
		if _name and _email and _password and _fullname and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password,user_fullname) VALUES(%s, %s, %s,%s)"
			data = (_name, _email, _hashed_password,_fullname)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			notify = {'notify': 'User added successfully!'}
			resp = jsonify(notify)
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
#AUTENTICAR
@app.route('/api/auth', methods=['POST'])
def auth():
	try:
		_json = request.json
		_name = _json['name']
		_password = _json['pwd']
		_hashed_password = generate_password_hash(_password)
		# save edits
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql="SELECT user_password FROM tbl_user WHERE user_name=%s"
		data = (_name)
		cursor.execute(sql, data)
		row = cursor.fetchone()
		if row != None:
			resp = jsonify(row)
			resp.status_code = 200
			#parse user_password
			str_row = str(row)
			split_row=str_row.split("{'user_password':",2)
			if len(split_row) == 2:
				split_row2=split_row[1].split("}")
				split_row3=split_row2[0].split("'")
				row_end=split_row3[1]
				if check_password_hash(row_end,_password):
					encoded_jwt = jwt.encode({"some": "thissecret"}, "secret", algorithm="HS256")
					json_resp={'jwt_token':encoded_jwt}
					resp = jsonify(json_resp)
					return resp
				else:
					notify={'notify':'Incorrect password'}
					resp = jsonify(notify)
					return resp
			else:
				notify = {'notify': 'Incorrect user'}
				resp = jsonify(notify)
				return resp
		else:
			notify = {'notify': 'Incorrect user'}
			resp = jsonify(notify)
			return resp

	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
#MOSTRAR USUARIOS
@app.route('/api/users', methods=['GET'])
def users():
	try:
		_json = request.json
		_jwt_token = _json['jwt_token']
		_check = {'some': 'thissecret'}
		if _check ==jwt.decode(_jwt_token, "secret", algorithms=["HS256"]):
			try:
				conn = mysql.connect()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				cursor.execute("SELECT * FROM tbl_user")
				rows = cursor.fetchall()
				resp = jsonify(rows=rows)
				resp.status_code = 200
				return resp
			except Exception as e:
				print(e)
			finally:
				cursor.close()
				conn.close()
		else:
			notify = {'notify': 'Error token'}
			resp = jsonify(notify)
			return resp
	except Exception:
		notify = {'notify': 'Error token'}
		resp = jsonify(notify)
		return resp
#MOSTRAR USUARIO POR ID
@app.route('/api/user/<int:id>', methods=['GET'])
def user(id):
	try:
		_json = request.json
		_jwt_token = _json['jwt_token']
		_check = {'some': 'thissecret'}
		if _check ==jwt.decode(_jwt_token, "secret", algorithms=["HS256"]):
			try:
				conn = mysql.connect()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
				row = cursor.fetchone()
				resp = jsonify(row=row)
				resp.status_code = 200
				return resp
			except Exception as e:
				print(e)
			finally:
				cursor.close()
				conn.close()
		else:
			notify = {'notify': 'Error token'}
			resp = jsonify(notify)
			return resp
	except Exception:
		notify = {'notify': 'Error token'}
		resp = jsonify(notify)
		return resp
#ACTUALIZAR USUARIO
@app.route('/api/update', methods=['PATCH'])
def update_user():
	try:
		_json = request.json
		_jwt_token = _json['jwt_token']
		_check = {'some': 'thissecret'}
		if _check ==jwt.decode(_jwt_token, "secret", algorithms=["HS256"]):
			try:
				_id = _json['id']
				_name = _json['name']
				_email = _json['email']
				_password = _json['pwd']
				_fullname = _json['fullname']
				if _name and _email and _password and _fullname and _id and request.method == 'PATCH':
					_hashed_password = generate_password_hash(_password)
					sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s, user_fullname=%s WHERE user_id=%s"
					data = (_name, _email, _hashed_password,_fullname, _id)
					conn = mysql.connect()
					cursor = conn.cursor()
					cursor.execute(sql, data)
					conn.commit()
					notify = {'notify': 'User updated successfully!'}
					resp = jsonify(notify)
					return resp
				else:
					return not_found()
			except Exception as e:
				print(e)
			finally:
				cursor.close()
				conn.close()
		else:
			notify = {'notify': 'Error token'}
			resp = jsonify(notify)
			return resp
	except Exception:
		notify = {'notify': 'Error token'}
		resp = jsonify(notify)
		return resp
#ELIMINAR USUARIO
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
	try:
		_json = request.json
		_jwt_token = _json['jwt_token']
		_check = {'some': 'thissecret'}
		if _check ==jwt.decode(_jwt_token, "secret", algorithms=["HS256"]):
			try:
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
				conn.commit()
				notify = {'notify': 'User deleted successfully!'}
				resp = jsonify(notify)
				resp.status_code = 200
				return resp
			except Exception as e:
				print(e)
			finally:
				cursor.close()
				conn.close()
		else:
			notify = {'notify': 'Error token'}
			resp = jsonify(notify)
			return resp
	except Exception:
		notify = {'notify': 'Error token'}
		resp = jsonify(notify)
		return resp
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run()
