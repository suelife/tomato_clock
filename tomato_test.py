import time
import datetime


class TomatoClock:
    def __init__(self):
        self.__WORK_MINUTES = 25
        self.__BREAK_MINUTES = 5

    def summary(self):
        print(f"WORK_MINUTES: {self.__WORK_MINUTES}")
        print(f"BREAK_MINUTES: {self.__BREAK_MINUTES}")
    
    def set_work_minutes(self, minutes):
        self.__WORK_MINUTES = minutes

    def set_break_minutes(self, minutes):
        self.__BREAK_MINUTES = minutes

    def timer(self):
        start_time = time.perf_counter()
        while True:
            deviation_second = round(time.perf_counter() - start_time)
            remaining_second = self.__WORK_MINUTES * 60 - deviation_second
            if remaining_second <= -1:
                print()
                break
            else:
                self.__prograssbar(remaining_second)
            time.sleep(1)
    
    def __prograssbar(self, total_second):
        minute, second = int(total_second/60), int(total_second%60)
        remaining_time = datetime.time(minute=minute, second=second)
        remaining_text = remaining_time.strftime("%M:%S")
        print(f"剩餘時間: {remaining_text}", end="\r")

    def notify_message(self, content):
        print(f"{str(content)}")

    
if __name__ == "__main__":
    tomato = TomatoClock()
    tomato.set_work_minutes(0.1)
    tomato.timer()
    tomato.notify_message("Time to break.")