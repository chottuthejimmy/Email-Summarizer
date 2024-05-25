import ezgmail

def unread_emails(n): # rename and change this function to unread emails
    threads = ezgmail.recent(maxResults = n)
    threads_body = []
    for i in range(n):
        thread = threads[i]
        if len(thread.messages)>1:
            continue
        threads_body.append(thread.messages[0].body)
    return threads_body

print(unread_emails(1))