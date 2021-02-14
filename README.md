# game-nation
A game server project with python and js
Python as front-end client and node.js as backend server.
Using socket.io to communicate between the two.

## Dev Environment setup 
Requirements: 
    * python3 (3.9.0) and pip (20.1.1)
    * npm (6.14.8)
    * (specific versions may not be required)

Instructions may vary for Windows and MacOS

### Get the source
1. Fork this repo
    (use github web portal)
2. Clone your repo to your local computer. (Let's say /home/you/git/game-nation)
    ```
    git clone https://github.com/code-mentoring/game-nation.git
    ```
2. Navigate to your new project folder (/home/you/git/game-nation)
    ```
    cd /home/you/git/game-nation
    ```
    You should see at least some "test-*" files and README.md

### Install Virtualenv and Socketio
3. Get virtualenv (this will help isolate installations to be project specific)
    ```
    pip install virtualenv
    ```
4. Create a virtual environment for this project (use path to your python)
    ```
    virtualenv -p /usr/bin/python3 .
    ```
    You should see new directories bin and lib now in your project dir.
5. Activate your virtual env (once activated installations will be local to this folder)
    ```
    source bin/activate
    ```
6. Install socketio for python (server, client and dependencies)
    ```
    pip install python-socketio
    pip install python-socketio[client]
    pip install eventlet
    ```
7. Test your python server:
    ```
    python3 test-server.py
    ```
    You should see something like:
    ```
    SERVER: (96370) wsgi starting up on http://0.0.0.0:5000
    ```
8. Test your python client (Leave the server running, then from another terminal, same project dir):
    ```
    source bin/activate 
    python3 test-client.py
    ```
    You should see something like:
    ```
    CLIENT: connection established
    SERVER: (96370) accepted ('127.0.0.1', 60006)
    ```
9. If all looks okay you can kill the client and server
    ctrl-C (on CLI usually)

### Install npm express and socket.io (still in project dir)
9. Install socket io and express
    ```
    npm install socket.io
    npm install express
    ```
11. Test server
    ```
    node test-server.js
    ```
    From your browser, enter "localhost:5000" in address bar. 
    ```
    BROWSER: "hello world"
    SERVER: "a user connected"
    ```
12. Test python client with js server (from same location in another terminal,
Again from your project directory with activated virtual environment)
    ```
    python3 test-client.py
    ```
    ```
    CLIENT: "connection established"
    SERVER: "a user connected"
    ```
13. Cool, looks like you have (a very simple) python client application talking to a javascript server via socketio.
    

