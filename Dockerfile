FROM orgoro/dlib-opencv-python:latest

WORKDIR /usr/src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/src

EXPOSE 5000

RUN ["python3", "app/create_db.py"]
