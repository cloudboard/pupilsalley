# 45 23 * * * /local/home/zghong/.servant/npr_transcript/npr_transcript.sh
/home/zghong/.local/python-3.6.3/bin/scrapy runspider /home/zghong/.servant/npr_transcript/npr_transcript.py -o /home/zghong/.servant/npr_transcript/data/$(date +%Y-%m-%d).json > /dev/null 2>&1
