class Tweet(ModelFactory):
    def __


class TweetProcessor:
    def __init__(self):
        self.filename = 'tweets.txt'

    def processes(self):
        with open('tweets.txt', 'r') as fs:
            if fs.mode == 'r':
                content = fs.readlines()

        for line in content:
            print('a line')


if __name__ == "__main__":
    tps = TweetProcessor()
    tps.processes()
