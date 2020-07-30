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


def main():
    tomato = TomatoClock()
    tomato.summary()

    if is_change_work_and_break_time():
        tomato.set_work_minutes()
        tomato.set_break_minutes()
        


if __name__ == "__main__":
    main()