import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY =os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

command='''
[6:32 pm, 4/9/2024] Siddharth Bhaiya: Waah tumkar do
[6:33 pm, 4/9/2024] Rahul Churiwal: Mere bolne pe koi cash nhi dega
[6:33 pm, 4/9/2024] Rahul Churiwal: Ab log tumhara sunta hai nah
[6:33 pm, 4/9/2024] Siddharth Bhaiya: Nahi sunta koi
[6:33 pm, 4/9/2024] Rahul Churiwal: Aur mera paisa se hum ipo apply Kiya hai
[6:33 pm, 4/9/2024] Rahul Churiwal: Aree kaha
[6:33 pm, 4/9/2024] Siddharth Bhaiya: Baad mai dekhta
[6:33 pm, 4/9/2024] Siddharth Bhaiya: Abhi kaam kar raha hai
[6:34 pm, 4/9/2024] Rahul Churiwal: Ok
'''
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(command)
print(response.text)
