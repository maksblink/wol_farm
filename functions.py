from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time
import random

driver = webdriver.Chrome("C:\drivers\chromedriver.exe")

driver.get("https://www.wolnifarmerzy.pl/")


def waiter(mint, maxt, scalar=1):
    t = (random.randint(mint, maxt)) / scalar
    minutes = int(t / 60)
    seconds = t - 60 * minutes

    print("Time left is ", minutes, " minutes and ", seconds, "seconds")

    if minutes > 1:
        for i in range(minutes):
            time.sleep(60)
            print("Time left is ", (minutes - i - 1), " minutes and ", seconds, "seconds\n")
        time.sleep(seconds)
    else:
        time.sleep(t)


def singing_in(wserver, wlogin, wpass):
    waiter(100, 200, 1000)
    server = WebDriverWait(driver, 3).until(
        ES.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[5]/div[2]/form/div[1]/select")))
    server.send_keys(wserver)

    waiter(100, 200, 1000)
    login = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div[2]/form/div[2]/input")
    login.send_keys(wlogin)

    waiter(100, 200, 1000)
    password = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div[2]/form/div[3]/input")
    password.send_keys(wpass)

    waiter(100, 200, 1000)
    click_sing_in = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div[2]/form/input[3]")
    click_sing_in.click()


def singing_out():
    waiter(350, 750, 1000)
    sing_out = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/div/div[6]/div[2]")
    sing_out.click()


def open_farm(farm_number):
    waiter(390, 450, 1000)
    # /html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[1]/div[1]/div[2]
    if farm_number == 1:
        farm_path = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[1]/div[1]/div[1]"
    elif farm_number == 2:
        farm_path = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[1]/div[1]/div[3]"
    elif farm_number == 3:
        farm_path = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[1]/div[1]/div[4]"

    farm = WebDriverWait(driver, 3).until(
        ES.presence_of_element_located((By.XPATH, farm_path)))
    farm.click()

    waiter(250, 350, 1000)
    garden = driver.find_element(By.ID, "gardenarea")
    fields = garden.find_elements(By.XPATH, "./*")
    return fields


def exit_farm():
    waiter(350, 390, 1000)
    x = driver.find_element(By.XPATH,
                            "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[2]/div[7]")
    x.click()


def kick_planter():
    waiter(130, 230, 1000)
    plant = driver.find_element(By.XPATH,
                                "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[2]/div[5]/span[1]")
    plant.click()


def kick_irrigator():
    waiter(110, 180, 1000)
    irrigator = driver.find_element(By.XPATH,
                                    "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[2]/div[5]/span[2]")
    irrigator.click()


def kick_cloud():
    waiter(210, 280, 1000)
    cloud = driver.find_element(By.XPATH,
                                "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[2]/div[5]/span[4]")
    cloud.click()


def kick_scythe():
    scythe = driver.find_element(By.XPATH,
                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[2]/div[5]/span[5]")
    scythe.click()


def kick_okay_after_harvest():
    waiter(200, 345, 1000)
    okay = driver.find_element(By.XPATH,
                               "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[58]/div[1]/div/div/div/div[3]/div[2]/button")
    okay.click()


def farming_1_square(crops, farm):
    fields = open_farm(farm)

    print(f"\n\n\n\nSTART FARMING {crops}\n\n\n\n")
    c = 0
    while True:
        c += 1
        print("ROUND ", c, "\n\n")
        waiter(110, 200, 1000)
        if crops == "carrot":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[17]")
        elif crops == "cucumber":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[1]")
        elif crops == "radish":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[12]")
        elif crops == "strawberry":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[12]")
        elif crops == "tomato":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[13]")
        elif crops == "onion":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[14]")
        elif crops == "spinach":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[17]")
        elif crops == "cauliflower":
            crops_to_plant = driver.find_element(By.XPATH,
                                                 "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/div[4]/div[17]")

        crops_to_plant.click()

        kick_planter()

        bad_ids = ["field120"]
        bad_ids = []

        for field in fields:
            element_id = field.get_attribute("id")

            if element_id not in bad_ids:
                waiter(20, 45, 1000)
                a = ActionChains(driver)
                a.move_to_element(field).perform()

                waiter(25, 60, 1000)
                field.click()

        waiter(110, 145, 1000)
        exit_farm()
        return


def water_1_square(farm):
    fields = open_farm(farm)

    print(f"\n\n\n\nSTART IRRIGATION\n\n\n\n")
    c = 0
    while True:
        c += 1
        print("ROUND W ", c, "\n\n")
        waiter(110, 200, 1000)

        kick_irrigator()

        bad_ids = ["field120"]
        bad_ids = []

        for field in fields:
            element_id = field.get_attribute("id")

            if element_id not in bad_ids:
                waiter(20, 45, 1000)
                a = ActionChains(driver)
                a.move_to_element(field).perform()

                waiter(20, 35, 1000)
                field.click()

        waiter(110, 155, 1000)
        exit_farm()
        return
