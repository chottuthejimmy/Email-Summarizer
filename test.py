import ezgmail
from transformers import pipeline

# Step 1: Authenticate with Gmail
ezgmail.init()

# Step 2: Fetch the most recent 10 emails
threads = ezgmail.recent(maxResults=2)

# Step 3: Extract email content
email_texts = []
for thread in threads:
    for message in thread.messages:
        email_texts.append(message.body)

# Step 4: Initialize summarizer
summarizer = pipeline('summarization')

# Step 5: Summarize emails
summaries = []
for text in email_texts:
    summary = summarizer(text, max_length=20, min_length=10, do_sample=False)
    summaries.append(summary[0]['summary_text'])

# Step 6: Display summaries
for i, summary in enumerate(summaries):
    print(f"Email {i+1} Summary:\n{summary}\n")
