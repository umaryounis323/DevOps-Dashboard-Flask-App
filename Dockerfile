FROM python:3.12-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["Python" , "app.py"]
