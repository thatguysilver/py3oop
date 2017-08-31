# /usr/bin/env python3

# We learn how to use the facade pattern.

import smtplib, imaplib
# these are libraries for two common email protocols, smtp & imap.

class EmailFacade:
    '''
    The whole purpose of this is to create a class that simplifies working
    with smtplib and imaplib. aka this is something that somebody has already
    created.
    '''
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not '@' in self.username:
            from_email = '{0}@{1}'.format(self.username, self.host)

        else:
            from_email = self.username
        message = ('From: {0}\r\n'
                'To: {1}\r\n'
                'Subject: {2}\r\n\r\n{3}').format(
                        from_email,
                        to_email,
                        subject,
                        message)
    smtp = smtp.SMTP(self.host)
    smtp.login(self.username, self.password)
    smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(byes(self.username, 'utf8'),
                bytes(self.password, 'utf8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split():
            x,message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])
        return messages
    


