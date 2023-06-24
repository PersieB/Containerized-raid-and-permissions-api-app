# Description
The web application was deployed using docker and contains the following APIs:

/permissions?code=<number>
This API method accepts a code given by number and returns a JSON object specifying the permissions represented for owner, group and other. E.g., The request /permissions?code=744 should return. 

{owner: [read, write, execute], group [read], other:[read]}.

/parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>
This API method accepts the bits on corresponding disk blocks of a RAID-4 and returns the parity bits. Assume that each block has two bits. E.g., The request /parity?b1=00&b2=10&b3=11&b4=10 should return 11.

# Running the web application
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



