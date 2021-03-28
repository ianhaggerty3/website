import csv
import datetime

STORY_FILE = 'exponent_stories.csv'
HTML_FILE = 'exponent_stories.html'

DATE_POS = 0
HEADLINE_POS = 1
URL_POS = 2
CATEGORY_POS = 3
PREVIEW_POS = 4

WRESTLING_CATEGORY = 'Wrestling'
WBB_CATEGORY = "Women's Basketball"

class Article:
    def __init__(self, date: str, headline: str, url: str, category: str, preview: str):
        print(date)
        self.date = datetime.datetime.strptime(date, '%m/%d/%Y')
        self.headline = headline.strip()
        self.url = url.strip()
        self.category = category.strip()
        self.preview = True if preview.strip() == 'TRUE' else False

    def __str__(self):
        return f'              <text>{self.date.strftime("%d %B %Y")}: </text>\n' + \
               f'              <a href="{self.url}">{self.headline}</a>\n' + \
               f'              <br>\n'

    def __repr__(self):
        return self.headline

if __name__ == '__main__':
    with open(STORY_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        articles = [None] * (sum(1 for _ in reader) - 1)

        csvfile.seek(0)
        
        # get rid of headers
        next(reader)

        for i, row in enumerate(reader):
            articles[i] = Article(row[DATE_POS], row[HEADLINE_POS], row[URL_POS], row[CATEGORY_POS], row[PREVIEW_POS])
    
    with open(HTML_FILE, 'w') as htmlfile:
        # TODO: sort by datetime
        wrestling_recaps = sorted(filter(lambda article: article.category == WRESTLING_CATEGORY and article.preview is False, articles), key=lambda item:item.date, reverse=True)
        wrestling_previews = sorted(filter(lambda article: article.category == WRESTLING_CATEGORY and article.preview is True, articles), key=lambda item:item.date, reverse=True)
        wbb_recaps = sorted(filter(lambda article: article.category == WBB_CATEGORY, articles), key=lambda item:item.date, reverse=True)
        
        htmlfile.write('            <h3>Wrestling Recaps</h3>\n')
        htmlfile.writelines(list(map(lambda entry: str(entry), wrestling_recaps)))

        htmlfile.write('            <br>\n')
        htmlfile.write('            <h3>Wrestling Previews</h3>\n')
        htmlfile.writelines(list(map(lambda entry: str(entry), wrestling_previews)))

        htmlfile.write('            <br>\n')
        htmlfile.write("            <h3>Women's Basketball</h3>\n")
        htmlfile.writelines(list(map(lambda entry: str(entry), wbb_recaps)))
        

        
        
        


