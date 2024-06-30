FROM python:3.12

# Install Poetry
RUN pip install poetry
LABEL MAINTAINER="Aqadirsamdani@gmail.com"

# Set the working directory
WORKDIR /code

# Copy the project files
COPY . /code/
COPY ./helloworld /code/helloworld/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Run the FastAPI app using uvicorn
CMD [ "poetry","run","uvicorn","helloworld.main:app","--host","0.0.0.0" ]