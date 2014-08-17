#/usr/bin/python

"""
Caitlin Rivers
cmrivers@vbi.vt.edu

Iterates through World Health Organization Disease Outbreak News
reports and prints sentences that contains numbers. If the DON
containts a table, it will output the table as a pandas df.
"""

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
import string


def make_table(table, save=False, meta=None):
    """
    Converts HTML table into pandas df.
    if save = True, outputs table as csv.
    """
    headings = [th.get_text() for th in table.find("tr").find_all("td")]

    datasets = []
    index = []
    for row in table.find_all("tr")[1:]:
        data = [td.get_text().strip() for td in row.find_all("td")]
        datasets.append(data)
    df = pd.DataFrame(datasets, columns=headings).dropna()

    if save:
        df.to_csv('./{}_{}.csv'.format(meta[1], meta[0]))


    return df


def extract(soup, save_table, meta):
    """
    """
    name = soup.title.string
    text = [x.text.strip() for x in soup.findAll('p')]
    table = soup.find('table')

    if table:
        tab = make_table(table, save_table, meta)
        print tab, '\n'
        return (text, tab)
    else:
        return (text, 'empty')



def show_numbers(text):
    """
    Display sentences with numbers
    """
    for paragraph in text:
        for sentence in paragraph.split('. '):
            if re.findall(r'\d+', sentence):
                print sentence


def main(date, save_table=False):
    """
    date = YYYY_MM_DD format. Accepts partials, e.g. "2014_08" or "2014_08_1".
    """
    year = date.split('_')[0]

    link = 'http://www.who.int/csr/don/archive/year/{}/en/'.format(year)
    initrequest = urllib2.Request(link)
    initresponse = urllib2.urlopen(initrequest)
    linksoup = BeautifulSoup(initresponse)

    for a in linksoup.find_all('a'):
        if '{}'.format(date) in a['href']:
            beginning = 'http://www.who.int/csr/don/'
            end = a['href'].split('/')[4:]
            end = '/'.join(end)
            link = beginning+end

            req = urllib2.Request(link)
            resp = urllib2.urlopen(req)
            soupout = BeautifulSoup(resp)

            date = soupout.find("meta", {"name":"webit_cover_date"})['content']
            disease = soupout.find("meta", {"name":"DC.keywords"})['content']
            disease = disease.split(', ')[0]

            print date, disease
            results = extract(soupout, save_table, (date, disease))
            show_numbers(results[0])

            print '## End of DON ##\n\n'

    return results


## Example - prints sentences that contain numbers, plus any tables for DONS published August 2014.
text = main('2014_08_')



