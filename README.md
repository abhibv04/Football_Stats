# Football_Stats
This project is a comprehensive study on football statistics, comprising of all the stats related to world football today.

There are 4 files in this project:
1. main.py- This file consists of all the tables in the database.It establishes a connection with the database using the MySql connector module. It has all the statistics ranging from goals, assists to other detailed player stats. It also has triggers and DML commands to establish relationships among tables.
2. server.js- This file establishes a connection from the backend.
3. frontend_streamlit.py- This file consists of the frontend code using a Streamlit framework.
4. login_template.py- This is a login template, which can be manipulated and run before running the frontend_streamlit.py file.

Steps to run the project-
1. Create a database in the MySQL command line client or Workbench.
2. Run the main.py file. Make sure to change the database name and other credentials. Now, all the tables in the database will be populated.
3. Run the server.js file. Make sure to have the http://localhost:8081 page open before you run the server.js file. Once you run the code, a message will appear in the browser, acknowledging backend connection.
4. Data can be viewed via routes, for instance, http://localhost:8081/player_stats, which displays data from the player_stats table.
5. Run the frontend_streamlit.py file. This will redirect you to your browser and the tables can be viewed and manipulated.
6. The login_template.py file can be manipulated and run before running the frontend_streamlit.py file. The data is stored into a 'users' database, which needs to be created before running the file.

Important
 1. Make sure to create the database before running the main.py file.
 2. Make sure that Streamlit is installed.
 3. Make sure that the MySQL connector module is installed.
 4. Make sure to create the users database before attempting to run the login_template.py file
