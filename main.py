from local_response import get_local_response
from unread import unread_emails
from output import output_fromatting
def main():
    prompt = unread_emails(1)
    response = get_local_response(prompt)
    output_fromatting(response)
    

if __name__ == "__main__":
    main()