
def output_fromatting(response):
 # convert the response into a .md file named catchup.md
    with open('catchup.md', 'w') as f:
        f.write(response)
    print("The response has been written to catchup.md")
    return None