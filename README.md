# Study Tracker

## A functional study tracker written in Python.

This project is a study tracker built using Python that records study sessions in an SQLite database and provides statistics such as daily study time, weekly totals, average session length and study streaks.

## Features

* Start and end study sessions
* Automatic session duration calculation
* SQLite database storage
* Daily study totals
* Weekly study totals
* Average session duration
* Daily streak calculation

## Technologies

* Python
* SQLite3
* Git

## Project Structure

- main.py - Handles the command line interface 
- session_manager.py - Handles the functions to start and end sessions
- stats_engine.py - Handles the calculation of stats 
- storage.py - Handles the creation of a database
- study_session.py - Handles the duration of a session

# Requirements

* Python 3.13

## How to run

1. Download or clone the repository.
2. Ensure Python 3 is installed on your computer.
3. Extract the ZIP file if downloaded.
4. Open the project folder.
5. Run 'main.py' using Python or a preferred IDE.

## Future Improvements

* GUI using Tkinter or PyQt
* Live session timer instead of calculating duration after completion
* Visual statistics and study graphs
* Monthly study summaries
* Improved user input and error handling
