model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(command)
print(response.text)