FROM python:3.11

WORKDIR /DogBreedAPI

# copy requirements file into dogapp directory
COPY requirements.txt /DogBreedAPI/


RUN pip install -r requirements.txt

EXPOSE 8000
# copy project files into container app directory
COPY ./webservices/ /DogBreedAPI/

CMD ["sh","./run.sh"]

