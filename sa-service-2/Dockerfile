FROM python:3.6.6-alpine
COPY src /app/src
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["src/main.py"]
