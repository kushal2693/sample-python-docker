FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD hello.py /
CMD [ "python", "./hello.py" ]
