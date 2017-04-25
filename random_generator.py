# coding=utf-8
from faker import Faker, Factory
import random
import time
import datetime

fake = Factory.create(locale='ru_Ru')
allname = fake.name().split()
email = fake.safe_email()
phone = random.randint(1016000000, 1016999999)
dt = datetime.datetime.now()
tranzakt = str("6" + time.strftime("%d%m%H%M"))
tranzakt2 = str(time.mktime(dt.timetuple()))