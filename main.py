import os
import time


# define variables
logPath = 'D:\\pythonLogMonitor'
fileName = 'log.txt'
sleep_time = 1  # 1 sec, modify as per the requirement


def process(log_line):
    print(log_line)


# file follow class
class Follower:
    def __init__(self, filepath):
        self.filePath = filepath
        self.fileName = os.path.split(self.filePath)[1]
        self._pos = 0

    def poll(self):
        return self._pos < os.stat(self.filePath).st_size

    def follow(self):
        if not os.path.exists(self.filePath):
            raise f'{self.filePath} not found'
        if not self.poll():
            return []
        with open(self.filePath, 'r') as f:
            f.seek(self._pos)
            result = f.readlines()
            self._pos = f.tell()
        return result


# create file follower instance
follower = Follower(os.path.join(logPath, fileName))

while True:
    try:
        if follower.poll():
            print(f'File change detected sleeping {sleep_time} secs')
            time.sleep(sleep_time)
            lines = follower.follow()
            process(lines)

    except:
        print('file follow error!')
        break




