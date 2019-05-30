# 45 23 * * * /local/home/zghong/.servant/npr_transcript/npr_transcript.sh
today=$(date +%Y-%m-%d)
/home/zghong/.local/python-3.6.3/bin/scrapy runspider /home/zghong/.servant/npr_transcript/npr_transcript.py -o /home/zghong/.servant/npr_transcript/data/$today.json > /dev/null 2>&1

if [ -f "/home/zghong/.servant/npr_transcript/data/$today.json" ]; then
    cd /home/zghong/.servant/

    cp npr_transcript/data/$today.json npr_transcript/data/latest.json
    git add .
    git commit -m "npr_transcript: $today"
    GIT_SSH_COMMAND="ssh -i ~/.ssh/id_cloudboard" git push
fi
