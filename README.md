# Stream2-Project

## Overview

### What is this site for?

This is a dashboard for an election campaign in Arkansas for a candidate who wishes to highlight the lack of school funding in the state.
.
### What does it do?

The website will allow users to view interactive graphs which pull data from a MySQL database

### How does it work?

This site will use MySQL for the database, Python, CSS, HTML and for the graphs Crossfilter, D3 and DC.

## Features

### Existing Features
	- Home page
  - Graph page with bar graph, pie chart and a drop down menu to select different states

## Tech Used

### Some the tech used includes:
- [Crossfilter]
    - We use **Bootstrap** to give our project a simple, responsive layout

## Contributing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** and **bower** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
  2. Once you've done this you'll need to run the following command:
     `npm install -g bower # this may require sudo on Mac/Linux`
3. Once **npm** and **bower** are installed, you'll need to install all of the dependencies in *package.json* and *bower.json*
  ```
  npm install
 
  bower install
  ```
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request
