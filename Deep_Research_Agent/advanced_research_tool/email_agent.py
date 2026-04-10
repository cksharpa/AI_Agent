import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, body: str) -> Dict[str, str]:
    """Send email to all prospect Clients"""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("cksharpa@gmail.com")  # Change to your verified sender
    to_email = To("<receiver>@gmail.com")  # Change to your recipient
    content = Content("text/html", body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return  "success"

instructions ="You are responsible for formatting and sending emails. \
Given an email body, first generate an appropriate subject using the subject_writer tool. \
Then convert the body into HTML using the html_converter tool. \
Finally, send the email using the send_html_email tool with the generated subject and HTML content."

email_agent = Agent(name="Email Manager", instructions=instructions, 
    tools=[send_email], model="gpt-oss-20b",)