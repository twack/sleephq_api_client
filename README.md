# SleepHQ API Client

This project contains a Python client for interacting with the SleepHQ API.

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

### Windows

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

## Testing

No test included by me yet. Needs cleanup.
To run the tests, use the `test` command from the `setuptools` package.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.