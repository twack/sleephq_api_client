# File: new_file_trigger.py
# Description: This module checks for new files in the file store directory and calls the callback function to process the file.

import os
import time
import threading
import json
import logging
import inspect
import constants

logger = logging.getLogger(__name__)

class FileTrigger:
    def __init__(self, directory, callback):
        self.directory = directory
        self.callback = callback
        self.stop_event = threading.Event()
        self.initial_files = self.get_all_files(self.directory)

    def get_all_files(self, directory):
        return set(
            os.path.join(dirpath, filename)
            for dirpath, dirnames, filenames in os.walk(directory)
            for filename in filenames
            if filename != 'inventory.json'
        )

    def check_new_files(self):
        while not self.stop_event.is_set():
            time.sleep(constants.CHECK_FREQ)  # Wait for some time to check again, defined in the constants.py file
            
            current_files = self.get_all_files(self.directory)

            # Check for new files
            logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Checking for new files...")         
            
            new_files = current_files - self.initial_files
            if new_files:
                for file in new_files:
                    # Skip inventory.json files
                    if 'inventory.json' in file:
                        continue

                    # Use the subdirectory folder name to determine the file type
                    file_type = os.path.basename(os.path.dirname(file))
                    
                    # Check if the file has been put in the inventory. If not, add it to the inventory and process it
                    inventory_file = os.path.join(os.path.dirname(file), 'inventory.json')                 
                    file_name = os.path.basename(file)
                    if os.path.isfile(inventory_file):
                        with open(inventory_file, 'r') as f:
                            inventory = json.load(f)
                    else:
                        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Creating new inventory file for {file_type}")
                        inventory = []

                    # Check the file size
                    file_size = os.path.getsize(file)
                    if file_size < constants.MINIMUM_RING_FILE_SIZE:
                        # Add the file to the inventory list
                        inventory.append(file_name)
                        with open(inventory_file, 'w') as f:
                            json.dump(inventory, f)
                        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> {file_name} Added to Inventory.")
                    else:
                        # Check the file age
                        file_age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(file))
                        if file_age < timedelta(seconds=constants.FILE_SETTLE_TIME):
                            # Skip the file
                            continue
                        else:
                            if file_name not in inventory:
                                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Found new file of type: {file_type}")
                                # call back to the main program for further processing of the file
                                self.callback(file=file, file_type=file_type)
                                # Add the file to the inventory
                                inventory.append(file_name)
                                with open(inventory_file, 'w') as f:
                                    json.dump(inventory, f)
                                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> {file_name} Added to Inventory and processed.")
    
    
    # Start the thread to check for new files
    def start(self):
        self.thread = threading.Thread(target=self.check_new_files)
        self.thread.start()

    # Stop the thread
    def stop(self):
        self.stop_event.set()
        self.thread.join()