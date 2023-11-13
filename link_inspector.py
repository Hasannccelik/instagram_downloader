
import instaloader
L = instaloader.Instaloader()


# Get the URL from the user
url = input("Please enter a URL: ")
# Split the URL by '/' and store it in a list 
url_list = url.split('/')

# Check if the first element of the list is 'https:' 
if url_list[0] == 'https:':

    # If yes, delete it from the list 
    del url_list[0]
    # Join the remaining elements of the list with '/' and store it in a new variable 
    new_url = '/'.join(url_list)
    url=url_list[3]
    # Print out the new URL 
    print("New URL:", url)
    


