# Filename: api.py
# * Description: This module is responsible for making API requests to SleepHQ. It also handles the file upload process.
# 
import requests
import logging
import constants
import json
import inspect
import hashlib
import os
from lib.check_credentials import has_credentials

logger = logging.getLogger(__name__)

class API:
    def __init__(self):
        self.client_id     = f'{has_credentials(silent=True)["client_uid"]}'
        self.client_secret = f'{has_credentials(silent=True)["client_secret"]}'
        
        self.BASE_URL     = f'{constants.BASE_URL}'
        self.API_BASE_URL = f'{self.BASE_URL}{constants.API_VERSION}'
        self.TOKEN_URL    = f'{self.BASE_URL}/oauth/token'
        
        self.access_token = self.get_new_access_token()
        self.team_id = self.get_team_id()
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> API object initialized")
        
    def process_files(self, import_id):
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Telling SleepHQ to process files.")
        endpoint = f'imports/{import_id}/process_files'
        response = self.api_request('POST', endpoint)
        if response.status_code == 201:
            logger.info(f"[{inspect.currentframe().f_code.co_name}] >> SleepHQ sucessfully processed files.")
            return True
        else:
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error processing files: {response.status_code}")
            return False
        
    def upload_file(self, file_name, file_path, import_id, combined_hash):
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Uploading {file_name} to SleepHQ")
        endpoint = f'imports/{import_id}/files'
          
        with open(file_path + '/' + file_name, 'rb') as f:
            # file_content = f.read()
            file_content = f
            
            files = {
                'import_id': import_id,
                'name': (None, file_name),
                'path': (None, file_path),
                # 'file': (file_name, file_content),
                'file': (file_content),
                'content_hash': (None, combined_hash)
            }

            response = self.api_request('POST', endpoint, files=files)
        
        if response.status_code == 201:
            logger.info(f"[{inspect.currentframe().f_code.co_name}] >> {file_name} file uploaded successfully.")
            return True
        else:
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error uploading {file_name}, ERROR CODE: {response.status_code}")
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error description: {response.json().get('errors')}")
            return False
        
    def api_request(self, method, endpoint, params=None, data=None, files=None):
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'accept': 'application/vnd.api+json'}
            
        url = f'{self.API_BASE_URL}/{endpoint}'
        response = requests.request(method, url, headers=headers, params=params, data=data, files=files)
        return response
        
    def get_file_md5_hash(self, file_path):
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Creating combined file/name hash.")
        try:
            os.path.exists(file_path)
            fn = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                file_contents = f.read()
                combined_hash = hashlib.md5(fn.encode('utf-8') + file_contents).hexdigest() 
        except:
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error trying to create hash file: {file_path}Creating combined file/name hash.")
            return None
        
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Hash successfully created.")
        return combined_hash

    def get_new_access_token(self):
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Getting new access token...")

        scope = "read write delete"
        
        payload = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': scope,
        }
        response = requests.post(self.TOKEN_URL, data=payload)
        response.raise_for_status()
        access_token = response.json()['access_token']
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> New access token retrieved. Access token: {access_token}")
        return access_token

    def get_team_id(self):
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Finding Team ID to use...")
        try:
            if constants.TEAM_ID:
                team_id = constants.SLEEPHQ_TEAM_ID
                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Using team ID from constants.py: {team_id}")
        except AttributeError:
            try:
                team_id = os.environ['SLEEPHQ_TEAM_ID']
                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Using team ID from environment variable: {team_id}")
            except KeyError:
                # If not set in constants.py or environment variable, make the API request
                response = self.api_request('GET', 'me')
                team_id =  response.json()['data']['current_team_id']
                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Using team ID from account: {team_id}")
        
        self.team_id = team_id
        return team_id

    def get_next_import_id(self, file_type):

        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Finding next import ID to use...")
        endpoint = f'teams/{self.team_id}/imports'
        params = {file_type: True}
        response = self.api_request('GET', endpoint, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            if data:
                import_id = data[0]['id']
                logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Using import ID: {import_id}")
                return  import_id
            else:
                return None
        else:
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error getting import ID, ERROR CODE: {response.status_code}")
            logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Error description: {response.json().get('errors')}")
            print(f"Error: {response.status_code}")
            return None