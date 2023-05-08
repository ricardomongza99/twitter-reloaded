# Twitter Reloaded

Twitter Reloaded is a Twitter clone project built using Django, Python, and MySQL. The project aims to implement core Twitter features, such as creating tweets, replying to tweets, and displaying tweets as threads.

## Features

- Create tweets with a maximum of 300 characters
- Reply to tweets
- Display tweets with replies as threads
- Display the recent 10 tweets on the home dashboard
- Event dashboard that logs user actions and provides reports

## Prerequisites

- Python 3.9
- pip

## Installation

1. Clone the repository to your local machine:
    ```zsh
    git clone https://github.com/yourusername/twitter_reloaded.git
    ```
2. Navigate to the project directory:
    ```zsh
    cd twitter_reloaded
    ```
3. Create a virtual environment to isolate your project dependencies:
    ```zsh
    python -m venv venv
    ```
4. Activate the virtual environment:

   - On macOS and Linux:

     ``` zsh
     source venv/bin/activate
     ```

   - On Windows:

     ```
     .\venv\Scripts\activate
     ```
5. Install the required packages from the `requirements.txt` file:
  ``` zsh
  pip install -r requirements.txt
  ```


## Running the project

1. Start the development server:
    ``` zsh
    python manage.py runserver
    ```