## Windows:
### python3.9
###### /todos
```
# Make and install environment
python -m venv .venv
.venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install fastapi
pip freeze > requirements.txt

# Create env from file
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
# Docker
###### /todos
```
docker build -t getting_started .
docker build -t api api/Dockerfile
docker run -it getting_started
```