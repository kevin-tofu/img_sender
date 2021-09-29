
## image Sender Based on Python
### 

#### Set Up
'''
python -m venv myrequest
source activate myrequest
pip install --upgrade pip
pip install -r requirements.txt
'''

#### Settings
For sending images, just you should do is to execute below command with setting file. 
You should execute the program like below If you create 'setting.json' as settings. 
'''
python main.py --setting ./setting.json
'''
So now, you can send images to server.

How do you write the setting.json file? 
Just fulfill some variables in an form below along with json-form.
'''
---setting.json

{
    "URL": "",
    "TOKEN": "",
    "COLLECTION_NAME":"",
    "DIR_IMAGES": "",
    "RECURSIVE": true
}
'''

#### Explanation of the Key in setting file
| URL | Description |
| --- | --- |
| URL | The url of image server that you are going to upload images. |
| TOKEN | a token that is required to access image server. |
| COLLECTION_NAME | a collection name where you'd like to save images. |
| DIR_IMAGES | a directory path that images are to be uploaded. |
| RECURSIVE | The url of image server that you are going to upload images|

