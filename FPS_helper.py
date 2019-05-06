import datetime

class FPS(object):
    """
    Class for FPS calculation
    """
    def __init__(self, interval):
        self._glob_start = None
        self._glob_end = None
        self._glob_numFrames = 0
        self._local_start = None
        self._local_numFrames = 0
        self._interval = interval
        self._curr_time = None
        self._curr_local_elapsed = None
        self._first = False

    def start(self):
        self._glob_start = datetime.datetime.now()
        self._local_start = self._glob_start
        return self

    def stop(self):
        self._glob_end = datetime.datetime.now()
        print('[INFO] elapsed time (total): {:.2f}'.format(self.elapsed()))
        print('[INFO] approx. FPS: {:.2f}'.format(self.fps()))

    def update(self):
        self._first = True
        self._curr_time = datetime.datetime.now()
        self._curr_local_elapsed = (self._curr_time - self._local_start).total_seconds()
        self._glob_numFrames += 1
        self._local_numFrames += 1
        if self._curr_local_elapsed > self._interval:
            print("> FPS: {}".format(self.fps_local()))
            self._local_numFrames = 0
            self._local_start = self._curr_time

    def elapsed(self):
        return (self._glob_end - self._glob_start).total_seconds()

    def fps(self):
        return self._glob_numFrames / self.elapsed()

    def fps_local(self):
        if self._first:
            return round(self._local_numFrames / self._curr_local_elapsed,1)
        else:
            return 0.0
