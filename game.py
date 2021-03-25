import pyfiglet
from random import choice
from users import data
from os import system

def get_second_user(name_to_avoid: str) -> dict:
    copy = list(filter(lambda x: not x["name"] == name_to_avoid, data.copy()))
    return choice(copy)

if __name__ == "__main__":
    try:
        wins = 0
        options = {"A": None, "B": None}
        prev_answer = None
        ran = False
        while True:
            system("clear")
            print(pyfiglet.figlet_format("Higher\nLower"))
            if ran: print(f"That's right! Current score: {wins}")
            if not options["A"]: options["A"] = choice(data)
            else: options["A"] = prev_answer
            options["B"] = get_second_user(options["A"]["name"])
            prev_answer = options["A"] if max(options["A"]["follower_count"], options["B"]["follower_count"]) == options["A"]["follower_count"] else options["B"]
            answer = "A" if prev_answer["name"] == options["A"]["name"] else "B"
            name1, name2 = options["A"]["name"], options["B"]["name"]
            print("Compare A: {}, a {}, from {}".format(name1, options["A"]["description"], options["A"]["country"]))
            print(pyfiglet.figlet_format("vs."))
            print("Against B: {}, a {}, from {}".format(name2, options["B"]["description"],options["B"]["country"]))
            if not input("Who has more followers? Type 'A' or 'B': ") == answer:
                print("Awww man the right answer was {} with staggering {} followers!.....".format(answer, prev_answer["follower_count"]))
                break
            wins += 1
            ran = True
        print(f"Wins collected: {wins}")
    except TypeError:
        print("You entered invalid data!...")