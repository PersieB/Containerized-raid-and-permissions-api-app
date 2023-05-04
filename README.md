# Flask-Docker-App
Assuming Docker is already installed:

### 1. From your terminal, navigate to the created directory name **"Flask-Docker-App"**

`cd Flask-Docker-App`

### 2. Create a virtual environment

**Windows**

`py -3 -m venv venv`
<br>

**macOS/Linux**

`python3 -m venv venv`

### 3. Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 4 .Install all dependencies from requirements.txt file (includes Flask installation if need be)

`pip install -r requirements.txt`

### 5. Run the python script to confirm that it works locally
`python app.py`

### 6. Dockerizing the Application
#6.1 Run the command:
`docker build --tag python-docker .` to build our image

#6.2 Run image as a container
`docker images` to see the docker images

#6.3 `docker run python-docker`

#6.4 Click on the link provided to test the web application



