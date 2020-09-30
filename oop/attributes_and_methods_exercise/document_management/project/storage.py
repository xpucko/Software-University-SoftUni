class Storage:
    def __init__(self, ):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current = [x for x in self.categories if x.id == category_id][0]
        current.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current = [x for x in self.topics if x.id == topic_id][0]
        current.topic = new_topic
        current.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current = [x for x in self.documents if x.id == document_id][0]
        current.file_name = new_file_name

    def delete_category(self, category_id):
        current = [x for x in self.categories if x.id == category_id][0]
        self.categories.remove(current)

    def delete_topic(self, topic_id):
        current = [x for x in self.topics if x.id == topic_id][0]
        self.topics.remove(current)

    def delete_document(self, document_id):
        current = [x for x in self.documents if x.id == document_id][0]
        self.documents.remove(current)

    def get_document(self, document_id):
        current = [x for x in self.documents if x.id == document_id][0]
        return current

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f'{document.__repr__()}\n'

        return result