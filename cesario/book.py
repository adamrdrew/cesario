import urllib.request
import os

class Book:
    raw_text = ""
    content = ""

    GUTENBURG_DELM = "***"

    def __init__(self, opts:dict):
        self.is_shakespeare = opts["is_shakespeare"]
        if "url" in opts:
            self.source = opts["url"]
            self.source_is_local = False
        if "file" in opts:
            self.source = opts["file"]
            self.source_is_local = True
        if "url" not in opts and "file" not in opts:
            raise Exception("Book must have a url or file")

    #Gets the lines of the text exactly as they are in the file
    def raw_lines(self) -> list[str]:
        return self.raw_text.split("\n")
    
    #Gets the lines of the text without the header and footer
    def __make_content_lines(self) -> str:
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

    def make_content_lines(self) -> str:
        start = self.raw_text.find("*** START")
        end = self.raw_text.find("*** END")
        return self.raw_text[start:end].replace("\n", " ")

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
        newbook = Book({"is_shakespeare": self.is_shakespeare, "url": self.source})
        newbook.content = new_content
        return newbook
        
    def attribute_author(self, slice_size:int, classifier) -> list[dict[str: int]]:
        slice_offset = 0
        results = []
        iterations = round(len(self.content_lines()) / slice_size)
        for i in range(iterations):
            slice_text = self.content_lines()[slice_offset:slice_offset+slice_size]
            prediction = classifier.predict_with_probability(slice_text)
            prediction_classes = prediction[0]
            is_shakespeare = prediction_classes[1] > prediction_classes[0]
            result = {
                "slice_number": i,
                "is_shakespeare": is_shakespeare,
                "is_shakespeare_probability": prediction_classes[1],
                "is_not_shakespeare_probability": prediction_classes[0]
            }
            results.append(result)
            slice_offset += slice_size
        return results
    
    def load(self):
        if self.source_is_local:
            self.__load_from_file()
        else:
            self.__load_from_url()
    
    def __load_from_file(self):
        txtfile_full_path = os.path.join(self.source)
        with open(txtfile_full_path) as f:
            self.raw_text = f.read()

    def __load_from_url(self):
        try:
            with urllib.request.urlopen(self.source) as f:
                self.raw_text =  f.read().decode("utf-8")
        except urllib.error.URLError as e:
            print("Failed to download book " + self.source + " with error " + e.reason)