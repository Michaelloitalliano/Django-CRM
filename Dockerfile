FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PROJECTDIR /usr/src/app

WORKDIR ${PROJECTDIR}

# COPY Pipfile Pipfile.lock 
COPY requirements.txt ./

RUN pip install -r requirements.txt
# RUN pip install pipenv

# RUN pipenv install --system --deploy