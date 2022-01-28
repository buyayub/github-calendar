import sys, requests
from html.parser import HTMLParser

user = sys.argv[1]

def cal_raw(user):
    # gets user's svg data from github.
    r = requests.get('https://www.github.com/' + user)
    cal = "" 

    if r.status_code != 200:
        cal = "STATUS: " + str(r.status_code)
    else:
        start = r.text.find('<svg width="828" height="128" class="js-calendar-graph-svg">')
        end = r.text.find('</svg>', start)
        cal = r.text[start:end+6]

    return cal

#test = '<svg width="100" height="100"><g transform="translate(10,20)" data-test="4"><rect height="10px" width="10px" /></g></svg>'

class calParser(HTMLParser):
    # handles calendar stuff
    cal_struct = [] 

    def handle_starttag(self, tag, attribute):
        tag_struct = [tag]

        for attr in attribute:
            tag_struct.append(attr)

        self.cal_struct.append(tag_struct)

    def handle_startendtag(self, tag, attribute):
        tag_struct = [tag]

        for attr in attribute:
            tag_struct.append(attr)

        self.cal_struct.append(tag_struct)
    
    def handle_endtag(self, tag):
        self.cal_struct.append(tag)

def cal_strip(cal, attr):
    for element in cal:
        if isinstance(element, list):
            for i in element:
                if isinstance(i , tuple):
                    if i[0] == attr:
                        element.remove(i)
    return cal  

cal_raw = cal_raw(user)
'''
parser = calParser()
parser.feed(cal_raw)
cal = parser.cal_struct
cal = cal_strip(cal, 'rx')
cal = cal_strip(cal, 'ry')
'''
print(cal_raw)

    
#def cal_json(cal_raw):
    # turns user's data into json
     

