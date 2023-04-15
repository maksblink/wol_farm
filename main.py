import time
from functions import singing_in, farming_1_square, water_1_square, open_farm, exit_farm, kick_scythe, \
    kick_okay_after_harvest, waiter

login = input("Login: ")
password = input("Password: ")
server = input("Server: ")

singing_in(server, login, password)

while True:
    farming_1_square("carrot", 1)
    waiter(550, 660, 1000)
    farming_1_square("carrot", 2)
    waiter(550, 660, 1000)
    farming_1_square("carrot", 3)
    waiter(550, 660, 1000)
    water_1_square(3)
    waiter(550, 660, 1000)
    water_1_square(2)
    waiter(550, 660, 1000)
    water_1_square(1)

    waiter(336, 337)
    open_farm(1)
    waiter(1, 2)
    exit_farm()
    waiter(336, 337)
    open_farm(3)
    waiter(1, 2)
    exit_farm()
    waiter(336, 337)

    open_farm(1)
    waiter(550, 660, 1000)
    kick_scythe()
    waiter(550, 660, 1000)
    kick_okay_after_harvest()
    waiter(550, 660, 1000)
    exit_farm()

    waiter(550, 660, 1000)
    open_farm(2)
    waiter(550, 660, 1000)
    kick_scythe()
    waiter(550, 660, 1000)
    kick_okay_after_harvest()
    waiter(550, 660, 1000)
    exit_farm()

    waiter(550, 660, 1000)
    open_farm(3)
    waiter(550, 660, 1000)
    kick_scythe()
    waiter(550, 660, 1000)
    kick_okay_after_harvest()
    waiter(550, 660, 1000)
    exit_farm()
