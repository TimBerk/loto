FROM python:3.7.7-slim

WORKDIR /project

COPY core /project/core
ADD ./main.py /project
ADD ./requirements.txt /project

RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]