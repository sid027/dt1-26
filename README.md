# DT1 2026 : Enabling Technologies, Assignment 1

The assignment description and requirements are on Moodle.

## Introduction
The small flask application presented here is a proxy that we use to interact with OpenRouter API.
Your job is to deploy and interact with OpenRouter API using this proxy. The interface will be built
using Streamlit. </br></br>
This assignment covers the first 3 learning cycles:
- Software Architecture
- API Design
- Cloud Computing

Different aspects of the assignment covers all the three cycles. Please go back to the lecture materials
in case there is something you don't understand. In addition, we provide materials here that we believe
will act as hints for successfully completing the assignment.

**NOTE: The code has been developed and tested on Ubuntu (Debian)/MacOS. You will be using Ubuntu on the Google 
Cloud Platform. For local testing, you might need to find the appropriate information and corresponding adjustments.**

## Codebase
- api.py: contains all the code for the api layer including the API routes
- frontend.py: the user interface that you that users can interact with
- Pipfile, Pipfile.lock: dependency file for running the codebase
- 2 Dockerfiles: docker build configuration for the api and frontend
- compose.yaml: docker compose file to start and stop docker images
- .env_example: the environment variables you will need in the .env file you should create locally (compose.yaml expects this)

## Supplementary Materials
### Software Architecture
- You can use TLDraw for diagramming: https://www.tldraw.com/ [you can use any other tool if you prefer, like LucidCharts, Miro etc.]
### Streamlit
Here is something to get you started: https://dev.to/niveshbansal07/streamlit-beginner-guide-with-examples-317d
### API Design
- Curl for testing your docker container locally: https://daniel.haxx.se/blog/2021/05/31/curl-localhost-as-a-local-host/
### Cloud Computing
- Installing Docker on Debian: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10
- You can use ```sudo passwd``` to set the password once you login to your GCP VM.
- Dockerize your application: https://docs.docker.com/get-started/02_our_app/
- Run Dockerfile: https://www.datacamp.com/tutorial/run-a-docker-image
- Docker image to Docker Hub: https://docs.docker.com/get-started/04_sharing_app/
- Firewall Rules on GCP: https://www.howtogeek.com/devops/how-to-open-firewall-ports-on-a-gcp-compute-engine-instance/
- In case you would like to work using your local terminal: https://cloud.google.com/sdk/docs/install-sdk#linux
- Docker Compose: https://betterstack.com/community/guides/scaling-docker/docker-compose-getting-started/