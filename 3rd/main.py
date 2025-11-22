from spacephoto import SpacePhoto
# import deepl

API_KEY = "2buUh7TBSJnEtdEx13XoM5fjYBYJbaWnWbdh1JiR"

def main():
    a = input("Confirm the date. Do you want your own? (1 - yes, 2 - no): ")
    if a == "1":
        b = input("Enter the date. Format: YYYY-MM-DD: ")
        photo = SpacePhoto(API_KEY, b)
        photo.load()
        photo.show_info()
    else:
        photo = SpacePhoto(API_KEY,"2025-11-21")
        photo.load()
        photo.show_info()

if name == "main":
    main()