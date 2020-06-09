def generate_hashtag(s):
    try:
        if len(s) == 0 or len(s) > 140:
            return False
        else:
            return '#' + ''.join([x.strip() for x in s.title()])
    except:
        pass
