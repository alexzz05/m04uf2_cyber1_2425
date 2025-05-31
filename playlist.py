#!/usr/bin/python3

from bs4 import BeautifulSoup
import os

def load_xml(file_path):
    """Load XML data from a file"""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return BeautifulSoup(file, "xml")
    else:
        print(f"Error: {file_path} not found!")
        return None

def show_menu():
    while True:
        print("--- Menu ---")
        print("1. Albums")
        print("2. Artists")
        print("3. Songs")
        print("4. Genres")
        print("0. Exit")
        
        option = input("Choose an option (0-4): ")
        if option.isdigit() and 0 <= int(option) <= 4:
            return int(option)
        else:
            print("Invalid choice, please enter a number between 0 and 4.")

def show_submenu(menu_type):
    """Display submenu and process input."""
    if menu_type == 'songs':
        print("1. List all songs")
        print("2. Search song by title")
    elif menu_type == 'albums':
        print("1. List all albums")
        print("2. Search album by title")
    elif menu_type == 'artists':
        print("1. List all artists")
        print("2. Search artist by name")
    elif menu_type == 'genres':
        print("1. List all genres")
        print("2. Search genre by name")
    print("0. Return")

def list_items(folder, type_name):
    """List items from the XML files in the specified folder."""
    for filename in os.listdir(folder):
        if filename.endswith(".xml"):
            item_path = os.path.join(folder, filename)
            item = load_xml(item_path)
            if item:
                print(f"{type_name} Title: {item.title.text}")

def search_item_by_title(folder, type_name):
    """Search for an item by title."""
    title = input(f"Enter the {type_name.lower()} title: ")
    found = False
    for filename in os.listdir(folder):
        if filename.endswith(".xml"):
            item_path = os.path.join(folder, filename)
            item = load_xml(item_path)
            if item and item.title.text.lower() == title.lower():
                print(f"{type_name} Found: {item.title.text}")
                found = True
                break
    if not found:
        print(f"{type_name} not found.")

def main():
    print("Playlist v0.5")
    print("-" * 15)

    while True:
        option_menu = show_menu()

        if option_menu == 0:
            print("Exiting...")
            break
        elif option_menu == 1:
            show_submenu('albums')
            album_option = input("Choose an option (0-2): ")
            if album_option == "1":
                list_items('albums', 'Album')
            elif album_option == "2":
                search_item_by_title('albums', 'Album')
        elif option_menu == 2:
            show_submenu('artists')
            artist_option = input("Choose an option (0-2): ")
            if artist_option == "1":
                list_items('artists', 'Artist')
            elif artist_option == "2":
                search_item_by_title('artists', 'Artist')
        elif option_menu == 3:
            show_submenu('songs')
            song_option = input("Choose an option (0-2): ")
            if song_option == "1":
                list_items('songs', 'Song')
            elif song_option == "2":
                search_item_by_title('songs', 'Song')
        elif option_menu == 4:
            show_submenu('genres')
            genre_option = input("Choose an option (0-2): ")
            if genre_option == "1":
                list_items('genres', 'Genre')
            elif genre_option == "2":
                search_item_by_title('genres', 'Genre')

if __name__ == "__main__":
    main()
