FROM python:latest
WORKDIR /python-docker
COPY app.py /python-docker
RUN pip3 install Flask
RUN pip3 freeze | grep Flask >> requirement.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
