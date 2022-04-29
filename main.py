# Create your own adventure with python here
def control_flow():
    print("Hello traveler, what is your name?")
    x = input()
    print("Hello, " + x + "! We're planning on going to Asia tonight. Would you like to go to Vietnam or Korea?")
    y = input()
    if y.lower() == 'vietnam':
        print("Nice! I'm from Vietnam! Let's eat right away when we land. Should we eat Pho or Sandwiches?")
        z = input()
        if z.lower() == 'pho':
            print(
                "You are so basic, but let's do it. Did you want to travel by Car or Motorcycle?")
            a = input()
            if a.lower() == 'car':
                print(
                    "Good choice, small chance of getting in a fatal accident! Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
            elif a.lower() == 'motorcycle':
                print("Vietnam streets are too dangerous to navigate through and we have died... Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
        elif z.lower() == 'sandwiches':
            print("Hopefully the bread doesn't scratch the roof of our mouths. There's a sandwich place by where we're staying so we can just grab it before heading home. Do you want Beef, Pork, or Vegan?")
            a = input()
            if a.lower() == 'beef':
                print(
                    "Good choice as I am born the year of the Ox! Would you like the play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
            elif a.lower() == 'pork':
                print(
                    "I am allergic to pork and you have killed me... Would you like the play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
            elif a.lower() == "vegan":
                print("Healthy person I see. Well you have fun with your grass and leaves, I'm going to find something else to eat! Would you like the play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
    elif y.lower() == 'korea':
        print("I've always wanted to go to Korea! I heard they have good food! What kind of dish should we try, Soup or Meat?")
        z = input()
        if z.lower() == 'soup':
            print(
                "I love soup, I'm in the mood for Kimchi or Pork Blood! Which one would you like?")
            a = input()
            if a.lower() == 'kimchi':
                print("Healthy and delicious! Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
            elif a.lower() == 'pork blood':
                print(
                    "You can just eat mine too... Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
        elif z.lower() == 'meat':
            print("Carnivore I see, should we get Chicken or Pork Belly?")
            a = input()
            if a.lower() == 'chicken':
                print(
                    "I heard the fried chicken there is better than the ones in America! Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")
            elif a.lower() == 'pork belly':
                print(
                    "We have to have soju as well, let's go! Would you like to play again? Yes or No?")
                b = input()
                if b.lower() == 'yes':
                    control_flow()
                if b.lower() == 'no':
                    print("Bye " + x + "!")


control_flow()
