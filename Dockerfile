FROM python

WORKDIR /srv/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
