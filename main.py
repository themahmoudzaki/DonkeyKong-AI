import yaml
import os
import time
import shutil
import pyautogui
import cv2
import numpy as np
import pygetwindow as gw
import tensorflow as tf

# Load configurations
with open("configs.yaml", "r") as file:
    configs = yaml.safe_load(file)

GAME_CONFIGS = configs["Game"]
TF_CONFIGS = configs["Tensorflow"]
PHOTO_CONFIGS = configs["Photo_Analysis"]

# Configure TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = TF_CONFIGS["log_level"]
physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)


def main():
    print("\n____________+____________+____________+____________+____________+____________+____________\n")
    print("Program Initiated\n")
    setup_game()

    snapshot_frame_counter = 1
    screen_width, screen_height = pyautogui.size()

    # To be honest I pulled these numbers straight out of my ass
    x = int (0.15625 * screen_width)
    width = int (screen_width - ( 0.2604 * screen_width ))
    y = int (0.03704 * screen_height)
    region = (x, y, width, screen_height)
    print(f"snapshot region: \n{region}")
    try:
        while True:
            snapshot_path = capture_snapshot(snapshot_frame_counter, region)
            analyse_snapshot(snapshot_path)
            snapshot_frame_counter += 1
    except KeyboardInterrupt: print("\nProgram Stopping")
    print("\n____________+____________+____________+____________+____________+____________+____________\n")


def setup_game():
    """Sets up the game environment and launches the emulator."""
    emulator_folder = GAME_CONFIGS["Paths"]["folder"]
    emulator_path = GAME_CONFIGS["Paths"]["emulator"]
    recent_games_path = GAME_CONFIGS["Emulator_State"]["RecentGames_Path"]
    save_states_path = GAME_CONFIGS["Emulator_State"]["SaveStates_Path"]

    """Validates and initializes the game state if necessary."""
    recent_game_dir = os.path.join(emulator_folder, "RecentGames")
    save_state_dir = os.path.join(emulator_folder, "SaveStates")

    if not os.path.exists(recent_game_dir) or not os.path.exists(save_state_dir):
        shutil.rmtree(recent_game_dir, ignore_errors=True)
        shutil.rmtree(save_state_dir, ignore_errors=True)
        shutil.copytree(recent_games_path, recent_game_dir)
        shutil.copytree(save_states_path, save_state_dir)
    
    os.startfile(emulator_path)
    time.sleep(1)
    print("\nGame Started")

    emulator_window = gw.getWindowsWithTitle('Mesen')[0]
    emulator_window.activate()
    emulator_window.maximize()
    time.sleep(0.1)
    pyautogui.click()
    print(f"Focused on Game window \n{emulator_window}")




def capture_snapshot(snapshot_frame_counter, snap_region):
    """Captures a screenshot and saves it to the configured photo folder."""
    photo_folder = PHOTO_CONFIGS["Path"]["folder"]
    snapshot_path = os.path.join(photo_folder, f"snapshot_{snapshot_frame_counter}.jpeg")

    snapshot = pyautogui.screenshot(region=snap_region)
    snapshot = np.array(snapshot)
    snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{snapshot_path}", snapshot)

    print(f"\nScreenshot saved at \n{snapshot_path}")

    return snapshot_path


def analyse_snapshot(snapshot_path):
    # Will give the image to the AI model
    return

if __name__ == "__main__":
    main()
