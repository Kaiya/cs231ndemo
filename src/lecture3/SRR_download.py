import re
from urllib.request import urlopen
import os
from sys import argv


def main(geo):
    response = urlopen("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={}".format(geo))
    pattern = re.compile("<a href=\"ftp://ftp-trace(.*?)\">\(ftp\)</a>")
    ftp_address = re.search(pattern, response.read().decode('utf-8')).group(1)
    os.system(' wget -nd -r 1 -A *.sra ' + ftp_address)


if __name__ == '__main__':
    main(argv[1])
