import numpy as np
import pandas as pd

from pdfminer.high_level import extract_text
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from io import StringIO


def read_makro_invoice(pdf_file):
        output_string = StringIO()
        parser = PDFParser(pdf_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        lines = output_string.getvalue().splitlines()


        # find the line which contains the word "Artikelnummer"
        start_line = [i for i, line in enumerate(lines) if 'Artikelnummer' in line][0]

        # find the line which contains the word "Aantal stuks"
        end_line = [i for i, line in enumerate(lines) if "Aantal stuks" in line][0]


        # dataframe that will contain all articles and their information
        articles_dtypes = np.dtype([('Statiegeld', bool), 
                                    ('Artikelnummer', str), 
                                    ('Artikelomschrijving', str),
                                    ('Prijs st/kg', str),
                                    ('Stuks per eenheid', str), 
                                    ('Prijs per collo', str),
                                    ('Aantal', str),
                                    ('Bedrag', str),
                                    ('BTW', str),
                                    ('Code korting', str),
                                    ('Prijs st/kg na korting', str)])
        articles = pd.DataFrame(np.empty(0, dtype=articles_dtypes))


        # go trough all lines containing articles and extract the information
        for i, line in enumerate(lines[start_line+3:end_line]):
            if "----------------" in line:
                end_articles = i
                break

            if not line=="" and not "ARTIKELEN---" in line:
                split_line = line.split()[::-1]
                article = pd.DataFrame(np.empty(1, dtype=articles_dtypes))
                
                first_entry = split_line.pop()
                if first_entry == '+':
                    article['Artikelnummer'] = split_line.pop()
                    article['Statiegeld'] = True
                else:
                    article['Artikelnummer'] = first_entry
                    article['Statiegeld'] = False

                # find stuks per eenheid indicator
                for i, entry in enumerate(split_line):
                    if len(entry) == 2 and entry.isupper():
                        article['Stuks per eenheid'] = split_line[i+1]
                        article['Prijs st/kg'] = split_line[i+2]
                        article['Prijs per collo'] = split_line[i-1]
                        article['Aantal'] = split_line[i-2]
                        article['Bedrag'] = split_line[i-3]
                        article['BTW'] = split_line[i-4]
                        article['Artikelomschrijving'] = " ".join(split_line[:i+2:-1])

                        split_line = split_line[:i-4]
                        if split_line[0] == 'A':
                            split_line = split_line[1:]
                        if len(split_line) == 2:
                            article['Code korting'] = split_line[1]
                            article['Prijs st/kg na korting'] = split_line[0]
                        if len(split_line) == 1:
                            article['Code korting'] = ""
                            article['Prijs st/kg na korting'] = split_line[0]
                        break
                
                # append article to articles
                articles = pd.concat([articles, article], ignore_index=True)

        return articles


def to_list(df):
    result = []
    for index, row in df.iterrows():
        result.append({
            "article_number": int(row['Artikelnummer']),
            "name": row['Artikelomschrijving'], 
            "price": float(row['Prijs st/kg'].replace(',','.')), 
            "stock": int(float(row['Stuks per eenheid'].replace(',','.'))*int(row['Aantal'])),
            "product_group": 1
        })
    return result