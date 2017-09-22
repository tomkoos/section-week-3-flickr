import json

with open('sample_diction.json') as f:
    txt = f.read()
flick_response = json.loads(txt)


class Photo:
    def __init__(self, photo):
        self.username = photo['owner']['username']
        self.tags = [item['raw'] for item in photo['tags']['tag']]
        self.id = photo['id']
        self.title = photo['title']['_content']
        self.url = photo['urls']['url'][0]['_content']

    def __str__(self):
        return '{} by {}'.format(self.title, self.username)

    def __repr__(self):
        return ("Title: {} \n" +
                "Author: {} \n" +
                "URL: {} \n" +
                "ID: {}").format(self.title, self.username, self.url, self.id)

    def __contains__(self, val):
        return val in self.tags


photo = Photo(flick_response['photo'])
print('( tags )', photo.tags, sep='\n', end='\n\n')
print('( __str__ )', photo, sep='\n', end='\n\n')
print('( __repr__ )', repr(photo), sep='\n', end='\n\n')
print('( __contains__ )', 'Nature' in photo, sep='\n', end='\n\n')
