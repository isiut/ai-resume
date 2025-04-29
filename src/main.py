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
prompt = "Why is the sky blue?"
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.cell(text="Test")
pdf.output("test.pdf")

# # TODO: create a GUI with tk
# root = tk.Tk()
# root.mainloop()
