# SleepHQ API Client

This project contains a Python client for interacting with the SleepHQ API.

## Project Structure

- `sleephq_api_client/`: Main source code directory.
    - `__init__.py`: Initializes the Python package.
    - `constants.py`: Contains constant values used across the project.
    - `file_stores/`: Contains modules for handling file storage.
        - `resmed/`: Module for ResMed file storage.
        - `viatom/`: Module for Viatom file storage.
        - `withings/`: Module for Withings file storage.
    - `lib/`: Contains utility modules and shared code.
        - `api.py`: Defines the API client.
        - `check_credentials.py`: Provides functionality to validate API credentials.
        - `logger_conf.py`: Sets up the application logger.
        - `new_file_trigger.py`: Handles triggering of new file events.
    - `main.py`: Entry point of the application.
- `tests/`: Contains unit tests for the project.

## Setup

1. Clone the repository.
2. Set up the virtual environment by running `source venv/bin/activate`.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the main script by running `python sleephq_api_client/main.py`.

## Testing

To run the tests, use the `test` command from the `setuptools` package.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.