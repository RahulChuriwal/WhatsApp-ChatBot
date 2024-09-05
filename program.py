import os
from dotenv import load_dotenv
import pyautogui
import time
import pyperclip
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv('API_KEY')
# print(API_KEY)
genai.configure(api_key=API_KEY)

# Allow some time to switch to the desired screen
time.sleep(3)

# Step 1: Click on the icon at (1322, 1065)
pyautogui.click(1265, 1041)

# Step 2: Drag from (662, 203) to (1897, 916) to select text
pyautogui.moveTo(864, 226)
pyautogui.dragTo(1739, 897, duration=1, button='left')

# Step 3: Copy selected text to clipboard using Ctrl+C
pyautogui.hotkey('ctrl', 'c')

# Step 4: Wait for a moment to ensure the clipboard is updated
time.sleep(0.5)
pyautogui.click(900,404)

# Step 5: Retrieve the copied text from the clipboard and store it in a variable
copied_text = pyperclip.paste()

# Print the copied text to verify
print(copied_text)

model = genai.GenerativeModel("gemini-1.5-flash")
ai_role = "You are a person named Rahul Churiwal who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast him. Output should be the next chat response (text message only). Dont start with [8:53 pm, 4/9/2024] Siddharth Bhaiya:. Just write the message."
prompt = f"{ai_role}\n\nHere is the text you need to analyze and provide a detailed response for:\n\n{copied_text}"
response = model.generate_content(prompt)
print(response.text)

# Step 6: Click on the target location (1062, 964)
pyautogui.click(1062, 964)

# Step 7: Copy the generated text to the clipboard
pyperclip.copy(response.text)

# Step 8: Paste the text at the target location using Ctrl+V
pyautogui.hotkey('ctrl', 'v')

# Step 9: Press Enter to submit the text
pyautogui.press('enter')

