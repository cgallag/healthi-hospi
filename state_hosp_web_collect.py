'''
Created on Jul 14, 2013

@author: cagallagher
'''

import urllib2
from bs4 import BeautifulSoup

def getsoup(link):
    response = urllib2.urlopen(link)
    html = response.read()
    soup = BeautifulSoup(html) 
    return soup

def hosp_list_parser(link):
    soup = getsoup(link)
    hosp_list = soup.find(id='hospital_lists')
    hosp_links = hosp_list('td')
    hosp_link_dict = {}
    for link in hosp_links:
        hosp_a_tag = link.find('a')
        hosp_name = unicode(hosp_a_tag.string)
        try:
            hosp_loc = link.contents[len(link.contents)-1].strip(', ').split(',')
        except:
            print len(link.contents), link.contents
            hosp_loc = ['', ''] #In case a location is not provided for the hospital
        hosp_link_dict[hosp_name] = {
                                     'link': unicode(hosp_a_tag['href']),
                                     'city': hosp_loc[0]
                                     }
    return hosp_link_dict
    
def state_list_parser(link):
    soup = getsoup(link)
    info = soup.find(id='CPHMain_LabelContentCenter')
    state_table = info.find('table').find_all('a')
    state_dict = {}
    for state in state_table:
        state_dict[state.string] = { 'href': state['href'] }

    for state in state_dict:
        try:
            hosp_list_dict = hosp_list_parser(state_dict[state]['href'])
            print state #, hosp_list_dict
            state_dict[state]['hosp_list'] = hosp_list_dict
        except:
            print state
            raise

    print hosp_list_dict
     
def main():
    state_list_parser("http://www.hospitaldreamjobs.com/10/Hospital_Websites.aspx")
                                        

if __name__ == '__main__':
    main()