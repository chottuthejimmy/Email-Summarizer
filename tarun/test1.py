import ezgmail, os
from transformers import pipeline
unreadThreads = ezgmail.unread()
# ezgmail.summary(unreadThreads, )
# print(unreadThreads)
print(unreadThreads[0].messages[0].body)
# summarizer = pipeline('summarization')
