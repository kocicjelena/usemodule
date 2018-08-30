FROM python:3
RUN python setup.py install
ADD test.py /
CMD [ "python", "./test.py" ]
