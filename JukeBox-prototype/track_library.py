from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Die With A Smile", "ady Gaga & Bruno Mars", 4)
library["02"] = LibraryItem("Cupid", "FIFTY FIFTY", 5)
library["03"] = LibraryItem("Sunflower ", "Post Malone & Swae Lee", 2)
library["04"] = LibraryItem("Uptown Funk", "Mark Ronson", 1)
library["05"] = LibraryItem("Michael Jackson", "Beat It", 3)


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
