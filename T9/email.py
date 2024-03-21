import random

# CLASS EMAIL with mark as read function
class Email:
    has_been_read = False

    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.email_status = self.has_been_read

    def mark_as_read(self):
        self.email_status = True

# function to populate the inbox
def populate_inbox(inbox, eaddress, esubject, econtent):
    inbox.append(Email(eaddress, esubject, econtent))

# function to list all emails and email status
def list_emails(inbox):
    print("\n Inbox:")
    for obj in inbox:
        print(f"\n  {obj.subject_line} -  Read : {obj.email_status}")

# create random 5 emails for easy testing
def create_fakeEmails():
    for i in range(5):
        sender = f"user{i+1}@example.com"
        subjects = ["Money for free", "Important message", "You won a prize", "Urgent help needed", "Marry My Daughter", "Prince from Dubai", "VOTE FOR ME"]
        subject = random.choice(subjects)
        body = '''
            Hello,
            This is a fake email.
            Regards'''
        populate_inbox(inbox, sender, subject, body)


# read emails with user input 
def read_email(user_choice, inbox):
    print(f'''\n Email Number {user_choice} Selected :
    From: {inbox[user_choice].email_address}
    Subject: {inbox[user_choice].subject_line}
    Message Content: {inbox[user_choice].email_content}
    --------------------------------------------------------------------------------------------------------------------''')
    inbox[user_choice].mark_as_read()

# check for emails not read
def unread_emails():
    for index, obj in enumerate(inbox):
        if obj.email_status == False:
            print(f"\n  {index}. {obj.subject_line} -  Read : {obj.email_status}")


inbox = []
menu = True
create_fakeEmails()

# this menu is for the user input
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        list_emails(inbox)
    elif user_choice == 2:
        unread_emails()
        user_choice = int(input('\nEmail Number:'))
        read_email(user_choice, inbox)

    elif user_choice == 3:
        print("Goodbye :*(")
        break
    else:
        print("Oops - incorrect input.")
