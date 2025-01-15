import yaml

# Load configurations
with open("configs.yaml", "r") as file:
    configs = yaml.safe_load(file)

GAME_CONFIGS = configs["Game"]
TF_CONFIGS = configs["Tensorflow"]
PHOTO_CONFIGS = configs["Photo_Analysis"]