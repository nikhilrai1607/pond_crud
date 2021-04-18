import os
from flask import Flask, request, jsonify
import sqlite3
import dbsqlite



#Database setup done!!
db = dbsqlite.db

app = Flask(__name__)

@app.route('/items/<id>',methods=['GET','PUT','DELETE'])
def item_func(id):
    row = dbsqlite.get_row(id)
    if row == None:
        return jsonify({"result":"Not Found."}),404
    
    conn,cur = dbsqlite.cursor()

    if request.method == 'GET':
        if row != None:
            return jsonify(dict(row))
        
    
    elif request.method == 'PUT':
        
        data = request.get_json()
        
        if 'id' in data or 'created_at' in data  or 'updated_at' in data:
            return jsonify({"result":"Change not allowed."}), 403
        else:
            try:
                
                cur.execute('UPDATE item set file_name=?,media_type=? where id=?',(data['file_name'],data['media_type'],id))
                
                conn.commit()
                conn.close()
                print('blah')
                return jsonify({"result":"Data updated successfully.","data":dbsqlite.get_row(id)})
            except:
                return jsonify({"result":"Error updating data."}), 403
          
            
        
    elif request.method == 'DELETE':
        if row:
            try:
            
                cur.execute('DELETE from item where id=?',(id,))
                conn.commit()
                conn.close()
                return jsonify({"result":"Data deleted successfully."}),202
            except:
                return jsonify({"result":"Error deleting data."}), 403

@app.route('/items/',methods=['POST'])
def save_item():

    #recieved data
    data = request.get_json()
    file_name = data['file_name']
    media_type = data['media_type']

    with sqlite3.connect(db) as con:
        try:
            cur = con.cursor()
            cur.execute('INSERT INTO item (file_name,media_type) VALUES (?,?)',(file_name,media_type))
            con.commit()
            id = cur.lastrowid
            result = "success"
            code = 201
        except:
            result = "Failure"
            code = 400
    con.close()
    return jsonify({'result':result,"data":dbsqlite.get_row(id) }),code
    



if __name__ == '__main__':
   app.run(debug = True)

