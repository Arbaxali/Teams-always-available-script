import pyautogui
import time
import PySimpleGUI as sg

# Define the GUI layout
layout = [[sg.Text('Enter the number of clicks to perform: '), sg.InputText()],
          [sg.Text('Enter the interval between messages (in seconds): '), sg.InputText()],
          [sg.Button('Start'), sg.Button('Stop')]]

# Create the GUI window
window = sg.Window('Microsoft Teams Clicker', layout)

# Run the event loop
while True:
    event, values = window.read()
    
    # If the user clicks the 'Start' button
    if event == 'Start':
        # Get the number of clicks and interval between messages
        num_clicks = int(values[0])
        type_interval = float(values[1])
        
        # wait for 5 seconds before starting the script
        time.sleep(5)
        
        # loop through the number of clicks and type a message
        for i in range(num_clicks):
            # move the mouse to the Teams icon and click it
  
            pyautogui.click()
            
            # wait for Teams to open
            time.sleep(10)
            
            # type a message in the chat window
            pyautogui.typewrite("Hello, Qiri how are you", interval=5)
            pyautogui.press('enter')
            
            # wait for the message to be sentQi
            time.sleep(type_interval)
            
        # wait for 5 seconds before exiting the script
        time.sleep(5)
        
    # If the user clicks the 'Stop' buttonu

    if event == 'Stop':
        break

# Close the window and exit the program
window.close()
