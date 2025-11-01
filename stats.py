from typing import TypedDict


def get_num_words(filepath: str):
    with open(filepath) as f:
        return len(f.read().split())


def get_num_chars(bookstring: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in bookstring.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


class CharCount(TypedDict):
    char: str
    num: int


def get_sorted_dictionary_list(counts: dict[str, int]) -> list[CharCount]:
    res: list[CharCount] = []
    for key, value in counts.items():
        res.append({"char": key, "num": value})

    res.sort(key=lambda x: x["num"], reverse=True)

    return res
