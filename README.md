## Detection Instructions
### Download dataset
Download a pretrained model from https://datasetcolab.com/models. Download the model for YOLOv5n and place it in the data folder.

### Create virtual environment for Python
```
pip3 install virtualenv
python3 -m virtualenv env
```

Ctrl + Shift + P, search for and select "Python: Select Interpreter", select ./env/bin/python  
### Install Python dependencies
```
pip3 install -r requirements.txt
```
### Run detection
```
python3 detect.py
```
Run Ctrl + C to cancel

## Set up systemd service on vision processor
### Install Java
`sudo apt install openjdk-11-jdk`  

### Set up PhotonVision as a systemd service
Copy photonvision.service to `/etc/systemd/service/`  
run `sudo systemctl daemon-reload` to integrate the new service file  
run `sudo systemctl enable photonvision` to cause PhotonVision to start at boot  
run `sudo systemctl status photonvision` to check to see if PhotonVision is running

### Open photonvision
Photonvision will listen for HTTP on port 5800. Try going to http://photonvision:5800 or http://\<IP Address of processor\>:5800
