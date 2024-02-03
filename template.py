import os
from pathlib import Path
import logging      #To log th information during runtime

## Creating login screen
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "Text_Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",  ## Will be used for CI/CD deployment. If code is committed to github, this line will automatically take the code from github and will deploy it on cloud.
    f"src/{project_name}/__init__.py",    ##"__init__.py is the constructor file. "               
    f"src/{project_name}/components/__init__.py",   ##Components is another local folder with constructor file.
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    ## Creating files inside the folder
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):   ## If filesize is 0 then the file gets created.
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")