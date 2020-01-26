from slackbot.bot import listen_to
from utils.messages import history
from collections import defaultdict
import re


@listen_to('^[0-9]+$')
def listen_hi(msg):
    msg.react('+1')


@listen_to('summary')
def clear(msg):
    credit = re.compile(r'^[0-9]+$')
    d = defaultdict(int)
    for message in history():
        if message['text'] == 'clear':
            break
        if credit.match(message['text']):
            d[message['user']] += int(message['text'])
    if len(d) == 0:
        msg.send('お金の貸し借りはないよ！')
    elif len(d) == 1:
        user = list(d.keys())[0]
        msg.send('<@{}>は{}円をもらってね'.format(user, d[user]))
    elif len(d) == 2:
        m = min(d.values())
        M = max(d.values())
        if m == M:
            msg.send('2人とも' + str(m) + '円だよ')
        else:
            for u, v in d.items():
                if v == m:
                    from_user = u
                elif v == M:
                    to_user = u
            msg.send('<@{}>は<@{}>から{}円をもらってね'.format(to_user, from_user, M - m))
    else:
        msg.send("！！！なんかバグったよ！！！")


@listen_to('clear')
def clear(msg):
    msg.send('清算しました！')
