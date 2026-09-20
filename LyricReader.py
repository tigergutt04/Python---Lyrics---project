import json


def LyricReader(file: str) -> None:
    with open(file) as f:  
        json_lyrics = json.load(f)

    return json_lyrics["lyrics"]
