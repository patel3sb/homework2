FROM python:3-onbuild

RUN pip install --upgrade pip

CMD ["python", "./homework2.py"]
