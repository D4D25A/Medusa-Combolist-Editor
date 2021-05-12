![](img/medusa-transbg.png)

## An advanced multi-function combolist editor written in one python file.
*Medusa is a proof-of-concept multi-function advanced combolist editor which has a variety of editing features.*   
***Medusa has been officially deprecated as of January 15, 2021***

![](img/medusa-localui.png)

### Information
Medusa is a fully-fledged advanced combolist editor that is able to take advantage of a variety of combolist edit options. It supports a SOCKET connection to a remote editor client.

### Current issues
- Need a lot of cleanup
- Is single-threaded
- Poor memory optimization - may result in a MemoryError exception depending on memory available and the size of the combolist
- It uses a (local) auth server to run because I left code from when Medusa was going to be sold

### Quick start guide for Medusa 
**1. Authentication Server (required)**  
Run ```pip3 install -r ./server/auth/requirements.txt```  
then ```python3 ./server/auth/auth.py```  
(keep this running when using the client)

**2. Medusa Client**  
Run ```pip3 install -r ./windows/requirements.txt``` or ```pip3 install -r ./macos/requirements.txt```  
then ```python3 ./windows/windows.py``` or ```python3 ./macos/macos.py```

**3. Remote Editor Server (optional)**  
Run ```pip3 install -r ./server/editor/requirements.txt```
then ```python3 ./server/editor/editor.py```  
(set to default to run on 127.0.0.1, port 34280)
