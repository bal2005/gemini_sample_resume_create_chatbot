# Gemini Sample Resume Create Chatbot

This is a simple chat application built with Flask that simulates a conversation between an HR representative and an employee.

## Features

*   Two distinct chat interfaces for HR and Employee.
*   Messages are sent back and forth between the two interfaces in real-time.
*   A clean and simple user interface.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/bal2005/gemini_sample_resume_create_chatbot.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the application:
    ```bash
    python app.py
    ```
2.  Open two browser windows or tabs.
3.  In the first window, navigate to `http://127.0.0.1:5000/hr` to act as the HR representative.
4.  In the second window, navigate to `http://127.0.0.1:5000/employee` to act as the employee.
5.  Messages sent from one window will appear in the other.

## Dependencies

*   [Flask](https://flask.palletsprojects.com/)
