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


test = '<svg width="100" height="100"><g transform="translate(10,20)" data-test="4"><rect height="10px" width="10px" /></g></svg>'

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

parser = calParser()
parser.feed(test)
cal = parser.cal_struct

'''
def cal_strip(cal):
    # strips out all the extra calendar stuff except important data
    for element in cal:
        if len(element) > 1:
            for i in range(element[1:]):
                if element[i][0] not in ['width', 'height', 'x', 'y', 'class', 'data-count', 'data-level']:
                    element.remove(i)
                 
'''       
                

    
#def cal_json(cal_raw):
    # turns user's data into json
     

