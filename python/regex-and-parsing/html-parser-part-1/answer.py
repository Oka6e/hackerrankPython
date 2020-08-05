from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    """Creates a subclass and override handler methods"""
    def handle_starttag(self, tag, attrs):
        print("Start :", tag) 
        for i in attrs:
            print("-> {} > {}".format(i[0], i[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :" , tag)
        for i in attrs:
            print("-> {} > {}".format(i[0], i[1]))

if __name__ == '__main__':
    N = int(input()) # Number of lines
    parser = HTMLParser()
    for _ in range(N):
        parser.feed(input())
