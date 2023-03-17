FROM python:3.10-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /REST/
WORKDIR /REST
# RUN apt update -y
# RUN apt upgrade -y # do not update because it is already with the exact dependencies
# RUN apt update -y  # required to run django==4 properly
RUN pip install --upgrade pip
RUN pip install -r /REST/requirements.txt
RUN chmod +x /REST/start.sh
