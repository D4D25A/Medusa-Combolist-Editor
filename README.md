![](img/medusa-transbg.png)

## A advanced multi-function combolist editor written in one python file.
*Medusa is a proof-of-concept multi-function advanced combolist editor which has a variety of editing features.*

![](img/medusa-mainui.png)

Medusa is a fully-fledged advanced combolist editor that is able to take advantage of a variety of combolist edit options. It supports a SOCKET connection to remote a remote editor client. This is a proof-of-concept program.

![](img/medusa-localui.png)

## Quick start guide for Medusa 
**Universal - Authentication Server (required)**  
Run ```pip3 install -r ./server/auth/requirements.txt```  
then ```python3 ./server/auth/auth.py```  
(keep this running in one terminal window)

**Universal - Medusa Client**  
Run ```pip3 install -r ./windows/requirements.txt``` or ```pip3 install -r ./macos/requirements.txt```  
then ```python3 ./windows/windows.py``` or ```python3 ./macos/macos.py```

**Windows Host - Remote Editor Server (optional)**  
Run ```pip3 install -r ./server/editor/requirements.txt```
then ```python3 ./server/editor/editor.py```  
(set to default to run on 127.0.0.1, port 34280)