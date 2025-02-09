# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install gettext tools
RUN apt-get update && apt-get install -y gettext

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8888


RUN python manage.py makemigrations
RUN python manage.py migrate

# Management commands use --help for more info 
## RUN python manage.py makemessages --help   
## RUN python manage.py compilemessages --help  

#RUN python manage.py makemessages -l se 
# RUN python manage.py makemessages
RUN python manage.py compilemessages 


# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"] 

 
