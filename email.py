import win32com.client as win32
import os
import subprocess


# Render Quarot

# Set the QUARTO_PATH environment variable
os.environ['QUARTO_PATH'] = 'C:/Program Files/RStudio/resources/app/bin/quarto/bin/'

# Define the paths for input and output
input_file = 'C:/Users/025883/OneDrive - Hawaiian Airlines, Inc/Documents/R Scripts/fsc_utilization/fsc_utilization.qmd'
execute_dir = 'C:/Users/025883/OneDrive - Hawaiian Airlines, Inc/Documents/R Scripts/fsc_utilization'

# Construct the Quarto command
command = [
    os.path.join(os.environ['QUARTO_PATH'], 'quarto'),
    'render',
    input_file,
    '--execute-dir', execute_dir
]

# Execute the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output and any errors
# print(result.stdout)
# print(result.stderr)
 
 
# Email
 
# You can adjust who recieves the email with the Irregularities report here
recipient = [
    "jacob.eisaguirre@hawaiianair.com",
    "derek.sutton@hawaiianair.com",
    "joshua.hamilton@hawaiianair.com",
    "patrick.flynn@hawaiianair.com",
    "Keenan-Celtic.Faatea@hawaiianair.com",
    "Terrance.Chariandy@hawaiianair.com"
    ]

# Join the list of recipients into a single string separated by semicolons
recipient_str = ";".join(recipient)
 
def send_email_with_attachment(recipient, subject, body, attachment_path):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.Body = body
    mail.Attachments.Add(attachment_path)
    mail.Send()


subject = "Monthly Freight Short Call Utilization Report"
body = "Aloha, Please find attached the Freight Short Call Utilization report."
attachment_path = os.getcwd() + "\\fsc_utilization.html"
 
# Modify the attachment path with the actual reporting week
#attachment_path = attachment_path.replace('reporting_week', reporting_week)
 
# Check if the file exists before sending the email
if os.path.exists(attachment_path):
    send_email_with_attachment(recipient_str, subject, body, attachment_path)
    print("Email sent successfully!")
else:
    print("Attachment file not found.")

