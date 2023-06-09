FROM python:3.9-slim
WORKDIR /usr/src/app
# sasme as copy
ADD . /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn api:app --port 8000 --reload