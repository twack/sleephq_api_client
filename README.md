# SleepHQ API Client

This project contains a Python client for interacting with the SleepHQ API. It monitors the subfolders
in the `file_stores` directory. Anytime a new file shows up, it will trigger an upload automatically.

It is only working for Viatom Ring files right now. All the same naming conventions that SleepHQ has for these
files are upheld. When the application runs and the file(s) is/are imported to your SleepHQ account, it/they should show up in your "Data Imports" page on the SleepHQ website. If the import/upload is successful, the name of the file as added to a file called `inventory.json`.

In the `constants.py` file there is a `CHECK_FREQ` veriable where you can set how many seconds the application
checks the  `file_stores` directory for new files. Set this value with some caution with consideration of the 
computer you are running on. The checker is on a seperate thread to try and minimize processor resources.

## Project Structure

- `sleephq_api_client/`: Main source code directory.
    - `__init__.py`: Initializes the Python package.
    - `constants.py`: Contains constant values used across the project.
    - `file_stores/`: Contains folders for file storage and `inventory.json` files.
        - `resmed/`: Module for ResMed file storage.
        - `viatom/`: Module for Viatom file storage.
        - `withings/`: Module for Withings file storage.
    - `lib/`: Contains utility modules and shared code.
        - `api.py`: Defines the API client.
        - `check_credentials.py`: Provides functionality to validate API credentials.
        - `logger_conf.py`: Sets up the application logger.
        - `new_file_trigger.py`: Handles triggering of new file events.
    - `main.py`: Entry point of the application.
- `tests/`: Contains unit tests for the project. Not updated yet. Needs cleanup

## Setup

Follow these steps to set up the project on your local machine:

1. Open Command Prompt.
2. Navigate to the location where you want to create the project folder:
    ```cmd
    cd <folder_path>
    ```
3. Create a new folder:
    ```cmd
    mkdir sleephq_api_client
    ```
4. Navigate into the new folder:
    ```cmd
    cd sleephq_api_client
    ```
5. Clone the GitHub repository:
    ```cmd
    git clone https://github.com/twack/sleephq_api_client.git
    ```
6. Set up the virtual environment:
    - Install the virtual environment package if not already installed:
        ```cmd
        pip install virtualenv
        ```
    - Create a new virtual environment:
        ```cmd
        virtualenv venv
        ```
    - ### Windows: Activate the virtual environment:
        ```cmd
        venv\Scripts\activate
        ```
    - ### Unix/MacOS Activate the virtual environment:
        ```cmd
        source venv/bin/activate
        ```
7. Install the required packages:
    ```cmd
    pip install -r requirements.txt
    ```
8. Run the main script:
    ```cmd
    python sleephq_api_client/main.py
    ```


Replace `<folder_path>` with the path to the location where you want to create the project folder.

## Constants

The `constants.py` file is used for settings certain variables used throughout the application.
### These can be set here, or as environment variables of the same name. 
`SLEEPHQ_CLIENT_UID=<your client ID>`

`SLEEPHQ_CLIENT_SECRET=<your client Secret>`

`SLEEPHQ_TEAM_ID=<your team id>` if you leave this blank it will use your default team id. This is mainly for if you belong to multiple teams.

### These must be set in the `constants.py` file

`CHECK_FREQ=5` variable where you can set how many seconds the application check for new files.

`FILE_STORE=./file_stores/` directory for storing and checking for new files.

`MINIMUM_RING_FILE_SIZE=500` # minimum file size in bytes for a ring file to be considered for upload to SleepHQ

`FILE_SETTLE_TIME=10` # number of seconds to wait before considering a file as complete

## Testing

No test included by me yet. Needs cleanup.
To run the tests, use the `test` command from the `setuptools` package.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.