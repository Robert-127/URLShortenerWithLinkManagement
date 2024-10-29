from url_shortener import URLShortener



def main():

    access_token = "YOUR_BITLY_ACCESS_TOKEN"

    url_shortener = URLShortener(access_token)



    while True:

        print("\n1. Shorten URL")

        print("2. Expand URL")

        print("3. Delete URL")

        print("4. Get Clicks")

        print("5. Exit")

        choice = input("Choose an option: ")



        if choice == '1':

            long_url = input("Enter the URL to shorten: ")

            short_url = url_shortener.shorten_url(long_url)

            if short_url:

                print(f"Shortened URL: {short_url}")



        elif choice == '2':

            short_url = input("Enter the shortened URL: ")

            long_url = url_shortener.expand_url(short_url)

            if long_url:

                print(f"Original URL: {long_url}")



        elif choice == '3':

            short_url = input("Enter the shortened URL to delete: ")

            url_shortener.delete_url(short_url)



        elif choice == '4':

            short_url = input("Enter the shortened URL to get clicks: ")

            clicks = url_shortener.get_clicks(short_url)

            if clicks is not None:

                print(f"Number of clicks: {clicks}")



        elif choice == '5':

            break



        else:

            print("Invalid option. Please try again.")



if __name__ == "__main__":

    main()



