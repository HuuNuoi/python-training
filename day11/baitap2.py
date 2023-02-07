
def print_show_info(tv_show):
    print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")
info = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(info)
