FROM python

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/hito_iv/

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD [ "hug",  "-p 80", "-f", "hug_hitos_iv.py" ]

EXPOSE 80
