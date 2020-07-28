import os
project_folder = './Sklearn'
os.makedirs(project_folder, exist_ok=True)

# copy the training script into project directory
import shutil
shutil.copy('train_iris.py', project_folder)