
# Facebook-BruteX

**Facebook-BruteX** is an educational script for brute-forcing Facebook login using a wordlist of potential passwords. It uses Selenium to automate the login process, and it is designed to help users learn about password security, brute-forcing techniques, and web automation.

## ⚠️ **Important Disclaimer**
This tool is intended for educational purposes **ONLY**. **CHEGEBB** does not take responsibility for any malicious use or unlawful actions. This script should not be used to compromise or access accounts without proper authorization. **Always ensure you have explicit permission before attempting any form of penetration testing**.

**By using this tool, you agree to take full responsibility for any consequences that arise from its usage.**

## 📜 **License**
This project is licensed under the **MIT License**.

## 🔧 **Requirements**

To run this script, you need to have Python 3.x installed along with the following dependencies. You can install them using the `requirements.txt` file:

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/CHEGEBB/Facebook-BruteX.git
   cd Facebook-BruteX
   ```

2. Install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 **How to Use the Script**

1. Make sure you have **Python 3.x** installed. You can check this by running:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/CHEGEBB/Facebook-BruteX.git
   cd Facebook-BruteX
   ```

3. Install the required libraries from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:
   You can now run the script with:
   ```bash
   python FbBruteX.py
   ```
   or if you're using Python 3:
   ```bash
   python3 FbBruteX.py
   ```

5. The script will ask you for the following:
   - Select the platform (e.g., Facebook or Instagram).
   - Select a wordlist (choose from predefined options like `rockyou.txt`, `darkweb.txt`, etc.).
   - Enter the target email/username.

6. The script will attempt each password from the wordlist and will display the current attempt along with a spinner animation.

7. **CAPTCHA Handling**: If CAPTCHA is detected during the brute-force process, the script will allow up to 30 seconds for manual solving. If not solved, the script will continue the brute-forcing process.

## 🚀 **Contribution Guidelines**

We welcome contributions! If you find any bugs or want to enhance the script with new features, feel free to open an issue or create a pull request.

### How to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## 🎨 **ASCII Banner**


```
(                                                  )  
 )\ )     (      (                    )          ( /(  
(()/(   ( )\   ( )\   (       (    ( /(     (    )\()) 
 /(_))  )((_)  )((_)  )(     ))\   )\())   ))\  ((_)\  
(_))_| ((_)_  ((_)_  (()\   /((_) (_))/   /((_) __((_) 
| |_    | _ )  | _ )  ((_) (_))(  | |_   (_))   \ \/ / 
| __|   | _ \  | _ \ | '_| | || | |  _|  / -_)   >  <  
|_|     |___/  |___/ |_|    \_,_|  \__|  \___|  /_/\_\ 
                                                      
                 Written by CHEGEBB
```

## ⚙️ **Technical Details**

This script uses **Selenium WebDriver** to automate the login process. The script simulates user input, checks the login result, and handles CAPTCHA screens. A list of password guesses is iterated, and the script will attempt to log in using each password.

## 🛠 **Known Issues**
- **CAPTCHA**: The script attempts to bypass CAPTCHA screens, but it relies on manual solving within 30 seconds.
- **Blocking**: Multiple failed attempts may lead to account or IP blocking by Facebook.

## 💡 **Educational Purpose**

This script is designed to help individuals learn about brute-forcing techniques, web automation with Selenium, and password security. **Please use this script responsibly** and only on accounts you have explicit permission to test.

---

### **Happy Hacking!**

If you encounter any issues or have any questions, feel free to open an issue here on GitHub.

```

### Key Sections of the README:
1. **Disclaimer**: A clear notice indicating the tool is for educational purposes only.
2. **Installation**: Step-by-step instructions for installing dependencies and running the script.
3. **Usage**: Instructions on how to run the script and what the user can expect.
4. **Contribution**: A guideline on how others can contribute to the project.
5. **ASCII Art**: Your custom ASCII art is included in the `README` to give it a fun touch.
6. **License**: A section on licensing (MIT License) to ensure the project’s legal coverage.

### License
For the license section, I assumed an **MIT License** for simplicity. If you have a specific license you want to apply, you can adjust it accordingly.
