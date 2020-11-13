import requests as req
import zipfile

web = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'

class DataSnatch(object):

    def __init__(self, url, filename, new_file):
        self.url = url
        self.filename = filename
        self.new_file = new_file

    #Method for downloading the zipfile off the website
    def download(self):
        with req.get(self.url) as rq:
            with open(self.filename, 'wb') as file:
                file.write(rq.content)

    #Method for unzipping the downloaded file
    def un_zip(self):
        with zipfile.ZipFile(self.filename, 'r') as zip_ref:
            zip_ref.extractall(self.new_file)
data = DataSnatch(web, 'other_general_data.zip', 'new_zip')
data.download()
data.un_zip()

