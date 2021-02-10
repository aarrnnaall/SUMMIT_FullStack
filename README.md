Requirements:
+sudo apt install python3
+sudo apt install python3-pip
Create Database:
CREATE DATABASE `Summit`;
user Summit;
CREATE TABLE `tbl_user` (
`user_id` bigint(20) NOT NULL AUTO_INCREMENT,
`user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
`user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
`user_fullname` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
Run Back-end:
+pip3 install -r requirements.txt
+python3 main.py
Frond End:
+npm install
+npm start
