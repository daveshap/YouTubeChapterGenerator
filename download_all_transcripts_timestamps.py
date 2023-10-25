import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
from pprint import pprint


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def clean_title(title):
    contraband = [':','/','\\','?','"']
    for c in contraband:
        title = title.replace(c,'')
    return title


channel_id = 'UCvKRFNawVcuz4b9ihUTApCg'
videos = scrapetube.get_channel(channel_id)
print(videos)


for video in videos:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video['videoId'])
        text = ['[{} - {}] {}'.format(i['start'], i['start'] + i['duration'], i['text']) for i in transcript]
        block = '\n\n'.join(text)
        title = clean_title(video['title']['runs'][0]['text'])
        print(title)
        save_file('timestamped/%s.txt' % title, block)
    except Exception as oops:
        print(video['title'], oops)