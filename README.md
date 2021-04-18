# ITEMS API

## SETUP
python version: python 3.8 +

```
pip install flask

python3 app.py
```

Technical notes:
1. Data source used is Sqlite3, as it requirement was to proviede easiest to setup locally.
2. Nothing other than flask is needed for app to work.
</br> 


## CRUD Functionality

#### CREATE </br>
Endpoint: localhost:5000/items/ </br>
payload: 
```
{
    "file_name":"file name here",
    "media_type":"mov"
}
```
Response:
```
{
  "data": {
    "created_at": "datetime",
    "file_name": "string",
    "id": int,
    "media_type": "string",
    "updated_at": "datetime"
  },
  "result": "success|Failure"
}

Example:
{
  "data": {
    "created_at": "2021-04-18 19:05:05",
    "file_name": "10file1",
    "id": 13,
    "media_type": "mov",
    "updated_at": "2021-04-18 19:05:05"
  },
  "result": "success"
}
```

#### GET/ RETRIEVE
Endpoint: localhost:5000/items/\<id\> </br>
Response:
```
{
  "created_at": "2021-04-18 19:05:05",
  "file_name": "10file1",
  "id": 13,
  "media_type": "mov",
  "updated_at": "2021-04-18 19:05:05"
}

```
If not found </br>
```
{
  "result": "Not Found."
}
```

#### UPDATE
Endpoint: localhost:5000/items/\<id\> </br>
payload: 
```
{
    "file_name":"Modified name here",
    "media_type":"MOD_mov"
}
```
Response:
```
{
  "data": {
    "created_at": "2021-04-18 19:05:05",
    "file_name": "Modified name here",
    "id": 13,
    "media_type": "MOD_mov",
    "updated_at": "2021-04-18 19:16:58"
  },
  "result": "Data updated successfully."
}
```

#### DELETE
Endpoint: localhost:5000/items/\<id\> </br>
Response:
```
{
  "result": "Data deleted successfully."
}
```