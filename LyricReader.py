import json


def LyricReader(file: str) -> None:
    with open(file) as f:  
        json_lyrics = json.load(f)

    for line in json_lyrics["lyrics"]:
        print(line)

LyricReader('lyric.json')