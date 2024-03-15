# File: constants.py
# Description: This module contains the constants used in the application.

# * Typically you would set keys and secrets in environment variables to avoid hardcoding them in the code
# * But you can define them here if they are not in the environment variables
# SLEEPHQ_CLIENT_UID = "put your client uid here"
# SLEEPHQ_CLIENT_SECRET = "put your client secret here"

# * You can define the team id here if you have multiple teams
# * You can also set the team id in the environment variables
# * If not in either place, the application will get the team
# SLEEPHQ_TEAM_ID = 'put your team id here'

BASE_URL = "https://sleephq.com"
API_VERSION = '/api/v1'

FILE_STORE = "./file_stores/" # relative path to the file store directory
CHECK_FREQ = 5 # number of seconds to wait before checking for new files

