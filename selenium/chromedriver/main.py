from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data_for_vessel(x):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
    vessel_url = f'https://www.marinetraffic.com/en/ais/details/ships/imo:{x}'
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\79291\\PycharmProjects\\pythonProject\\selenium\\chromedriver\\chromedriver.exe',
        options=options
    )
    driver.set_window_size(300, 800)
    try:
        driver.get(url=vessel_url)
        wait = WebDriverWait(driver, 10)
        click_agree = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()
        driver.execute_script('window.scrollTo(0, 1800)')
        lon = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[5]/b/a'))).text[11:20]
        lat = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[5]/b/a'))).text[:8]
        position_age = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[1]'))).text
        mouse_cursor = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[6]')))
        action = ActionChains(driver)
        action.move_to_element(mouse_cursor).perform()
        driver.execute_script('window.scrollTo(0, 3600)')
        vessel_img = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetailsHeader"]/div/div/div[1]/div/img'))).get_attribute('src')
        navigation_status = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[6]'))).text[21:]
        speed_heading = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_latestPositionSection"]/div[2]/div/div/div/div/div[1]/p[7]'))).text[14:]
        vessel_purpose = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="vesselDetails_summarySection"]/div[2]/div/div/div/p[10]'))).text
        vessel_name = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="shipName"]'))).text[6:]

        return {
                "lat": lat,
                "lon": lon,
                "position_age": position_age,
                "navigation_status": navigation_status,
                "speed_heading": speed_heading,
                "vessel_img": vessel_img,
                "vessel_purpose": vessel_purpose,
                "vessel_name": vessel_name
               }
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_data_for_aircraft(x):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
    aircraft_url = f'https://www.flightradar24.com'
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\79291\\PycharmProjects\\pythonProject\\selenium\\chromedriver\\chromedriver.exe',
        options=options
    )
    driver.set_window_size(500, 500)
    try:
        driver.get(url=aircraft_url)
        wait = WebDriverWait(driver, 10)
        driver.refresh()
        cookies = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler'))).click()
        search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchBox"]'))).send_keys(x.upper())
        flight_click = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#mapControlsApp > div > div:nth-child(7) > section > div > div.absolute.z-10.ml-0.overflow-hidden.shadow-default.w-\[375px\].min-h-10.rounded-2xl.mt-12 > div > div > div > div.contents > div > div:nth-child(2) > div:nth-child(2) > div > div > a > div.flex.items-center.justify-center.pl-2.pr-0 > button > svg'))).click()
        mouse_cursor = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]')))
        action = ActionChains(driver)
        action.move_to_element(mouse_cursor).perform()
        airline = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="airlineInfo"]/section/div[2]/div[1]/span[1]'))).text
        departure_city = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[1]/div/div[1]/div[1]/h3/span'))).text
        arrival_city = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[1]/div/div[1]/div[2]/h3/span'))).text
        scheduled_time_of_arrival = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[1]/div/div[3]/div[2]/div[1]/time/span'))).text
        scheduled_time_of_departure = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[1]/div/div[3]/div[1]/div[1]/time/span'))).text
        aircraft_img = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[1]/a/img'))).get_attribute('src')
        down_table = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[12]/div[2]/div[2]/div[1]/span[2]')))
        action.move_to_element(down_table).perform()
        altitude = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[7]/div[2]/div[1]/div[1]/div/span'))).get_attribute('data-tooltip-value')
        aircraft_bearing = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[7]/div[2]/div[2]/div[2]/span[2]'))).text
        aircraft_speed = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[9]/div[1]/div[2]/div[1]/div[1]/div/span'))).get_attribute('data-tooltip-value')
        aircraft_type = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[5]/div[2]/div[1]/div/span[2]'))).text
        lat = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[12]/div[2]/div[2]/div[1]/span[2]'))).text
        lon = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapStaticOverlays"]/div[3]/section[3]/section[12]/div[2]/div[2]/div[2]/span[2]'))).text
        return {
                "airline": airline,
                "route": f'{departure_city}-{arrival_city}',
                "scheduled_time_of_arrival": scheduled_time_of_arrival,
                "scheduled_time_of_departure": scheduled_time_of_departure,
                "aircraft_img": aircraft_img,
                "altitude": altitude,
                "aircraft_bearing": aircraft_bearing,
                "aircraft_speed": aircraft_speed,
                "aircraft_type": aircraft_type,
                "lat": lat,
                "lon": lon
        }
        # print(lat, lon, aircraft_type, scheduled_time_of_arrival, scheduled_time_of_departure, airline, altitude, aircraft_bearing, aircraft_speed, departure_city,arrival_city, aircraft_img)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    print(get_data_for_vessel('9691735'))


if __name__ == '__main__':
    main()