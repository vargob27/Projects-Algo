myNumber = 42;
myName = "Bryce";

print(myNumber);
print(myName);

def swap(x,y):
    i = x;
    x = y;
    y = i;
    return x, y;

print(swap(myNumber, myName));
print(myNumber);
print(myName);

def neg52to1066():
    for x in range(-52,1067):
        print(x);
    pass;

neg52to1066();

def beCheerful():
    return print('good morning!');

for i in range(98):
    beCheerful();

def multi3():
    for i in range(-300,0):
        if i%3 == 0:
            if i == -3 or i == -6:
                pass;
            else:
                print(i);
    pass;

multi3();

def while2000to5280():
    i = 2000;
    while i <= 5280:
        print(i);
        i+=1;
    pass;

while2000to5280();

def bday(x,y):
    if x == 1 and y == 31 or x == 31 and y == 1:
        print('How did you know?');
    else:
        print('Just another day...');

def leapYear(x):
    if x % 400 == 0:
        print(f"{x}" + ' is a leap year');
        return;
    if x % 4 == 0:
        if x % 100 == 0:
            print(f"{x}" + ' is not a leap year');
            return;
        else:
            print(f"{x}" + ' is a leap year');
            return;
    else:
        print(f"{x}" + ' is not a leap year');
leapYear(2001);

def printCount():
    list = [];
    for i in range(512,4096):
        if i % 5 == 0:
            list.append(i);
    print(list);
    print(len(list));

printCount();

def while6():
    i = 0;
    while i <= 60000:
        if i % 6 == 0:
            print(i);
        i+=1;
    pass;

while6();

def countingDojo():
    for i in range(1,101):
        if i % 5 == 0 and i % 10 ==0:
            print('Coding Dojo');
        elif i % 5 == 0:
            print('Coding');
        else:
            print(i);
    pass;
countingDojo();

def whatDoYouKnow(incoming):
    print(incoming);
    pass;
whatDoYouKnow("beans");

def odd300k():
    total = 0;
    i = -300000;
    while i <= 300000:
        if i % 2 != 0:
            total += i;
        i+=1;
    print(total);
odd300k();

def countdown4():
    for i in range(2016,1,-4):
        print(i);
countdown4();

def flexCount(lowNum, highNum, mult):
    for i in range(highNum,lowNum,-1):
        if i % mult == 0:
            print(i);
    pass;
flexCount(2,9,3);

def finalCount(param1,param2,param3,param4):
    while param2 <= param3:
        if param2 % param1 == 0 and param2 != param4:
            print(param2);
            param2 += 1;
        else:
            param2 += 1;
finalCount(3,5,17,9);
