FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
