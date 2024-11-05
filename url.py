import webbrowser

# List to keep track of opened URLs
opened_urls = []

def open_url(link):
    """Open the specified URL in the default web browser if it's not already opened."""
    if link in opened_urls:
        print(f"The URL '{link}' has already been opened.")
    else:
        webbrowser.open(link)
        opened_urls.append(link)
        print(f"The URL '{link}' has been opened.")

# Example usage
open_url('https://www.example.com')
open_url('https://www.example.com')  # Duplicate link
open_url('https://www.openai.com')

