# Install

ssh into the EC2 terminal:

## Dependencies

- sudo yum install python36
- curl -O https://bootstrap.pypa.io/get-pip.py
- python3 get-pip.py --user
- sudo yum install git

## Get repo in EC2

- git clone https://github.com/Davidcparrar/DS4_FinalProject.git
- cd DS4_FinalProject
- pip3 install -r requirements.md
- nohup python3 app.py &
- cat nohup.out --> check for errors

## Enjoy!
