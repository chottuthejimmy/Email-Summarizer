import ezgmail

def recent_emails(n):
    threads = ezgmail.recent(maxResults = n)
    for i in range(n):
        thread = threads[i]
        if len(thread.messages)>1:
            continue
        with open('mails.md', 'a') as f:
            f.write(thread.messages[0].body)
        #print(thread.messages[0].body)

recent_emails(1)