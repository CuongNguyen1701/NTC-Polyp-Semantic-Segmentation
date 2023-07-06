
import subprocess
import os
def init(dir):
    #initiate AI model
    model_folder = os.path.join(dir, 'models')
    model_path = os.path.join(model_folder, 'polyp_model.h5')
    #In case the model is not existed(i. e. when deploying to the cloud), download it from google drive
    if not os.path.exists(model_folder):
        os.mkdir(model_folder)
    if not os.path.exists(model_path):
        subprocess.run(["gdown", "1EDyOfeEhwlYCy5YUHObj-Sfo1N8EbVxK", "-O", model_path]) 
        
    #initiate assets
    assets_folder = os.path.join(dir, 'assets')
    avatar_path = os.path.join(assets_folder, 'me.jpg')
    if not os.path.exists(assets_folder):
        os.mkdir(assets_folder)
    if not os.path.exists(avatar_path):
        subprocess.run(["gdown", "1aZ9r06lZbEa0gEngPhvXXwc6LBZ37BAz", "-O", avatar_path])
    