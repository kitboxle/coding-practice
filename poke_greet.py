import datetime

class poke_greet:
    def __init__(self, name='Trainer'):
        self.name           = name


    def time_of_day(self):
        date = datetime.datetime.now()
        time_of_day = 'null'
        hr = date.hour

        if 5 <= hr < 12:
            time_of_day = 'morning'
        elif 12 <= hr < 18:
            time_of_day = 'afternoon'
        elif 18 <= hr < 21:
            time_of_day = 'evening'
        else:
            time_of_day = 'night'
        
        return time_of_day


    def greet(self):
        d = datetime.datetime.now()
        h = d.hour
        t = self.time_of_day()
        if h >= 13:
            h -= 12

        if t == 'morning':
            print(f"Rise and shine, {self.name}.")
        elif t == 'afternoon':
            print(f"Good afternoon, {self.name}.")
            print('Did you have a good morning? Lets keep our drive up!')
        elif t == 'evening':
            print(f"Evening already {self.name}? Hope you got lots of work done!")
            print("Don't settle in just yet! Now's the time to push through!")
        else:
            print("What a great day you had! It's already nighttime!")
            print("You deserve a nice long rest, partner! I'll be here when you wake up.")
            return "Have a good night, and sleep well. We can get through this together."
        
        print('...')
        m = d.minute
        if d.minute <10:
            print(f"It's currently {h}:{0}{m}.")
        else:
            print(f"It's currently {h}:{m}.")
        

if __name__ == '__main__':
    say_hi = poke_greet('Ceana')
    say_hi.greet()