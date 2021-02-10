#Requirements:

* sudo apt install python3
* sudo apt install python3-pip
* sudo apt install nodejs
* sudo apt install npm

#Create Database:

	CREATE DATABASE `Summit;
	user Summit;
	CREATE TABLE `tbl_user` (
`		user_id` bigint(20) NOT NULL AUTO_INCREMENT,
`		user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
`		user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
`		user_fullname` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
		PRIMARY KEY (`user_id`)
				) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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

* kubectl apply -f deployment.yaml
* kubectl get pods

**(run the commands in pwd /Frond_End y pwd /Back_End)**
