# Trasaterra GPT Local Flask Dev Environment Setup :
### Steps:
<ol>
<li> Create a directory for your project<code>cd</code> into the directory</li>
<li>Start a virtual environment: <code>python venv venv</code></li>
<li>Activate virtual environment: <code>source venv/bin/activate</code>(Mac)</li>
<li>Choose the interpreter in for the venv. in VS Code it is often the 
'recommended' choice</li>
<li>Create first file:<code>main.py</code></li>
<li>Add a flask basic route to start test. https://flask.palletsprojects.com/en/3.0.x/quickstart/
</li>
<li> Run application: <code>python -m flask --app ./main.py run</code></li>
<li> Install ngrok:<code>brew install ngrok/ngrok/ngrok</code></li>
<li> Add Auth token: 
<code>ngrok config add-authtoken 2ZYQoVIDN3m0f4YgkOfEcZx7QvZ_2WmKfL3YFYVsXAhhZHmSj</code></li> 
<li> Spin up ngrok to expose endpoints: 
While applciation is running open new 
bash terminal and type the following <code>ngrok http 5000</code></li> 
</ol>

***

### Commands: 
#### Turn On Environment: 
<code>source venv/bin/activate</code>

#### Upgrade pip: 
<code>python -m pip install --upgrade pip</code>

#### Install Deps:
<code>pip install flask</code>

#### Verify Install:
<code>pip list</code>

#### Deactivate venv:
<code>deactivate</code>

#### Run application: 
<code>python -m flask --app ./main.py run</code>

#### Run Ngrok
<code>ngrok http http://localhost:5000</code>

***

# App dependency list:

<ul>
    <li>python = ">=3.10.0,3.11"</li>
    <li>flask = "^3.0.0"</li>
    <li>functions = "^0.7.0"</li>
    <li>openai = "^1.2.3"</li>
    <li>packaging = "^23.2"</li>
    <li>requests = "2.31.0"</li>
    <li>prompt = "^0.4.1"</li>
</ul>

### PIP Install
<ul>
    <li>pip install flask</li>
    <li>pip install functions</li>
    <li>pip install openai</li>
    <li>pip install packaging</li>
    <li>pip install requests</li>
    <li>pip install prompt</li>
</ul>


***

### Useful Resources:

Expose Local web server to internet with flask app: 
https://sumanshunankana.hashnode.dev/expose-a-local-web-server-to-the-internet-example-flask-app

How to create a simple flask app in just 5 minutes: 
https://youtu.be/6M3LzGmIAso?si=ndAo_d_NFOwbkFig

Python Boilerplate for .gitignore:
https://www.python-boilerplate.com/about/

Ingress Platfor for Devs: Expose endpoints for VF 
(2FA required) 
https://ngrok.com/

Start applciation over from scratch commit: 
<code>commit 27b9d995f30bd6a98d150bf0f39bc762fb04a315</code>

***

### Ngrok Info: 

#### Install Ngrok
<code>brew install ngrok/ngrok/ngrok</code>

#### Run Auth Token: 
<code>ngrok config add-authtoken 2ZYQoVIDN3m0f4YgkOfEcZx7QvZ_2WmKfL3YFYVsXAhhZHmSj</code>

#### Response: 
<code>Authtoken saved to configuration file: /Users/jamesahnking/Library/Application Support/ngrok/ngrok.yml</code>

