import re
import customtkinter as ctk

root = ctk.CTk()
root.title("Email Extractor - Alpha 1 Version")
root.geometry("800x700")
root.configure(fg_color="#70cce1")

titles_font = ctk.CTkFont(size=20,family="Digital", weight="bold")
ENTER_EMAIL_TEXT = ctk.CTkLabel(root,text="Enter Your Long Text to\nExtract Emails",font=titles_font)
ENTER_EMAIL_TEXT.pack()

enter_email_sec = ctk.CTkTextbox(root,height=280,width=750)
enter_email_sec.pack()
email_number=""
email_number_label = ctk.CTkLabel(root, text=email_number)
email_number_label.pack()
def get_text_to_extract() :
    global email_number
    raw_text = enter_email_sec.get("1.0","end")
    extract_raw = re.findall(r"\w+@\w+.\w+",string=raw_text)
    output_emails_sec.delete("1.0","end")
    email_number = len(extract_raw)

    if email_number:
        email_number_label.configure(text=f"There's {email_number} Founded")
    else:
        email_number_label.configure(text="No Emails Founded :(")
    for everyemail in extract_raw :
        output_emails_sec.insert("end",everyemail + "\n")


RUN_BUTTON= ctk.CTkButton(root,text="Extract It",hover=True,height=70, width=200,font=("Normal",20),command=get_text_to_extract)
RUN_BUTTON.pack(padx=10,pady=10)

output_emails_sec = ctk.CTkTextbox(root,height=200,width=750,font=("Normal",15),)
output_emails_sec.pack()


root.mainloop()