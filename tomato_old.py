import os
import time
import yaml


class TomatoClock:
    def __init__(self, settings):
        if settings is not None:
            self.__WORK_MINUTES = settings["work_minutes"]
            self.__BREAK_MINUTES = settings["break_minutes"]
        else:
            self.__WORK_MINUTES = 25
            self.__BREAK_MINUTES = 5

    def run(self):
        start_time = time.perf_counter()
        # while True:


def raise_system_exit(content=None):
    if content is not None:
        print(f"{str(content)}")
    raise SystemExit(os.system("pause"))


def load_setting():
    SETTING_FILE = "settings.yml"
    settings = None

    try:
        with open(SETTING_FILE, "r") as f:
            stream = yaml.load(f, yaml.SafeLoader)
            settings = {
                "work_minutes": int(stream["work_minutes"]),
                "break_minutes": int(stream["break_minutes"])
            }
    except FileNotFoundError:
        pass
    except ValueError:
        raise_system_exit(f"請填入整數。")
    except KeyError:
        print(f"參數名稱錯誤，只支援以下參數。")
        print(f"參數名稱: work_minutes, break_minutess")
        raise_system_exit()
    except Exception as err:
        raise_system_exit(f"{err}")

    return settings


def main():
    settings = load_setting()
    # print(settings)
    tomato = TomatoClock(settings)
    # tomato.run()


if __name__ == "__main__":
    main()
