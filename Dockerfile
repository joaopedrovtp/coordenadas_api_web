FROM python:3.8
ADD . /coordenadas_API
WORKDIR /coordenadas_API
RUN pip install -r requirements.txt
CMD ["python","app.py"]