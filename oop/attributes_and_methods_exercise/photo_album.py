class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if len(self.photos[self.page]) == 4:
            if self.page + 1 == self.pages:
                result = 'No more free spots'
            else:
                self.page += 1
                self.photos[self.page].append(label)
                result = f'{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}'
        else:
            self.photos[self.page].append(label)
            result = f'{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}'

        return result

    def display(self):
        result = ''
        for page in self.photos:
            result += '-' * 11 + '\n'
            for i in range(len(page)):
                if i == len(page) - 1:
                    result += '[]'
                else:
                    result += '[] '
            result += '\n'
        result += '-' * 11 + '\n'

        return result
