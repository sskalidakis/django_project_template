FROM python:3.7-slim

RUN apt-get update && apt-get install -y netcat && apt-get install dos2unix

# User arguments on Dockerfile build - declared in the Docker-Compose file
ARG SETTINGS
ARG PORT

# create directory for the app user
RUN mkdir -p /home/django_project

# create the app user
RUN addgroup --system django_project && adduser -system django_project -ingroup django_project

# create the appropriate directories
ENV HOME=/home/django_project
ENV APP_HOME=/home/django_project/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


# Install Project requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

#Copy whole project
COPY . $APP_HOME

# chown (change owner of) all the files to the app user
RUN chown -R django_project:django_project $APP_HOME

# change to the app user
USER django_project

EXPOSE ${PORT}
RUN dos2unix config_prod/run.sh
CMD bash config_prod/run.sh
