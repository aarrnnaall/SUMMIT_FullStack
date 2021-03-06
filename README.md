#Requirements:
	
	* sudo apt install python3
	* sudo apt install python3-pip
	* sudo apt install nodejs
	* sudo apt install npm
	* sudo snap install docker
	* sudo snap install kubectl --classic
	* curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
	* sudo install minikube-linux-amd64 /usr/local/bin/minikube

#Create Database:

	CREATE DATABASE `Summit;
	user Summit;
	CREATE TABLE `tbl_user`(user_id` bigint(20) NOT NULL AUTO_INCREMENT,user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,user_fullname` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,PRIMARY KEY (`user_id`))ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#Run Back-end:

	* pip3 install -r requirements.txt
	* python3 main.py

#Run Frond End:

	* npm install
	* npm start

#Run Docker Back End:

	* docker build -f Dockerfile -t backend_flask:latest .
	* docker image ls
	* docker run -p 5001:5000 backend_flask

#Run Docker Frond End:

	* docker build -f Dockerfile -t frontend_angular:latest .
	* docker image ls
	* docker run -p 4201:4200 fontend_angular

#Run Kubernetes BackEnd y FrondEnd:

	* minikube start
	* kubectl apply -f deployment.yaml
	* kubectl get pods

**(run the commands in pwd /Frond_End y pwd /Back_End)**

#TEST API REST

**authentication**
	
	POST http://127.0.0.1:5000/api/auth
	{
	"name":"user",
	"pwd":"password"
	}
	
**adduser**

	POST http://localhost:5000/api/add
	{
	"name":"username",
	"email":"username@gmail.com",
	"pwd":"password",
    	"fullname": "fullname"
	}
**listuser**
	
	GET http://127.0.0.1:5000/api/users
	{
 	"jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoidGhpc3NlY3JldCJ9.fcTkRge5MtBonh67TXgfxJmOW0cJeOsUxLeHmDIMhiY"
	}

**user**
	
	DELETE http://127.0.0.1:5000/api/user/<id>
	{
	"jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoidGhpc3NlY3JldCJ9.fcTkRge5MtBonh67TXgfxJmOW0cJeOsUxLeHmDIMhiY"
	}

**updateuser**
	
	PATCH http://127.0.0.1:5000/api/update
	{
	"jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzbdsdsdds21lIjoidGhpc3NlY3JldCJ9.fcTkRge5MtBonh67TXgfxJmOW0cJeOsUxLeHmDIMhiY",
	"id":1,
	"name":"userupdate",
	"email":"userupdate@gmail.com",
	"pwd":"password",
	"fullname": "userfullnameupdate"
	}

**deleteuser**
	
	DELETE http://127.0.0.1:5000/api/delete/<id>
	{
	"jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoidGhpc3NlY3JldCJ9.fcTkRge5MtBonh67TXgfxJmOW0cJeOsUxLeHmDIMhiY"
	}


