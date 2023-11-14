class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Entry must contain a title or contents.")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Can't calculate with wpm of 0")
        return len(self.contents.split()) / wpm

    def reading_chunk(self, wpm, minutes):
       WUCR = wpm * minutes
       words = self.contents.split()
       if self.read_so_far > len(words):
           self.read_so_far = 0
       chunk_start = self.read_so_far
       chunk_end = self.read_so_far + WUCR
       chunk_words = words[chunk_start:chunk_end]
       self.read_so_far = chunk_end
       return " ".join(chunk_words)