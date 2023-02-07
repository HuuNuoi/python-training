"""Yêu cầu:
Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
Thay đổi giá trị của key: release_year từ 1973 thành 1971
Xóa phần tử với key là track_list
Thêm một key mới là amount = 2000 bằng hai cách
Làm trống dict: album_info
"""
# Cho dict sau:
import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
# C1 :

value_name = album_info['album_name']
value_release = album_info['release_year']
print(f"In album name : {value_name} \nRelease year : {value_release}")

# C2 :
print(
    f"In album name : {(album_info.get('album_name'))} \nRelease year : {(album_info.get('release_year'))}")

# Thay đổi giá trị của key: release_year từ 1973 thành 1971
value_release = 1971
print(f"Release year : {value_release}")

# Xóa phần tử với key là track_list
del album_info["track_list"]
print(json.dumps(album_info, indent=4))

# 4. Thêm một key mới là amount = 2000 bằng hai cách
# album_info["amount"] = 2000
album_info.update(amount=2000)
print(json.dumps(album_info, indent=4))

# 5. Làm trống dict: album_info
album_info.clear()
print(album_info)
