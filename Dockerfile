FROM python:3.12
RUN pip install kopf python-kasa
COPY src/* /src/
ENTRYPOINT [ "kopf" ] 
CMD ["run", "/src/handler.py", "--verbose"]