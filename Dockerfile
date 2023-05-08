FROM orgoro/dlib-opencv-python:latest
#LABEL project=face_recognizer

#RUN adduser --disabled-password service
#RUN chown -R service:service /usr/local

#USER service
#ENV PATH="/home/service/.local/bin:$PATH"

WORKDIR /usr/src

#RUN python -m pip install
#WORKDIR /face_recognizer
# pyhcarm make it in opt/project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#RUN python -m pip install --upgrade pip \
#    && pip install poetry

#RUN pip install poetry
#
#RUN poetry config virtualenvs.create false
#
#COPY pyproject.toml .
#COPY poetry.lock .
#
#RUN poetry install --no-interaction --no-ansi --without test,dev

#COPY --chown=service:service . .
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/src

EXPOSE 5000
