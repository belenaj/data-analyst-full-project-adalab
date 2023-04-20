-- CREATE DATA BASE

CREATE DATABASE db_ball_api;

-- CREATE TABLES

USE `db_ball_api`;

CREATE TABLE IF NOT EXISTS table_teams (
id INT NOT NULL,
abbreviation VARCHAR(255),
city VARCHAR(255),
conference VARCHAR(255),
division VARCHAR(255),
full_name VARCHAR(255),
`name` VARCHAR(255),
PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS table_games (
id INT NOT NULL ,
`date` VARCHAR(255) ,
home_team_score INT ,
period INT ,
postseason VARCHAR(255) ,
season INT ,
status VARCHAR(255) ,
time VARCHAR(255) ,
visitor_team_score INT ,
`home_team.id` INT ,
`home_team.abbreviation` VARCHAR(255) ,
`home_team.city` VARCHAR(255) ,
`home_team.conference` VARCHAR(255) ,
`home_team.division` VARCHAR(255) ,
`home_team.full_name` VARCHAR(255) ,
`home_team.name` VARCHAR(255) ,
`visitor_team.id` INT ,
`visitor_team.abbreviation` VARCHAR(255) ,
`visitor_team.city` VARCHAR(255) ,
`visitor_team.conference` VARCHAR(255) ,
`visitor_team.division` VARCHAR(255) ,
`visitor_team.full_name` VARCHAR(255) ,
`visitor_team.name` VARCHAR(255) ,
PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS table_players (
id INT NOT NULL ,
first_name VARCHAR(255),
height_feet VARCHAR(255),
height_inches VARCHAR(255),
last_name VARCHAR(255),
position VARCHAR(255),
weight_pounds VARCHAR(255),
`team.id` INT,
`team.abbreviation` VARCHAR(255),
`team.city` VARCHAR(255),
`team.conference` VARCHAR(255),
`team.division` VARCHAR(255),
`team.full_name` VARCHAR(255),
`team.name` VARCHAR(255),
PRIMARY KEY (id));