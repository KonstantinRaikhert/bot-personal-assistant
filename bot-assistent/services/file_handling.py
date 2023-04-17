from math import ceil

BOOK_PATH = "bot-assistent/book/book.txt"
PAGE_SIZE = 750


book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = start + size
    prep_list = [",", ".", "!", ":", ":", "?"]
    if len(text) < end:
        new_text = text[start:]
        return new_text, len(new_text)
    if text[end] in prep_list:
        end -= 1
    while text[end] not in prep_list:
        end -= 1
    if text[end + 1] != ".":
        new_end = end + 1
        new_text = text[start:new_end]
        return new_text, len(new_text)
    else:
        if text[end - 1] in prep_list:
            end -= 2
        else:
            end -= 1
        while text[end] not in prep_list:
            end -= 1
        new_end = end + 1
        new_text = text[start:new_end]
        return new_text, len(new_text)


def prepare_book(path: str) -> None:
    with open(path, "r") as file:
        text_str = "".join(file.readlines())
        count = ceil(len(text_str) / PAGE_SIZE)
        start = 0
        for i in range(1, count + 1):
            text_line = _get_part_text(text=text_str, start=start, size=PAGE_SIZE)[0]
            book[i] = text_line.lstrip("\n ")
            start += len(text_line)


prepare_book(BOOK_PATH)
