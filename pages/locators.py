from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTER_LINK = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a/span')
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(1) > a > span")
    FILTER_BY_PET_NAME = (By.XPATH, '//*[@id="petName"]')
    FILTER_BY_TYPE = (By.XPATH, '//*[@id="typesSelector"]')
    DOG = (By.XPATH, '//*[@id="pv_id_2_0"]')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')
    DETAILS = (By.CLASS_NAME, 'p-button-label')
    COMMENTS = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[3]/form/div/div/div[2]/div[1]')
    SECOND_PAGE = (By.CSS_SELECTOR,"#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > "
                                   "div.p-paginator.p-component.p-paginator-bottom > span > "
                                   "button.p-paginator-page.p-paginator-element.p-link.p-highlight")
    THIRD_PAGE = (By.CSS_SELECTOR, "#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > "
                                   "div.p-paginator.p-component.p-paginator-bottom > span > button:nth-child(3)")
    LIKE_FOR_FIRST_PET = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/span[1]')
    PREWIEW_FOTO_OF_FIRST_PET = (By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/span/div')
    DETAILS_FIST_PET = (By.CSS_SELECTOR,
                        "#app > main > div > div.p-dataview.p-component.p-dataview-grid.ml-3.mr-3 > "
                        "div.p-dataview-content > div > div:nth-child(1) > div > "
                        "div.product-grid-item-bottom.grid.flex-row.mt-3 > div:nth-child(1) > button > span")


class LoginPageLocator:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, 'p-button-label')
    ICON = (By.XPATH, '//*[@id="app"]/header/div/div/img')


class RegisterPageLocator:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]')
    PASSWORD_BUTTON = (By.CSS_SELECTOR, '#password > input')
    CONFIRM_PASSWORD_BUTTON = (By.CSS_SELECTOR, '#confirm_password > input')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'p-button-label')
    DELETE_BTN = (By.CSS_SELECTOR, "#app > main > div > div > div.p-dataview-header > div > div:nth-child(2) > button")
    YES_BTN_POPUP = (By.CSS_SELECTOR,
                     "body > div.p-confirm-popup.p-component.p-ripple-disabled > div.p-confirm-popup-footer > "
                     "button.p-button.p-component.p-confirm-popup-accept.p-button-sm > span")


class ProfilePageLocator:
    PLUS_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    NAME_NEW_PET = (By.XPATH, '//*[@id="name"]')
    SELECT_A_TYPE = (By.XPATH, '//*[@id="typeSelector"]')
    SELECT_A_GENDER = (By.XPATH, '//*[@id="genderSelector"]')
    AGE = (By.XPATH, '//*[@id="age"]/input')
    SUBMIT_NEW_PET = (By.CSS_SELECTOR,
                      '#app > main > div > div > form > div > div.p-card-body > div.p-card-footer > '
                      'button.p-button.p-component.p-button-success > span.p-button-label')
    CANCEL_NEW_PET = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]/span[2]')
    TYPE_OF_NEW_PET = (By.XPATH, '//*[@id="pv_id_2_1"]')
    MALE = (By.XPATH, '//*[@id="pv_id_3_0"]')
    FEMALE = (By.XPATH, '//*[@id="pv_id_3_1"]')
    PROFILE = (By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a/span[2]')
    DELETE = (By.CSS_SELECTOR,
              "#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > div > "
              "div.product-list-action > button.p-button.p-component.p-button-danger > span.p-button-label")
    POPAP_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]/span')
    EDIT = (By.CSS_SELECTOR,
            "#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > div > "
            "div.product-list-action > button:nth-child(1) > span.p-button-label")
    NAME = (By.XPATH, '//*[@id="name"]')
    SAVE_EDIT = (By.CSS_SELECTOR,
                 "#app > main > div > form > div > div.p-card-body > div.p-card-footer > button > span.p-button-label")
    QUIT = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a/span[2]')
