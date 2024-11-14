FROM python:3.9-slim

RUN mkdir /crud

COPY ./app/* /crud/
RUN pip install -r /crud/requirements.txt

CMD ["python", "/crud/frm.py"]
