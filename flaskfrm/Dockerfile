FROM python:3.9-slim

RUN mkdir /crud

COPY ./app/ /crud/
RUN pip install -r /crud/requirements.txt

ENV FLASK_APP=/crud/frm.py
CMD ["flask", "run", "--host=0.0.0.0"]
