
class Book:
    title = ""
    author = ""
    url = ""
    raw_text = ""
    content = ""

    GUTENBURG_DELM = "***"

    def __init__(self, title:str, author: str, url:str):
        self.title = title
        self.author = author
        self.url = url

    #Gets the lines of the text exactly as they are in the file
    def raw_lines(self) -> list[str]:
        return self.raw_text.split("\n")
    
    #Gets the lines of the text without the header and footer
    def make_content_lines(self) -> str:
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

    #Memoized getter for content_lines
    def content_lines(self) -> list[str]:
        if len(self.content) == 0:
            self.content = self.make_content_lines()
        return self.content

    #Gets the size (length) of the content
    def size(self) -> int:
        return len(self.content_lines())

    #Splits the book by a size and returns that as a new book
    def split(self, size: int): 
        new_content = self.content_lines()[:size]
        remainder = self.content_lines()[size:]
        self.content = remainder
        newbook = Book(self.title, self.author, self.url)
        newbook.content = new_content
        return newbook
        
