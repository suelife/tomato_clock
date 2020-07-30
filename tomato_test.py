import time
import datetime


class TomatoClock:
    def __init__(self):
        self.__WORK_MINUTES = 25
        self.__BREAK_MINUTES = 5

    def summary(self):
        print("=====Summary=====")
        print(f"工作時間: {self.__WORK_MINUTES}")
        print(f"休息時間: {self.__BREAK_MINUTES}")
        print("=================")
        print()
    
    def set_work_minutes(self, minutes):
        self.__WORK_MINUTES = minutes

    def set_break_minutes(self, minutes):
        self.__BREAK_MINUTES = minutes

    def timer(self, minutes):
        start_time = time.perf_counter()
        while True:
            past_second = round(time.perf_counter() - start_time)
            remaining_second = int(minutes * 60 - past_second)
            self.__prograssbar(remaining_second)
            if remaining_second <= 0:
                print()
                break
            time.sleep(1)
    
    def __prograssbar(self, total_second):
        minute, second = int(total_second/60), int(total_second%60)
        remaining_time = datetime.time(minute=minute, second=second)
        remaining_text = remaining_time.strftime("%M:%S")
        print(f"剩餘時間: {remaining_text}", end="\r")

    def notify_message(self, content):
        print(f"{str(content)}")

    def run(self):
        print()
        self.timer(self.__WORK_MINUTES)
        self.notify_message("Time to break!")
        self.timer(self.__BREAK_MINUTES)
        self.notify_message("Time to work!")
    
if __name__ == "__main__":
    tomato = TomatoClock()
    tomato.set_work_minutes(1)
    tomato.run()
    # tomato.timer()
    # tomato.notify_message("Time to break.")