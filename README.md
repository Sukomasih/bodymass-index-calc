# Instruction running bmi calculator rest api
## Python
### Install python 3
- Install python 3 : [link](https://www.python.org/downloads/) \
just skip it, if python 3 already exists
### Running app
- `python3 -m venv bmi-cal` \
Create virtualenvirement in python
- `source bmi-cal/bin/activate` \
Running virtualenvirement
- `pip install -r requirements.txt` \
Install module requirements in python 
- `uvicorn main:app --host=0.0.0.0 --port=80 --reload` \
Running app bmi claculator rest api

### Stop app
- `ctrl + c`
- `deactivate`

Endpoint rest api : \
`http://localhost/?height=170&weight=50`

## Docker 
### Install docker
- Install docker : [link](https://docs.docker.com/engine/install/) \
just skip it, if docker already exists
### Running image container
- `docker build -t bmi-cal:bmi .` \
Building image container proses
- `docker run --name bmi -p 80:80 bmi-cal:bmi` \
Running image after build
### Stop dan remove image container
- `docker rm -f bmi`

Endpoint rest api : \
`http://localhost/?height=170&weight=50`