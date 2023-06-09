### Windows:
### python3.9
###### /todos
```
python -m venv .venv
.venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install fastapi uvicorn
pip freeze > requirements.txt
pip install -r requirements.txt
```
### Docker
###### /todos
```
docker build -t api_image .
docker run -it --rm -p 8000:8000 api_image
```
### Run
```commandline
uvicorn api:app --port 8000 --reload
curl http://127.0.0.1:8000/
```