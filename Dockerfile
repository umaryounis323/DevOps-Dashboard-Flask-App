FROM python:3.9-slim-bullseye
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["Python" , "app.py"]
