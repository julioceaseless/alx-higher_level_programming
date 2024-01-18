-- utilize more constraints

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to the database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (id)
	);
