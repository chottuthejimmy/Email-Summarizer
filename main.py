from local_response import get_local_response
from unread import unread_emails

def main():
    prompt = unread_emails(1)
    print(prompt)
    response = get_local_response(prompt)
    print(response)
    

if __name__ == "__main__":
    main()