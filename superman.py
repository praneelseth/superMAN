import requests
import threading
import time
import sys

from colorama import Fore, Back, Style, init

import subprocess

# Define colors in order to simulate the beachball colors
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def print_ball(i):
    # Create the beachball ASCII art with rotating colors
    ball = f"""
                   {colors[i % len(colors)]}*** ### {colors[(i + 5) % len(colors)]}### ***
               {colors[i % len(colors)]}*###########{colors[(i + 5) % len(colors)]}##########*
           {colors[i % len(colors)]}*###############{colors[(i + 5) % len(colors)]}##############*
        {colors[i % len(colors)]}*##################{colors[(i + 5) % len(colors)]}#################*
      {colors[i % len(colors)]}*####################{colors[(i + 5) % len(colors)]}###################*
    {colors[(i + 1) % len(colors)]}*####{colors[i % len(colors)]}#################{colors[(i + 5) % len(colors)]}#################{colors[(i + 4) % len(colors)]}#####*
   {colors[(i + 1) % len(colors)]}*########{colors[i % len(colors)]}##############{colors[(i + 5) % len(colors)]}#############{colors[(i + 4) % len(colors)]}##########*
  {colors[(i + 1) % len(colors)]}*############{colors[i % len(colors)]}###########{colors[(i + 5) % len(colors)]}##########{colors[(i + 4) % len(colors)]}##############*
 {colors[(i + 1) % len(colors)]}*################{colors[i % len(colors)]}########{colors[(i + 5) % len(colors)]}#######{colors[(i + 4) % len(colors)]}##################*
 {colors[(i + 1) % len(colors)]}*###################{colors[i % len(colors)]}#####{colors[(i + 5) % len(colors)]}####{colors[(i + 4) % len(colors)]}#####################*
 {colors[(i + 1) % len(colors)]}*#######################{colors[i % len(colors)]}#{colors[(i + 5) % len(colors)]}#{colors[(i + 4) % len(colors)]}########################*
 {colors[(i + 1) % len(colors)]}*#######################{colors[(i + 2) % len(colors)]}##{colors[(i + 3) % len(colors)]}#{colors[(i + 4) % len(colors)]}#######################*
 {colors[(i + 1) % len(colors)]}*###################{colors[(i + 2) % len(colors)]}######{colors[(i + 3) % len(colors)]}####{colors[(i + 4) % len(colors)]}####################*
  {colors[(i + 1) % len(colors)]}*###############{colors[(i + 2) % len(colors)]}#########{colors[(i + 3) % len(colors)]}#######{colors[(i + 4) % len(colors)]}################*
   {colors[(i + 1) % len(colors)]}*###########{colors[(i + 2) % len(colors)]}############{colors[(i + 3) % len(colors)]}##########{colors[(i + 4) % len(colors)]}############*
    {colors[(i + 1) % len(colors)]}*#######{colors[(i + 2) % len(colors)]}###############{colors[(i + 3) % len(colors)]}#############{colors[(i + 4) % len(colors)]}########*
      {colors[(i + 1) % len(colors)]}*##{colors[(i + 2) % len(colors)]}##################{colors[(i + 3) % len(colors)]}################{colors[(i + 4) % len(colors)]}###*
        {colors[(i + 2) % len(colors)]}*##################{colors[(i + 3) % len(colors)]}#################*
           {colors[(i + 2) % len(colors)]}*###############{colors[(i + 3) % len(colors)]}##############*
               {colors[(i + 2) % len(colors)]}*###########{colors[(i + 3) % len(colors)]}##########*
                   {colors[(i + 2) % len(colors)]}*** ### {colors[(i + 3) % len(colors)]}### ***
                   {Style.RESET_ALL}
"""
    print(ball)


# Initialize colorama for cross-platform color support
init()

def loading_animation():
    while not stop_loading_event.is_set():
        # ANSI escape sequence to clear screen
        for i in range(len(colors)):
            print("\033[H\033[J", end="")
            print_ball(i)
            time.sleep(0.1)
    print("\033c", end="")

def run_command(command):
    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # Output the result
    print(result.stdout)

def explain_command(command):
    # Define the data with the user's input
    data = {
        "model": "superman_expl",
        "messages": [
            { "role": "user", "content": command }
        ],
        "stream": False
    }
    # Create a threading event to control the loading animation
    stop_loading_event = threading.Event()
    
    # Start the loading animation in a separate thread
    loader_thread = threading.Thread(target=loading_animation)
    loader_thread.start()

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        
        # Stop the loading animation
        stop_loading_event.set()
        loader_thread.join()  # Wait for the loader thread to finish
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the response
            print("\nResponse JSON:", response.json())
            command = response.json()['message']['content']
            print("Explanation: ")
            print(command)
            request_times.append(response.json()['total_duration'])
        else:
            print("Error:", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        stop_loading_event.set()
        loader_thread.join()
        print("Request failed:", e)

# URL with the custom port
# will need 128.83.177.39 or cloudflare
url = "https://aviation-intro-distance-americans.trycloudflare.com/api/chat"

request_times = []

# Start the loop for multiple inputs
while True:
    # Prompt the user for input
    user_input = input("\nEnter your question or type \"exit\": ")
    
    # Break the loop if the user types "exit"
    if user_input.lower() == "exit":
        print("Exiting superman.")
        break
    
    # Define the data with the user's input
    data = {
        "model": "superman_code",
        "messages": [
            { "role": "user", "content": user_input }
        ],
        "stream": False
    }
    
    # Create a threading event to control the loading animation
    stop_loading_event = threading.Event()
    
    # Start the loading animation in a separate thread
    loader_thread = threading.Thread(target=loading_animation)
    loader_thread.start()

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        
        # Stop the loading animation
        stop_loading_event.set()
        loader_thread.join()  # Wait for the loader thread to finish
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the response
            print("\nResponse JSON:", response.json())
            command = response.json()['message']['content']
            if command == "Invalid question.":
                print(command)
            else:
                print("Enter y to run this command, e to explain this command, r to retry, n to cancel:", command)
                run = input()
                if run == "y":
                    run_command(command)
                elif run == "r":
                    continue
                elif run == "e":
                    explain_command(command)
                elif run == "n":
                    print("Command cancelled")
                else:
                    print("Invalid input")
            request_times.append(response.json()['total_duration'])
        else:
            print("Error:", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        stop_loading_event.set()
        loader_thread.join()
        print("Request failed:", e)

print("Request times:", request_times)