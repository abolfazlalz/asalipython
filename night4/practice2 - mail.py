class Email:
    def __init__(self, title, content, sender, receiver):
        self.title = title
        self.content = content
        self.sender = sender
        self.receiver = receiver


class EmailAccount:
    def __init__(self, email_address):
        self.mail = email_address
        self.sent = []

    def send(self, title, content, receiver):
        new_mail = Email(
            title,
            content,
            self.mail,
            receiver,
        )
        self.sent.append(new_mail)

    def show_sent_box(self):
        # print(self.sent)
        print("your sent box:")
        for mail in self.sent:
            print("Title:", mail.title)
            print("Receiver:", mail.receiver)


account = EmailAccount("a.alizadeh@gmail.com")
account.send("vpn", "this is my new vpn", "f.torkamani@gmail.com")
account.show_sent_box()
