# gunicorn-flask

FROM python:3.6-stretch 
MAINTAINER Daniel Riti <dmriti@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
#RUN apt-get install -y python python-pip python-virtualenv gunicorn

# Setup flask application
RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN pip install -r /deploy/app/requirements.txt
WORKDIR /deploy/app

# Start gunicorn
#CMD ["ddtrace-run","/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "--statsd-host","${DATADOG_TRACE_AGENT_HOSTNAME}:${DATADOG_STATSD_AGENT_PORT}", "hello:app"]
#CMD ["/bin/bash","-c","ddtrace-run /usr/bin/gunicorn --config /deploy/gunicorn_config.py --statsd-host ${DATADOG_TRACE_AGENT_HOSTNAME}:${DATADOG_STATSD_AGENT_PORT} hello:app"]
#CMD ["/bin/bash","-c","/usr/bin/gunicorn --config /deploy/gunicorn_config.py hello:app"]
CMD ["gunicorn", "--config", "/deploy/gunicorn_config.py",  "hello:app"]
#CMD ["ddtrace-run","/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "hello:app"]
