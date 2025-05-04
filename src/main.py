from google import genai
from google.genai import types
import json
import tkinter as tk
import tkinter.messagebox as messagebox
from fpdf import FPDF
import os

# Get gemini token from json file
with open("src/config.json", "r") as file:
    data = json.load(file)
gemini_api_key = data.get("gemini-api-key")

# Create gemini client
client = genai.Client(api_key=gemini_api_key)

name = ""
contact_info = ""
education = ""
experience = ""
skills = ""
other = ""


def generate_resume():
    # Get inputs
    name = name_input.get("1.0", tk.END).strip()
    contact_info = contact_info_input.get("1.0", tk.END).strip()
    education = education_input.get("1.0", tk.END).strip()
    experience = experience_input.get("1.0", tk.END).strip()
    skills = skills_input.get("1.0", tk.END).strip()
    other = other_input.get("1.0", tk.END).strip()

    # Send prompt
    prompt = f"""Type out a good looking resume in pdf format according to these responses to questions.
        What you are creating will be the final product. Do not include any suggestions or text other than
        the resume itself. Do not use any unicode characters such as u2013. Do not use any
        non-text formatting, pdf designations or code blocks with ```, just text. Use whatever text-based formatting you can. Use '-' for bullets.
        Do not merely paste the responses. Add some fluff to the resume and make it super attractive.
        Add a summary and infer facts about any information below to make a solid, long resume.
        Do not comments about inferring anything, simply do it. Do not format anything to the right.
        Name: '{name}'
        Contact info: '{contact_info}'
        Education: '{education}'
        Experience: '{experience}'
        Skills: '{skills}'
        Other info (put this wherever is best): '{other}'"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=prompt
        )
        print(response.text)
    except:
        messagebox.showerror(
            "Error", "An error occurred while getting data from Google Gemini."
        )
    else:
        gen_label.config(text="Creating PDF ...")
        root.update_idletasks()

    try:
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=13)
        pdf.multi_cell(0, 10, txt=response.text)
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf.output(os.path.join(downloads_folder, f"{name}.pdf"))
    except:
        messagebox.showerror("Error", "An error occurred while creating your PDF.")
    else:
        gen_label.config(text="Done! Check your Downloads.")
        root.update_idletasks()


# GUI
root = tk.Tk()
root.title("AI Resume Generator")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_input = tk.Text(root, height=1, width=30)
name_input.pack()

contact_info_label = tk.Label(root, text="Contact Info:")
contact_info_label.pack()
contact_info_input = tk.Text(root, height=2, width=30)
contact_info_input.pack()

education_label = tk.Label(root, text="Education:")
education_label.pack()
education_input = tk.Text(root, height=3, width=30)
education_input.pack()

experience_label = tk.Label(root, text="Experience:")
experience_label.pack()
experience_input = tk.Text(root, height=3, width=30)
experience_input.pack()

skills_label = tk.Label(root, text="Skills:")
skills_label.pack()
skills_input = tk.Text(root, height=2, width=30)
skills_input.pack()

other_label = tk.Label(root, text="Other Info:")
other_label.pack()
other_input = tk.Text(root, height=2, width=30)
other_input.pack()


def update_label():
    gen_label.config(text="Generating...")
    gen_label.update()
    root.update_idletasks()


gen_label = tk.Label(root, text="Click to generate")
gen_label.pack()

gen_button = tk.Button(
    root, text="Generate", width=30, command=lambda: [update_label(), generate_resume()]
)
gen_button.pack()


root.mainloop()
