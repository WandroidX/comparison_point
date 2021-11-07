import bs4, requests

yout=requests.get('https://www.y2mate.com/es38')

parsing=bs4.BeautifulSoup(yout.text,'html.parser')
vidtit=parsing.select('#bootstrap-themes > div.container-overflow-wrap > div:nth-child(2) > div > div > div.row.row-padded.row-bordered.row-centered.p-l-md.p-r-md > div > div > h2 > strong')


print(vidtit[0].text.strip())
