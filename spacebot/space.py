import random


class Space:
    characters: dict[str, int] = {
        " ": 500,
        ".": 50,
        "✦": 40,
        "˚": 40,
        ":comet:": 3,
        ",": 20,
        "　ﾟ": 30,
        ":sunny:": 2,
        ":earth_americas:": 2,
        "*": 10,
        ":sun_with_face:": 0,
        ":star:": 2,
        ":sparkles:": 4,
        ":stars:": 1,
        ":full_moon:": 2,
        ":new_moon:": 2,
        ":ringed_planet:": 1,
    }

    @classmethod
    def generate(cls, length: int) -> str:
        return "".join(
            random.choices(
                list(cls.characters.keys()),
                weights=list(cls.characters.values()),
                k=length,
            )
        )
