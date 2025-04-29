from google import genai
from google.genai import types
import json
import tkinter as tk
from fpdf import FPDF

# Get gemini token from json file
with open("src/config.json", "r") as file:
    data = json.load(file)
gemini_api_key = data.get("gemini-api-key")

# Create gemini client
client = genai.Client(api_key=gemini_api_key)

# Send prompt
prompt = "Should the math folder be red or blue"
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
print(response.text)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("courier", size=12)
pdf.multi_cell(0, 10, txt=response.text)
pdf.output("test.pdf")

# # TODO: create a GUI with tk
# root = tk.Tk()
# root.mainloop()