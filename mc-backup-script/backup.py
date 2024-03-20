from datetime import datetime, timedelta
import os 
from dotenv import load_dotenv
import shutil

def get_env_var():
    """
    Fucntions to retrieve environment variables.

    This function retrieves environment variables 'SRC' and 'DST' using os.getenv().

    Returns: 
        dict: A dictionary containing environment variables 'SRC' and 'DST'.
    """
    keys = ["SRC", "DST"]
    env_var = {key: os.getenv(key) for key in keys} # Retrieving environment variables

    return env_var

def zipFolder(folderName):
    """
    Function to zip a folder.

    Args:
        folderName (str): Name of the folder to be zipped.
    """
    try:
        shutil.make_archive(f"{folderName}", "zip", folderName) # Creating a zip archieve of the folder
    except Exception as e:
        print("An error occured as zip folder\n", e) # Handling errors


def createBackup(env_var, now):
    """
    Function to create backups of a source folder.

    This function creates up to three backups of the source folder specified in the environment variable 'SRC'.
    Each backup is copied to a destination folder specified in the environment variable 'DST'.
    The backups are named with a timestamp to indicate when they were created.

    Args:
        env_var (dict): A dictionary containing environment variables 'SRC' and 'DST'.
        now (datetime): Current date and time.
    """
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S") # Formatting current datetime

    dest_path = env_var["DST"]
    for i in range(1,4):
        backup_folder = f"{dest_path}/mc_server_backup_{i}_{dt_string}" # Naming the backup folder
        try:
            shutil.copytree(env_var["SRC"], backup_folder) # Copying the source folder to the backup folder
            zipFolder(backup_folder) # Zipping the backup folder
            print("Backup zipped")
            shutil.rmtree(backup_folder) # Removing the backup folder
        except Exception as e:
            print("An error occured at creating backup\n", e) # Handling errors

def old_file(filename, now):
    """
    Function to check if a file is older than 10 minutes.

    This function extracts the timestamp from the filename and compares it with the currenttime.
    If the time difference is greater than 10 minutes, it returns True.

    Args:
        filename (str): Name of the file.
        now (datetime): Current date and time.

    Returns:
        bool: True if the file is older than 10 minutes, False otherwise.
    """
    removeExt = filename.split('.')[0].split('_')
    time = "_".join(removeExt[-2:])
    file_time = datetime.strptime(time, '%d-%m-%Y_%H:%M:%S') # Extracting timestamp from filename

    time_diff = now - file_time # Calculating time difference
    ten_min = timedelta(minutes=10)
    return time_diff > ten_min # Checking if time difference is greater than 10 minutes

def houseKeep(env_var, now):
    """
    Function to perform housekeeping by removing old backup files.

    This function iterates through the files in the destination folder specified in the environment variable 'DST'.
    It checks each file's timestamp to determine if it is older than 10 minutes.
    If a file is older than 10 minutes, it removes the file.

    Args:
        env_var (dict): A dictionary containing environment variables 'DST'.
        now (datetime): Current date and time.
    """
    for file in os.listdir(env_var["DST"]):
        if old_file(file, now): # Checking if the file is older than 10 minutes.
            os.remove(f"{env_var['DST']}/{file}") # Removing the old backup file
        
    

if __name__ == "__main__":
    load_dotenv() # loading environment variables form .env file
    data = get_env_var() # Retrieving environment variables

    now = datetime.now() # Getting current date and time 

    createBackup(data, now) # Creating backups
    houseKeep(data, now) # Performing housekeeping 