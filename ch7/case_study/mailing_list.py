# our attempt at a mailing list in py.

import smtplib
from collections import defaultdict
from email.mime.text import MIMEText

class MailingList:
    'Manage groups of email addresses for sending emails.'
    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        'Returns a set of all emails in the given group(s).'
        groups = set(groups) # Creates a set out of our groups list.
        emails = set()       # Creates an empty set.
        for e, g in self.email_map.items(): # adds the key e to emails if g in group(s)
            if g & groups:                  # '&' = intersection
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers = None):
        'Actually sends our emails to the groups they\'ve been added to'
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers = headers)

    def save(self):
        'Majorly insecure way to save our email list to disk.'
        with open(self.data_file, 'w') as file:
            for email, groups in self.email_map.items():
                file.write(
                        '{} {}\n'.format(email, ','.join(groups))
                        )

    def load(self):
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(' ')
                    groups = set(groups.split(','))
                    self.email_map[email] = groups
        except IOError:
            pass

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

def send_email(subject, message, from_addr, *to_addrs, 
        host = 'localhost', port = 1025, headers = None):

    headers = {} if headers is None else headers

    email = MIMEText(message)
    email['subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()
