FROM ubuntu:latest


RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  
RUN  pip install psycopg2-binary
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
ADD . /app

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]