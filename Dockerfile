FROM python:3.9-slim

# working directory in container
WORKDIR /app

# non-root user called "siya" creation to run app
RUN adduser --disabled-password --gecos "" siya

# copy script into container
COPY app.py .

# giving ownership of the script file to siya
RUN chown siya:siya app.py

# switching to user
USER siya

# run the script when container starts up
CMD [ "python", "app.py" ]

