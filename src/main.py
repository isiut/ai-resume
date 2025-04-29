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

name = "John James"
contact_info = "phone: 2245091996, email: johnny@gmail.com"
education = "I studied at Waukegan High School, majored in English and minored in psychology at Harvard"
experience = "I have worked as an english teacher at Mundelein High School for 10 years"
skills = "High school education, English"
other = "I'm a very hard worker"


# Send prompt
prompt = f"""Type out a good looking resume in pdf format according to these responses to questions.
    What you are creating will be the final product. Do not include any suggestions or text other than
    the resume itself. Do not use any unicode characters such as u2013. Do not use any
    non-text formatting or ``` pdf, just text. Use whatever text-based formatting you can. Use '-' for bullets.
    Do not merely paste the responses. Add some fluff to the resume and make it super attractive.
    Add a summary and infer facts about any information below to make a solid, long resume.
    Name: '{name}'
    Contact info: '{contact_info}'
    Education: '{education}'
    Experience: '{experience}'
    Skills: '{skills}'
    Other info (put this wherever is best): '{other}'"""

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
print(response.text)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=13)
pdf.multi_cell(0, 10, txt=response.text)
pdf.output("test.pdf")

# # TODO: create a GUI with tk
# root = tk.Tk()
# root.mainloop()
