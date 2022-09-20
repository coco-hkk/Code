"""互斥锁 threading.Lock()"""
import threading
import time

mutex = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, counter):
        super(MyThread, self).__init__()
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        print("Start thread " + self.name)

        # 获取锁，用于线程同步
        mutex.acquire()
        self.task_process(self.counter, 3)
        # 释放锁，开启下一个线程
        mutex.release()

        # 等价于
        # with mutex:
        #    self.task_process(self.counter, 3)

    def task_process(self, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (self.name, time.ctime(time.time())))
            counter -= 1


if __name__ == '__main__':
    threads = []

    # 创建新线程
    thread1 = MyThread(1)
    thread2 = MyThread(2)

    # 开启新线程
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成
    for t in threads:
        t.join()

    print("Main thread exit.")
