
class Book:
    title = ""
    author = ""
    url = ""
    raw_text = ""

    CONTENT_START = "*** START OF THE PROJECT GUTENBERG EBOOK"
    CONTENT_END = "*** END OF THE PROJECT GUTENBERG EBOOK"

    GUTENBURG_DELM = "***"

    def __init__(self, title:str, author: str, url:str):
        self.title = title
        self.author = author
        self.url = url

    #Gets the lines of the text exactly as they are in the file
    def raw_lines(self) -> list[str]:
        return self.raw_text.split("\n")
    
    #Gets the lines of the text without the header and footer
    def content_lines(self) -> list[str]:
        out = []
        found_content = False
        for line in self.raw_lines():
            if line.startswith(self.GUTENBURG_DELM) and not found_content:
                found_content = True
                continue
            if line.startswith(self.GUTENBURG_DELM) and found_content:
                break
            if found_content:
                out.append(line)
        return "\n".join(out)