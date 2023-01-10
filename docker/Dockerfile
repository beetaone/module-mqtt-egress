FROM python:3.8-slim

# create app directory to store source code and dependencies
RUN mkdir /app

# copy requirements file to install dependencies
COPY requirements.txt /app/

# install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy source code
COPY src /app/src
COPY docker/docker-entrypoint.sh /app/

# set the entrypoint for the container
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# expose the port according to the weeve spec
EXPOSE 80
