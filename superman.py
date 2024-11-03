import requests
import threading
import time
import sys
import os
from shell_find import get_shell_info

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

def loading_animation(loading_event):
    while not loading_event.is_set():
        # ANSI escape sequence to clear screen
        for i in range(len(colors)):
            print("\033[H\033[J", end="")
            print_ball(i)
            time.sleep(0.1)
    print("\033[H\033[J", end="")

def run_command(command):
    # Run the command
    result = os.popen(command)
    # Output the result
    print(result.read())

def explain_command(command_to_explain):
    # Define the data with the user's input
    explain_data = {
        "model": "superman_expl",
        "messages": [
            { "role": "user", "content": command_to_explain }
        ],
        "stream": False
    }

    # Create a threading event to control the loading animation
    explain_loading_event = threading.Event()
    
    # Start the loading animation in a separate thread
    explain_loader_thread = threading.Thread(target=loading_animation, args=(explain_loading_event,))
    explain_loader_thread.start()

    # Send the POST request
    try:
        response = requests.post(url, json=explain_data)
        
        # Stop the loading animation
        explain_loading_event.set()
        explain_loader_thread.join()  # Wait for the loader thread to finish
        
        # Check if the request was successful
        if response.status_code == 200:
            # Print the response
            explanation = response.json()['message']['content']
            print(f"""{superman_color}Explanation of command:""", f""": \n{Fore.YELLOW}""", explanation)
            request_times.append(response.json()['total_duration'])
        else:
            print("Error:", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        explain_loading_event.set()
        explain_loader_thread.join()
        print("Request failed:", e)

# URL with the custom port
# will need 128.83.177.39 or cloudflare
shell_info = get_shell_info()
url = "https://andrews-accepted-subscribers-reach.trycloudflare.com/api/chat"

request_times = []

# Start the loop for multiple inputs
superman_color = Fore.LIGHTGREEN_EX
start_message = f"""{superman_color}Welcome to {Fore.MAGENTA}superMAN{superman_color}! Your one stop shop for all your terminal command needs.{Fore.WHITE}"""
question_prompt = f"""{superman_color}\nAsk me a question! or type \"exit\" to quit: {Fore.WHITE}"""
exit_message = f"""{superman_color}\nUp, up, and away! Until next time.{Fore.WHITE}"""
print(start_message)
while True:
    # Prompt the user for input
    user_input = input(question_prompt)
    
    # Break the loop if the user types "exit"
    if user_input.lower() == "exit":
        print(exit_message)
        break
    
    # Define the data with the user's input
    user_input = shell_info + " " + user_input
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
    loader_thread = threading.Thread(target=loading_animation, args=(stop_loading_event,))
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
            command = response.json()['message']['content']
            if command == "Invalid question.":
                print(command)
            else:
                print(f"""{superman_color}Here's your command(s): """)
                print(f"""{Fore.YELLOW}""", command)
                print(f"""{superman_color}Enter 'r' to run this command, 'e' to explain this command, 'm' to modify, or 'x' to cancel.{Fore.WHITE}""")
                run = input().lower()
                if run == "r":
                    run_command(command)
                elif run == "m":
                    continue
                elif run == "e":
                    explain_command(command)
                elif run == "x":
                    print(f"""{superman_color}Command cancelled""")
                else:
                    print(f"""{Fore.RED}Invalid input""")
            request_times.append(response.json()['total_duration'])
        else:
            print(f"""{Fore.RED}Error:""", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        stop_loading_event.set()
        loader_thread.join()
        print(f"""{Fore.RED}Request failed:""", e)

# print("Request times:", request_times)
