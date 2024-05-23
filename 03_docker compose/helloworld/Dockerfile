FROM python:3.12
RUN pip install poetry
LABEL MAINTAINER="Aqadirsamdani@gmail.com"
WORKDIR /code
COPY ./pyproject.toml /code/
COPY ./helloworld /code/helloworld/
# RUN poetry install
CMD [ "poetry","run","uvicorn","helloworld.main:app","--host","0.0.0.0" ]