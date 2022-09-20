"""threading 模块创建线程
threading.currentThread()   返回当前的线程变量。
threading.enumerate()       返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount()     返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread 类提供了以下方法:

run()           用以表示线程活动的方法。
start()         启动线程活动。
join([time])    等待至线程中止。这阻塞调用线程直至线程的 join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive()       返回线程是否活动的。
name            线程名。
"""
import threading
import time


class MyThread (threading.Thread):
    def __init__(self, counter):
        super(MyThread, self).__init__()
        self._stop_event = threading.Event()
        self.counter = counter

    def run(self):
        print("Thread {} begin.".format(self.name))
        self.task_process(self.counter, 5)
        print("Thread {} end.".format(self.name))

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def task_process(self, delay, counter):
        while counter:
            if self.stopped():
                break

            time.sleep(delay)
            print("%s: %s" % (self.name, time.ctime(time.time())))
            counter -= 1


if __name__ == '__main__':
    # 创建新线程
    thread1 = MyThread(1)
    thread2 = MyThread(2)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Main thread exit.")
