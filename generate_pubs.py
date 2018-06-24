import json

def json_to_html(pub):
    print('<li>')
    print('<div class="publication">')
    if 'link' in pub:
        print('<a href="{0}">'.format(pub['link']))
    print('<img class="pub-thumb" src="images/thumbs/{0}" /></a>'.
            format(pub['thumbnail']))
    if 'link' in pub:
        print('</a>')
    if 'link' in pub:
        print('<a href="{0}">'.format(pub['link']))
    print('<h4 class="pub-title">{0}</h4>'.format(pub['title']))
    if 'link' in pub:
        print('</a>')

    print('<span class="pub-authors">')
    print(', '.join(pub['authors']))
    print('</span>') 
    print('<span class="pub-venue">In {0}</span>'.format(pub['venue']))
    print('<span class="pub-loc-date">{0}</span>'.format(pub['loc-date']))
    if 'publisher' in pub and len(pub['publisher']) > 0:
        print('<span class="pub-publisher">Publisher: {0}</span>'.format(pub['publisher']))
    print('</div>')
    print('</li>')

json_pub_str = open('publications.json').read()
json_pubs = json.loads(json_pub_str);


for pub in json_pubs:
    json_to_html(pub)
