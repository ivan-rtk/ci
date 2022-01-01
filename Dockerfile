FROM python:3

WORKDIR /library

COPY . .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/library/entrypoint.sh"]