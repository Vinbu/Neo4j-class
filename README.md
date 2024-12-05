# Neo4j-class
This is a little practical example of how to use basic commands in python for graph databases in Neo4j.  
>[!TIP]
>To see the documentation of Neo4j press the next link: [Neo4j documentation](https://neo4j.com/docs/)  
## Index
1. [Introduction](#introduction)
2. [Installing](#installing)
3. [Docker](#docker)
## Introduction
First you have to register into [Neo4](https://login.neo4j.com/u/signup/identifier?state=hKFo2SBUeVZ5NzlobHZoQ3lqZjFpeURBYW5QNFYzd2szMGNVM6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIC1yZFdBeWQ1ZjBCX2pUcVBxTkQxQUJveTFaTzNXdUtzo2NpZNkgV1NMczYwNDdrT2pwVVNXODNnRFo0SnlZaElrNXpZVG8) page and accept the Terms and Conditions. Then you have to click on AuraDb Free, copy in a safe place the code what is generated, and when it´s done the instance creation, will be downloaded a txt file, wich have your credentials.  
This is gonna create an instance, what it means that it generating the database, which its a remote access database. Click on "open" to connect to the database, where you have to copy the user and password wich is in the txt file. Copy the protocol and Connection URL.  
## Installing
>[!TIP]
>It is recommendable to use Visual Studio Code to this project
>If you need to install it go to the next link: [Visual Studio Code](https://code.visualstudio.com/)


>[!IMPORTANT]
>You have to install Docker Desktop to this project, so go to the next link based in your Operative System:  
>[Docker Windows](https://docs.docker.com/desktop/install/windows-install/)  
>[Docker Linux](https://docs.docker.com/desktop/install/linux/)  
>[Docker Mac](https://docs.docker.com/desktop/install/mac-install/)


After clone the project you have to copy your user, password and protocol concatanate to Connection URL, into the neo.env archive that is in the src folder.  
```env
neo_user=<your_user>
neo_password=<your_password>
neo_url=<protocol+ConnectionURL>
```

## Docker
So open Docker Desktop and then you have to go to the project directory from your device or IDE terminal, specifically to the /docker folder.
If you are in the project clone directory you should write something like this:
```bash
cd NEO4j-CLASS/docker
```
Then, in the docker directory write the next commands:
```bash
docker-compose build
docker-compose up
```
It will raise the docker container.
Now open another terminal, it's no matter from what directory, and write the next code to open a bash of your image:  
```bash
docker exec -it docker-neo4j_image-1 /bin/bash
```
You should see something similar to this:
```bash
root@abcdefg:/neo4j#
```
It means that you are already in your bash image system. Now you are ready to go to Use.
## Use
Ready! Now go to the [scripts](scripts.md) file to know how to run the commands.