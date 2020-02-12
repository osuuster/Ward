FROM python:3-alpine

MAINTAINER Oliver Suuster

WORKDIR C:\Users\Administrator.DESKTOP-NTBIGRE\Google Drive\Ward

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]