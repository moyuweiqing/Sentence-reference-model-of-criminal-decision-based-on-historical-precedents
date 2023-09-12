from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

page_num = 8
# page_num = 14

def switch_new_windows_handle(chrome):
    windows = chrome.window_handles
    chrome.switch_to.window(windows[-1])

def switch_old_windows_handle(chrome):
    windows = chrome.window_handles
    chrome.switch_to.window(windows[0])

def get_judgement(chrome,title):

    judgetext = ''
    if_judge = True
    text_xpath_num = 1

    while if_judge:
        try:
            xpath = f'//*[@id="_view_1541573883000"]/div/div[1]/div[3]/div[{text_xpath_num}]'
            text = chrome.find_element(by=By.XPATH, value=xpath).text
            judgetext += text
            judgetext += '\n'
            text_xpath_num += 1
        except:
            if_judge = False

    with open(f'./result/{title}.txt', mode='w', encoding='utf-8') as f:
        f.write(judgetext)
        f.close()

    print('finished', title)

def click_next_page(chrome):
    global page_num
    if page_num < 14:
        chrome.find_element(by=By.XPATH, value=f'//*[@id="_view_1545184311000"]/div[18]/a[{page_num}]').click()
        page_num += 1
    else:
        chrome.find_element(by=By.XPATH, value='//*[@id="_view_1545184311000"]/div[18]/a[14]').click()
    print('finished, ', page_num)

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
    chrome_driver = r"D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    for loop in range(1, 100):
        for i in range(3, 18):
            title = driver.find_element(by=By.XPATH, value=f'//*[@id="_view_1545184311000"]/div[{i}]/div[2]/h4/a').text
            main_text = driver.find_element(by=By.XPATH, value=f'//*[@id="_view_1545184311000"]/div[{i}]/div[4]/h4').text
            if main_text == '[不公开理由]':
                continue

            driver.find_element(by=By.XPATH, value=f'//*[@id="_view_1545184311000"]/div[{i}]/div[2]/h4/a').click()
            switch_new_windows_handle(driver)
            time.sleep(1)
            get_judgement(driver, title=title)
            driver.close()
            switch_old_windows_handle(driver)
            time.sleep(1)
        click_next_page(driver)
        time.sleep(2)