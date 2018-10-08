class Source:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Articles:
    def __init__(self,source,author,title,description,url,urltoImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urltoImage = urltoImage
        self.publishedAt = publishedAt
