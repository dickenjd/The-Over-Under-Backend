# Docker Research

## General

[Docker Basics](https://www.youtube.com/watch?v=rOTqprHv1YE) ~ 16 minutes

[Example implenting docker on node.js application](https://www.youtube.com/watch?v=gAkwW2tuIqE)

## Why and how?
- allows developer applications to work for testing on different machines
- you can use a virtual machine, but docker is quicker and much more efficient
- easier to use accross multiple platforms (mac, windows, linux, etc.)
- creates a 'light' container with all requirements for running an application
- the 'framework' will contain **all required installs** across our entire application
- uses a REST API to manage a client to server communication (which can be programmed). the docker server will take requests from the docker client on the computer

## Keywords
- **Dockerfile:** blueprint for image
  - define environment
- **Image:** template for running docker containers
  - use dockerfile to rebuild image
  - these can be found readily avaliable online, these are what allow people to run built applications
- **Container:** running code, in our case it is our Electron application

## Requirements
### 1. [Install docker desktop](https://www.docker.com/products/docker-desktop/)
  - You may need to run the following command to update windows subsystem for linux
```cmd

wsl --update

```
  - Run this in your command terminal to see all running containers on the system:

```cmd

docker ps

```

### 2. Add docker extention in VS code
  - to write dockerfiles

### 3. Design .dockerignore file
  - same as .gitignore, little different look

## Writing Dockerfiles

[Docker Syntax for dockerfiles](https://docs.docker.com/engine/reference/builder/)

Always starts with FROM ____. In our case it will be:

```docker
FROM node
```

RUN will run ANY command. For our app we will use:

```docker
RUN npm install
```

This line installs node.

## Running an Image from Dockerfile

```cmd

docker build -t (username)/mainline-application .

```
Once this is run, the following should show in the terminal:

```cmd

PS C:\Users\joshm\OneDrive\Documents\GitHub\team-project-the-over-under-frontend\mainline_application> docker build -t mckettja/mainline-application .
[+] Building 5.7s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                               0.0s
 => => transferring dockerfile: 32B                                                                                                                                                0.0s 
 => [internal] load .dockerignore                                                                                                                                                  0.0s 
 => => transferring context: 34B                                                                                                                                                   0.0s 
 => [internal] load metadata for docker.io/library/node:16                                                                                                                         0.9s 
 => [auth] library/node:pull token for registry-1.docker.io                                                                                                                        0.0s
 => [internal] load build context                                                                                                                                                  0.1s
 => => transferring context: 1.05MB                                                                                                                                                0.0s 
 => [1/5] FROM docker.io/library/node:16@sha256:8ef06c513538040a988ac7731afa8ad8b1135cfe5d8b6ad78489d80c6f6c0137                                                                   0.0s 
 => CACHED [2/5] WORKDIR /app                                                                                                                                                      0.0s 
 => [3/5] COPY package*.json ./                                                                                                                                                    0.0s 
 => [4/5] RUN npm install                                                                                                                                                          4.4s
 => [5/5] COPY . .                                                                                                                                                                 0.0s
 => exporting to image                                                                                                                                                             0.2s
 => => exporting layers                                                                                                                                                            0.1s
 => => writing image sha256:107b1e947040c0f80798352006931fc89c31f5375f15d44a24adbf57db31b599                                                                                       0.0s
 => => naming to docker.io/mckettja/mainline-application                         

```
Check the image was created by checking the docker desktop application.

## Creating a container from an image

Run the following in your terminal after confirming the image was created from the dockerfile:

```cmd

docker run -p 5000:8080 (image id from docker desktop app)

```




