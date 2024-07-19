import subprocess
import time
import os
import tempfile

def display_initial_message():
    message = """
@echo off
reg add "HKCU\\Console" /v FullScreen /t REG_DWORD /d 1 /f
echo ******************************************************************************
echo *                                                                            *
echo *                           TEST SCRIPT EXECUTION                            *
echo *                                                                            *
echo * This framework, developed by Vithal-ji using Selenium with Python,         *
echo * is designed for ease of use even by individuals with minimal programming   *
echo * knowledge. After a brief practice period, users can understand the         *
echo * functions in the library file and utilize the framework effectively.       *
echo *                                                                            *
echo * The framework automatically generates Proof Of Testing files along with    *
echo * Test Case files by providing valid inputs during script execution.         *
echo *                                                                            *
echo * *********************** EXECUTING TEST SCRIPTS **************************** *
echo * The following scripts will be executed:                                    *
echo * - Purchase Order Creation                                                  *
echo * - Sales Order Creation                                                     *
echo * - Sales Invoice Creation                                                   *
echo * - Purchase Invoice Creation                                                *
echo *                                                                            *
echo ******************************************************************************
timeout /T 25
"""
    # Create a temporary batch file with the message
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bat") as temp_batch:
        temp_batch.write(message.encode('utf-8'))
        temp_batch_path = temp_batch.name

    # Run the temporary batch file
    command = f"start cmd /max /k \"{temp_batch_path}\""
    subprocess.Popen(command, shell=True)

def display_thank_you_message():
    thank_you_message = """
@echo off
reg add "HKCU\\Console" /v FullScreen /t REG_DWORD /d 1 /f
echo ******************************************************************************
echo *                                                                            *
echo *                         All test scripts have been executed.               *
echo *                                                                            *
echo *                              Thank you!                                    *
echo *                                                                            *
echo ******************************************************************************
"""
    # Create a temporary batch file with the thank you message
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bat") as temp_batch:
        temp_batch.write(thank_you_message.encode('utf-8'))
        temp_batch_path = temp_batch.name

    # Run the temporary batch file
    command = f"start cmd /max /k \"{temp_batch_path}\""
    subprocess.Popen(command, shell=True)

def run_script(script_name):
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def main():
    print("\033[1;32m" + "Starting all test scripts..." + "\033[0m")
    
    scripts = [
        "C:/Testing_projects/Automation/B-POS/Test_Script_Files/Purchase_Order_Creation.py",
        "C:/Testing_projects/Automation/B-POS/Test_Script_Files/Sales_Order_Creation.py",
        "C:/Testing_projects/Automation/B-POS/Test_Script_Files/Sales_Invoice_Creation.py",
        "C:/Testing_projects/Automation/B-POS/Test_Script_Files/Purchase_invoice_Creation.py"
    ]
    
    display_initial_message()
    time.sleep(25)  # Wait for 10 seconds before running the scripts

    for script in scripts:
        print(f"\nRunning {script}...\n")
        run_script(script)
    
    print("\033[1;32m" + "All test scripts have been executed." + "\033[0m")

    # Display the thank you note in another command prompt window
    display_thank_you_message()


main()
