import pandas as pd
import numpy as np
import datetime
import os
import sys
import time

# Global variable to keep track of the task being tracked
current_task = None
# Global variable to indicate whether to continue time tracking
continue_tracking = None

# Create a function to start and stop time tracking
def time_tracker(task):
    global current_task, continue_tracking
    current_task = task
    print(f"Started tracking time for task: {task}")

    # Create a list to store data dictionaries
    data_list = []

    # Start time tracking loop
    while continue_tracking:
        # Use time to automatically track date and time
        # Create a variable to store the current date and time
        current_time = datetime.datetime.now()

        # Record start time
        start_time = current_time

        # Print current time every 10 seconds
        print(f"Current time: {start_time}")
        time.sleep(10)

        # # Check if the task has changed or not
        # if task != current_task:
        #     print("Task changed. Stopping time tracker.")
        #     break  # Break out of the loop if the task changes

        # Record end time
        end_time = datetime.datetime.now()

        # Calculate completed time
        completed_time = end_time - start_time

        # Append data dictionary to the list
        data_list.append({'Date': current_time,
                          'Task': task,
                          'Start Time': start_time,
                          'End Time': end_time,
                          'Completed Time': completed_time})

    # # Convert the list of dictionaries into a DataFrame
    # df = pd.DataFrame(data_list)

    # # Convert time-related columns to datetime objects
    # df['Date'] = pd.to_datetime(df['Date'])
    # df['Start Time'] = pd.to_datetime(df['Start Time'])
    # df['End Time'] = pd.to_datetime(df['End Time'])
    # df['Completed Time'] = pd.to_timedelta(df['Completed Time'])

    # # Save dataframe to CSV file
    # file_name = 'time_tracker.csv'
    # df.to_csv(file_name, index=False)

    print("Time tracking stopped.")

# Function to start the time tracking
def start_time_tracking(task):
    global continue_tracking
    continue_tracking = True
    time_tracker(task)

# Function to stop the time tracking
def stop_time_tracking():
    global continue_tracking
    continue_tracking = False