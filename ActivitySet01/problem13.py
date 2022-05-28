# Network Programming
# https://www.py4e.com/lessons/network
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

number_open=0
url = input("Enter address:")
while number_open <7:
    link_position=0
    if len(url)<1: url="http://py4e-data.dr-chuck.net/known_by_Ailidh.html"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        link_position+=1
        if link_position == 18:
            url=tag.get('href', None)
            print("Retrieving data From:",url)
            print("Content by:",tag.contents[0])
    number_open+=1
    