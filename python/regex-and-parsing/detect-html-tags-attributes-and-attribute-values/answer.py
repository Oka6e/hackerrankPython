from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    """Subclass to override handler methods."""
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("-> {} > {}".format(i[0], i[1])) 

if __name__ == '__main__':
    N = int(input()) # Number of lines in the HTML code snippet
    parser = MyHTMLParser()
    for _ in range(N):
        parser.feed(input())
