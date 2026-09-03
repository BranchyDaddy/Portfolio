FROM python:3.13.1

RUN pip install pandas scikit-learn explainerdashboard

WORKDIR /app

COPY eda.py model.py app.py ./
COPY abalone.csv ./

RUN python eda.py && python model.py

EXPOSE 9050

CMD ["python", "app.py"]