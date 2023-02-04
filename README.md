$ mkdir fastapi-demo

$ cd fastapi-demo

$ conda create -p venv

$ conda activate venv/

$ touch readme.md

$ pip install fastapi uvicorn

$ mkdir src && cd $_

$ touch __init__.py main.py

$ cd ..

$ uvicorn src.main:app --reload #execute main.py

$ touch Dockerfile

$ pip freeze>requirements.txt

$ docker build -t fastapi-demo

$ docker run -dp 8000:8000 fastapi-demo

#navigate to the .pem key
$ chmod 400 fastapi-deploy.pem

$ ssh -i "fastapi-deploy.pem" #ec2

#u should be inside ur EC2 instance

#install docker on EC2

[ec2-user@ip-172-31-5-6 ~]$ sudo yum update -y

[ec2-user@ip-172-31-5-6 ~]$ amazon-linux-extras install docker

[ec2-user@ip-172-31-5-6 ~]$ sudo amazon-linux-extras install docker

[ec2-user@ip-172-31-5-6 ~]$ sudo service docker start

[ec2-user@ip-172-31-5-6 ~]$ sudo usermod -a -G docker ec2-user

$exit


