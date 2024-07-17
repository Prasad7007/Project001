import os
import logging
from datetime import datetime

# Set the root directory manually
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
log_directory = os.path.join(root_dir, 'logs')

# Create the directory if it does not exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the log file name with the current timestamp
log_filename = os.path.join(log_directory, datetime.now().strftime("%m_%d_%Y_%H_%M_%S.log"))

# Configure logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
