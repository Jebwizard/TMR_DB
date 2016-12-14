TMR Database README
Decemner 14, 2016
By: Joel Bassett

Purpose:
This database is implemented in Python to use MongoDB to receive TMR structures from the OntoSem
    website and store these structures. These structures can then be retrieved with MongoDB for
    the use of analyzing the Ontology system.

Requirements:
(All Instructions are written for Windows 7 Users. I will update this as I know what works for other systems)
-Python
    index.py
-MongoDB
    Download the community edition at this website:
        https://www.mongodb.com/download-center#community
    You will be running mongo.exe to access the database and mongod.exe to run the database
-OntoSem TMR Project
    Download from GitHub at:
    https://github.com/ethanbond/ontosem
    Contact Chris or Ross if you have issues with this system

Capabilities:
Recieve TMRs through HTML POST requests
Convert the POST requests into Python Dictionaries
Insert the Dictionary into MongoDB
Retrieve all previously stored TMRs from the database

Instructions:
1- Start mongod.exe
    This starts the MongoDB. This will open a terminal window. Closing this window will
        terminate the database. Leave this window open till you are done with the server.
    The contents of the database are preserved between sessions.
2- Start OntoSem server
    This must be on your local machine. Refer to the OntoSem Readme.
    Most likely this will require you to open 2 terminal windows and use the following 2 commands:
        npm run scss
        npm run start
3- Navigate your browser to localhost:3000
4- Run index.py
    Install pymongo through pip.
    I believe all of the required packages except pymongo come with Python.
    If not, here is the list of packages that are imported:
        web
        collections
        pymongo
        json
        ast
        pprint
    
    Index.py will start a server on your machine. Leave this terminal window open.
    The output from POST requests will appear here.
    
    Make a note of the URL address that appears at the top of this window.
    This is the address of the python server.
    
    If your browser opens a new tab, ignore it.
    (This might be an issue with my configurations in Microsoft Visual Studio)
    
5- In the OntoSem site, paste the TMR you want to store. Then click the "TMR" button.
6- On the next screen, find the TMR you want to mark as the Gold TMR.
    Click the GOLD button next to it.
7- A window will open. In the text field labeled "Put destination address here" put 
    the address of the python server. you can replace "0.0.0.0" with "localhost."
    For example: Inputing "http://localhost:8080/" or "http://0.0.0.0:8080/" 
        will result in the TMR being sent to the python server.
    Click "Submit" to send the TMR.
    You can close the small window now.
8- In the python server window, you will see various output showing what the server
    received and how it manipulated it.
    There will also be a print out of the entire database.
9- To search the database or manipulate it, you much use mongo.exe and the database
    specific commands found here:
    https://docs.mongodb.com/v3.2/reference/mongo-shell/


To Dos:
Add a web interface to allow the user to add TMRs to the database.
Add a way for the user to retrieve the TMRs without using the mongo shell.