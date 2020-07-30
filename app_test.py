from tomato_test import TomatoClock


def is_change_work_and_break_time():
    contrast_talbe = {
        "Y": True,
        "N": False,
    }

    while True:
        print("是否修改工作及休息時間?")
        ans = input("(Y/N): ").upper()
        if ans in ["Y", "N"]:
            ans = contrast_talbe[ans]
            break
        
    return ans


def set_minutes(text):
    while True:
        try:
            minutes = float(input(f"輸入{text}時間(單位分鐘): "))
            break
        except ValueError:
            print("請輸入數字")
        except Exception as e:
            print(e)

    return minutes


def main():
    tomato = TomatoClock()
    tomato.summary()

    if is_change_work_and_break_time():
        tomato.set_work_minutes(set_minutes("工作"))
        tomato.set_break_minutes(set_minutes("休息"))
        tomato.summary()
        


if __name__ == "__main__":
    # main()
    set_minutes()