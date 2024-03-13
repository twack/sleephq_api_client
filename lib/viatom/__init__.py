# File: viatom/__init__.py
# Description: Custom module for the Viatom instance of the API
#
import logging
import os
import inspect
from lib.api import API

logger = logging.getLogger(__name__)

base_directory = os.path.dirname(os.path.realpath(__file__))
file_store_directory = 'file_stores'

def process_viatom_file(file):
    logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Processing file specifically for file type...") 
    
    # instantiate the API object
    api = API()
    
    try:
        file_type = 'o2'
        fname = os.path.basename(file)
        fpath = os.path.dirname(file)
        
        # get the next import id for viatom file import
        next_import_id = api.get_next_import_id(file_type)
        
        # get hash of the combined filename and file contents
        combined_hash = api.get_file_md5_hash(file)
        
        # upload the file to my sleephq account
        success = api.upload_file(fname, fpath, next_import_id, combined_hash)
        
        # if success we can tell sleephq to process the file
        if success:
            api.process_files(next_import_id)
            logger.info(f"METHOD: 'process_viatom_file: ACTION: Viatom file processed successfully.")
            logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Successfully processed Viatom file: {file}")
        return success
    
    except Exception as e:
        logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error proccessing Viatom file: {file} - {e}")
        return False