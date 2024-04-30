class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) >0:
            self._title = value
        

class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        my_magazines = [article.magazine for article in Article.all if article.author == self]
        filtered_magazines = list(set(my_magazines))
        return filtered_magazines

    def add_article(self, magazine, title:str):
        new_article = Article(author=self, magazine=magazine, title=title)
        return new_article

    def topic_areas(self):
        my_categories = [article.magazine.category for article in Article.all if article.author == self]
        filtered_categories = list(set(my_categories))
        if filtered_categories == []:
            return None
        else:
            return filtered_categories
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >0:
            self._name=value
        else:
            raise Exception("sdfds")


class Magazine:
    
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        article_list = [article for article in Article.all if article.magazine == self]
        return article_list

    def contributors(self):
        my_contributors = [article.author for article in Article.all if article.magazine == self]
        filtered_contributors = list(set(my_contributors))
        return filtered_contributors

    def article_titles(self):
        my_titles = [article.title for article in Article.all if article.magazine == self]

        if my_titles == []:
            return None
        else:
            return my_titles

    def contributing_authors(self):
        author_count = {}
        duplicates =[]
        my_authors = [article.author for article in Article.all if article.magazine == self]

        for author in my_authors:
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        
        for author, count in author_count.items():
            if count >= 2:
                duplicates.append(author)
        
        if duplicates == []:
            return None
        else:
            return duplicates

     

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if type(value) == str and 2 <= len(value) <= 16:
            self._name = value

    
    @property
    def category(self):
        return self._category 
    
    @category.setter
    def category(self, value):
        if type(value) == str and 0 < len(value):
            self._category = value
    
  