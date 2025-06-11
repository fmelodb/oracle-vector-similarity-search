import os
import oracledb
import sys
from dotenv import load_dotenv

load_dotenv()

def connect_database():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    dsn = os.getenv("DB_URL")

    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)        
        print("\nConnection successful!\n")
        return connection
    except Exception as e:
        print("Connection failed!\n")
        exit(1)
        
connection = connect_database()

print("Creating schema objects\n")

with connection.cursor() as cursor:
    sql = ["drop table if exists test_data",
           """create table test_data (
                id        int generated as identity primary key,
                info      varchar2(128) not null,
                embedding vector)"""
           ]
    
    for s in sql:
        try:
            cursor.execute(s)
        except oracledb.DatabaseError as e:
            if e.args[0].code != 942:
                raise
    
    cursor.execute("select column_name, data_type from user_tab_columns where table_name = 'TEST_DATA'")
    columns = cursor.fetchall()

    print("Created table TEST_DATA with columns:\n")      
    for column in columns:
        print(f"  {column[0]} ({column[1]})")   
    
    
    data_to_insert = [
        ("New York is in New York",),
        ("Los Angeles is in California",),
        ("Chicago is in Illinois",),
        ("Houston is in Texas",),
        ("Phoenix is in Arizona",),
        ("Philadelphia is in Pennsylvania",),
        ("San Antonio is in Texas",),
        ("San Diego is in California",),
        ("Dallas is in Texas",),
        ("San Jose is in California",),
        ("Austin is in Texas",),
        ("Jacksonville is in Florida",),
        ("Fort Worth is in Texas",),
        ("Charlotte is in North Carolina",),
        ("San Francisco is in California",),
        ("Denver is in Colorado",),
        ("Boston is in Massachusetts",),
        ("El Paso is in Texas",),
        ("Nashville is in Tennessee",),
        ("Detroit is in Michigan",),
        ("Oklahoma City is in Oklahoma",),
        ("Portland is in Oregon",),
        ("Las Vegas is in Nevada",),
        ("Memphis is in Tennessee",),
        ("Louisville is in Kentucky",),
        ("Baltimore is in Maryland",),
        ("Milwaukee is in Wisconsin",),
        ("Tucson is in Arizona",),
        ("Atlanta is in Georgia",),
        ("Kansas City is in Missouri",),
        ("Colorado Springs is in Colorado",),
        ("Miami is in Florida",),
        ("Oakland is in California",),
        ("Minneapolis is in Minnesota",),
        ("Tampa is in Florida",),
        ("New Orleans is in Louisiana",),
        ("Cleveland is in Ohio",),
        ("Anaheim is in California",),
        ("Honolulu is in Hawaii",),
        ("Pittsburgh is in Pennsylvania",),
        ("Orlando is in Florida",),
        ("Ferraris are often red",),
        ("Teslas are electric",),
        ("Fiat 500 are small",),
        ("Jeeps are good for off-road",),
        ("Volvos are known for safety",),
        ("BMWs are sporty",),
        ("Mercedes-Benz cars are luxurious",),
        ("Toyotas are reliable",),
        ("Subarus have all-wheel drive",),
        ("Mazdas are fun to drive",),
        ("Chevrolets are American",),
        ("Fords are popular in the USA",),
        ("Lamborghinis are exotic",),
        ("Porsches are fast",),
        ("Hondas are fuel efficient",),
        ("Kias are affordable",),
        ("Hyundais have long warranties",),
        ("Audis have quattro technology",),
        ("Nissans are practical",),
        ("Cadillacs are premium",),
        ("Buicks are comfortable",),
        ("Acuras are sporty and reliable",),
        ("Infinitis are luxury Nissans",),
        ("Mini Coopers are compact",),
        ("Land Rovers are good for off-road",),
        ("Maseratis are Italian luxury cars",),
        ("Alfa Romeos are stylish",),
        ("Dodge Chargers are powerful",),
        ("Chevy Corvettes are iconic sports cars",),
        ("Volkswagens are German engineered",),
        ("Peugeots are French",),
        ("Citroëns are innovative",),
        ("Renaults are popular in Europe",),
        ("Suzukis are compact",),
        ("Mitsubishis are versatile",),
        ("Saabs are Swedish",),
        ("Skodas are practical",),
        ("Seat cars are Spanish",),
        ("Bugattis are extremely fast",),
        ("Rolls-Royces are ultra-luxurious",),
        ("Bentleys are handcrafted luxury cars",),
        ("Bananas are yellow",),
        ("Kiwis are green inside",),
        ("Oranges are orange",),
        ("Apples can be red or green",),
        ("Strawberries are sweet and red",),
        ("Blueberries are small and blue",),
        ("Lemons are sour and yellow",),
        ("Pineapples have spiky skin",),
        ("Watermelons are juicy and red inside",),
        ("Cherries are small and red",),
        ("Grapes can be green or purple",),
        ("Mangoes are tropical and sweet",),
        ("Peaches are fuzzy and sweet",),
        ("Coconuts have hard shells",),
        ("Papayas are orange inside",),
        ("Avocados are creamy and green",),
        ("Blackberries are dark and sweet",),
        ("Raspberries are red and tart",),
        ("Pomegranates have many seeds",),
        ("Passion fruits are tangy",),
        ("Cranberries are tart and red",),
        ("Dragon fruits are exotic and pink",),
        ("Tangerines are easy to peel",),
        ("Dogs are loyal",),
        ("Cats are independent",),
        ("Horses have four legs",),
        ("Mice are small",),
        ("Elephants have trunks",),
        ("Lions are called the king of the jungle",),
        ("Tigers have stripes",),
        ("Bears hibernate in winter",),
        ("Foxes are clever",),
        ("Rabbits have long ears",),
        ("Kangaroos carry babies in pouches",),
        ("Giraffes have long necks",),
        ("Zebras have black and white stripes",),
        ("Monkeys are playful",),
        ("Gorillas are strong",),
        ("Chimpanzees use tools",),
        ("Dolphins are intelligent",),
        ("Whales are the largest animals",),
        ("Sharks have sharp teeth",),
        ("Eagles have sharp vision",),
        ("Parrots can mimic sounds",),
        ("Cows give milk",),
        ("Pigs are intelligent",),
        ("Chickens lay eggs",),
        ("Ducks can swim",),
        ("Frogs can jump far",),
        ("Crocodiles live in rivers",),
        ("Alligators are similar to crocodiles",),
        ("Bats are the only flying mammals",),
        ("Bees make honey",),
        ("Mumbai is in India",),
        ("Mumbai is the financial capital of India",),
        ("Mumbai is famous for Bollywood",),
        ("Mumbai is known for its street food",),
        ("Dubai is in the United Arab Emirates",),
        ("Dubai is famous for its skyscrapers",),
        ("Dubai has the Burj Khalifa",),
        ("Dubai has artificial islands",),
        ("Oracle CloudWorld is an annual conference",),
        ("Oracle CloudWorld is hosted by Oracle",),
        ("Oracle CloudWorld focuses on cloud technology",),
        ("Oracle CloudWorld features keynote sessions",),
        ("Oracle CloudWorld offers hands-on labs",),
        ("Oracle CloudWorld brings together IT professionals",),
        ("Oracle CloudWorld showcases Oracle innovations",),
        ("Oracle CloudWorld is held in Las Vegas",),
        ("Oracle CloudWorld covers database advancements",),
        ("Oracle CloudWorld includes networking opportunities",),
        ("Oracle CloudWorld presents customer success stories",),
        ("Mercury is the closest planet to the Sun",),
        ("Venus is the hottest planet",),
        ("Earth is the only planet with life",),
        ("Mars is known as the red planet",),
        ("Jupiter is the largest planet",),
        ("Saturn has beautiful rings",),
        ("Uranus rotates on its side",),
        ("Neptune is blue and windy",),
        ("Pluto is a dwarf planet",),
        ("Mercury has no moons",),
        ("Venus is similar in size to Earth",),
        ("Earth has one moon",),
        ("Mars has two moons",),
        ("Jupiter has a giant red spot",),
        ("Saturn has many moons",),
        ("Uranus is an ice giant",),
        ("Neptune has strong storms",),
        ("Pluto was reclassified as a dwarf planet",),
        ("Jupiter has the most moons",),
        ("Saturn is less dense than water",)
    ]
    
    connection.autocommit = True
    cursor.executemany("insert into test_data (info) values (:1)", data_to_insert)
    
    print(f"\nInserted {len(data_to_insert)} rows into test_data table.\n")