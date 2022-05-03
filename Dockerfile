FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#anytime you have a space in your run command, you split them up into different strings
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]