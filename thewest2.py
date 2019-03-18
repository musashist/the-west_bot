import smtplib
from email.mime.text import MIMEText
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from seleniumrequests import Chrome,Firefox
from selenium.webdriver.common.action_chains import ActionChains

# options = webdriver.ChromeOptions()
# options.binary_location = '/usr/bin/chromium'
# options.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()



lista_produktow = {'Złoto azteków': 'Poszukiwanie skarbu', 'Złoty pył': 'Wydobycie złota', 'Torba z łupami': 'Napad na pociąg', 'Drut kolczasty': 'Zakładanie ogrodzenia z drutu kolczastego',
                   'Fasola': 'Zbieranie fasoli', 'Torba ze zwykłym produktem': 'Prowadzenie biura handlowego', 'Skóra z bobra': 'Polowanie na bobry',
                   'Pułapka na bobry': 'Polowanie na bobry', 'Jagody': 'Zbieranie jagód', 'Skóra z bizona': 'Polowanie na bizony', 'Fajka pokoju': 'Rokowania pokojowe',
                   'Obraz': 'Włamanie', 'Cygara': 'Handlowanie z Indianami', 'Węgiel': 'Wydobycie węgla', 'Flaga Stanów Południowych': 'Budowa posiadłości',
                   'Garnek do gotowania': 'Ochrona wozu osadników', 'Ciepły posiłek': 'Naprawa wozów', 'Kukurydza': 'Zbieranie kukurydzy', 'Bawełna': 'Zbieranie bawełny',
                   'Ząb kojota': 'Polowanie na kojoty', 'Wybity ząb': 'Przeganianie rozbójników', 'Dokumenty': 'Gaszenie pożaru', 'Dynamit': 'Transport amunicji',
                   'Eliksir': 'Pracuj jako konował', 'Biżuteria damska': 'Napad', 'Wędka': 'Wędkowanie', 'Chorągiewka': 'Ustanawianie prawa własności', 'Mąka': 'Mielenie zboża',
                   'Piryt': 'Wydobycie złota', 'Kamienie półszlachetne': 'Poszukiwanie kamieni połszlachetnych', 'Szklanka wody': 'Rozkładanie torów', 'Złota figura': 'Sprzedaż broni Indianom',
                   'Zboże': 'Zbieranie zboża', 'Kamienie': 'Kamieniołom', 'Szynka': 'Pilnowanie świń', 'Młotek': 'Naprawianie płotów', 'Kajdanki': 'Strażnik więzienia',
                   'Krowi róg': 'Znakowanie bydła', 'Podkowa': 'Podkuwanie koni', 'Dzban': 'Kopanie studni', 'Lasso': 'Łapanie koni', 'Skóra': 'Garbowanie', 'Mapa': 'Eksploracja kontynentu', 'Maska': 'Łowca nagród',
                   'Medal zasłużonych': 'Służba w armii', 'Gwoździe': 'Budowa rancza', 'Gazeta': 'Sprzedaż gazet\nDrukowanie gazet', 'Ropa': 'Wydobycie ropy', 'Pomarańcze': 'Zbieranie pomarańczy',
                   'Paczka': 'Napad na powóz pocztowy', 'Kilof': 'Wydobycie żelaza', 'Kawałek kartki (Część 2)': 'Handel\nNapad\nPlądrowanie zwłok', 'Widły': 'Sprzątanie stajni', 'Hebel': 'Budowa trumien',
                   'Zegarek kieszonkowy': 'Okradanie ludzi', 'Trąbka pocztyliona': 'Pony-Express', 'Plakat': 'Rozwieszanie plakatów', 'Ćwierćdolarówka': 'Czyszczenie butów', 'Pióro kruka': 'Przepędzanie ptaków z pola',
                   'Pierścionek': 'Plądrowanie zwłok', 'Sukno': 'Handel', 'Szpulka drutu': 'Stawianie masztów telegraficznych', 'Naboje': 'Ochrona powozu pocztowego',
                   'Siodło': 'Ujeżdżanie koni', 'Łosoś': 'Połów ryb', 'Piła': 'Tartak', 'Okowy': 'Transport więźniów', 'Dzwon okrętowy': 'Pilotowanie parowców kołowych',
                   'Sierp': 'Koszenie pastwiska', 'Srebro': 'Wydobycie srebra', 'Młot kowalski': 'Budowa mostów', 'Towar przemycany': 'Ściganie bandytów',
                   'Śpiewnik': 'Misjonarze', 'Łopata': 'Kopanie grobów\nBudowa urządzeń nawadniających', 'Pal drewniany': 'Wyrównywanie koryta rzeki',
                   'Cukier': 'Zbieranie trzciny cukrowej', 'Stek': 'Hodowla krów', 'Tequila': 'Zbieranie agawy', 'Liście tytoniu': 'Zrywanie liści tytoniu', 'Pomidor': 'Zbieranie pomidorów',
                   'Skrzynka z narzędziami': 'Budowa wiatraków', 'Bransoleta z zębem': 'Polowanie na wilki', 'Bilet kolejowy': 'Budowa stacji kolejowej',
                   'Trofeum': 'Polowanie na grizzly', 'Pstrąg': 'Wędkowanie\nPołów ryb', 'Indyk': 'Polowanie na indyki', 'Flaga Stanów Północnych': 'Obserwacja fortecy',
                   'Whiskey': 'Pracuj jako żołdak', 'Drewno': 'Wycinka drzew', 'Wełna': 'Wypasanie owiec', 'Ziemniak': 'Wykopki', 'Siano': 'Karmienie bydła', 'Dynia': 'Zbieranie dyń',
                   'Borówki': 'Zbieranie borówek', 'Nasiona': 'Sadzenie drzew', 'Orle pióro': 'Zbieranie orlich piór', 'Indygo': 'Zbieranie indygo', 'Kwiat lotosu': 'Zbieranie kwiatów lotosu',
                   'Mięso kraba': 'Połów krabów', 'Kreda': 'Nauczanie', 'Gwiazda szeryfa': 'Pracuj jako szeryf', 'Ruda siarki': 'Wydobycie siarki', 'Zestaw do pokera': 'Hazardzista w trasie',
                   'Skóra węża': 'Polowanie na grzechotniki', 'Saletra': 'Kopanie saletry', 'Papierosy': 'Transport koni', 'Puchar za rodeo': 'Rodeo', 'Świadectwo zawarcia małżeństwa': 'Oszust matrymonialny',
                   'Skóra pumy': 'Polowanie na pumy', 'Rum': 'Transport alkoholu', 'Ołów': 'Wydobycie ołowiu', 'Drewniany krzyżyk': 'Budowa domu misyjnego', 'Metalowy żeton': 'Budowa kasyna',
                   'Wyrok śmierci': 'Pracuj jako Marshall', 'Forma drukarska': 'Napad na bank', 'Kwiat pokoju': 'Uwalnianie niewolników', 'Róża': 'Występ z Buffalo Billem', 'Jagnięca wełna': 'Wypasanie jagniąt',
                   'Przekłuta ryba': 'Łowienie oszczepem', 'Mielona kawa': 'Mielenie kawy', 'Pręty metalowe': 'Wydobycie żelaza', 'Kule dużego kalibru': 'Wytapianie kul', 'Godło': 'Rekrutowanie żołnierzy', 'Butelka mleka': 'Przewódź nowicjuszom',
                   'Szczypce': 'Budowa osady', 'Sekstant': 'Eksploracja Zachodu', 'Bandaże': 'Budowa lazaretu', 'Nuty': 'Pracuj jako pianista', 'Godło Pinkerton': 'Pracuj jako agent Pinkerton',
                   'Poroże': 'Tropienie zwierząt', 'Trąbka do musztry': 'Dowodzenie wojskiem', 'Perforowany kapelusz': 'Pracuj jako ochroniarz', 'Słownik': 'Pracuj jako tłumacz', 'Kamień graniczny': 'Kolonizowanie nowych obszarów',
                   'Dokumenty publiczne': 'Pracuj jako ambasador', 'Laska ceremonialna': 'Planowanie rezerwatu', 'Scyzoryk': 'Pracuj jako traper', 'Łuska': 'Pracuj jako rewolwerowiec', 'Ostre papryki': 'Zbieranie papryk',
                   'Sygnet': 'Pracuj dla loży', 'Duże majtki': 'Pracuj jako aktor sceniczny', 'Surowe jajka': 'Siłowanie na rękę', 'Detonator': 'Produkcja dynamitu', 'Czaszka': 'Pracuj jako grabarz',
                   'Białe rękawiczki': 'Pracuj jako funkcjonariusz pokoju', 'Dogmat': 'Pracuj jako kaznodzieja', 'Skóra aligatora': 'Polowanie na aligatory', 'Wódka': 'Destylacja alkoholu', 'Zniszczona ostroga': 'Zakładanie ostróg',
                   'Lejce': 'Pracuj dla Wells Fargo', 'Pismo': 'Prowadzenie ekspedycji'}
lista = {'Poszukiwanie skarbu':4, 'Wydobycie złota':1, 'Napad na pociąg':3, 'Zakładanie ogrodzenia z drutu kolczastego':2, 'Zbieranie fasoli':4,'Prowadzenie biura handlowego':4, 'Polowanie na bobry':2, 'Zbieranie jagód':1, 'Polowanie na bizony':4, 'Rokowania pokojowe':3, 'Włamanie':3, 'Handlowanie z Indianami':2, 'Wydobycie węgla':3, 'Budowa posiadłości':1, 'Ochrona wozu osadników':3, 'Naprawa wozów':1, 'Zbieranie kukurydzy':3, 'Zbieranie bawełny':3, 'Polowanie na kojoty':3, 'Przeganianie rozbójników':5, 'Gaszenie pożaru':4, 'Transport amunicji':2, 'Pracuj jako konował':1, 'Napad':1, 'Wędkowanie':1, 'Ustanawianie prawa własności':1, 'Mielenie zboża':1, 'Poszukiwanie kamieni połszlachetnych':2, 'Rozkładanie torów':1, 'Sprzedaż broni Indianom':3, 'Zbieranie zboża':4, 'Kamieniołom':1, 'Pilnowanie świń':1, 'Naprawianie płotów':1,
       'Strażnik więzienia':4, 'Znakowanie bydła':4, 'Podkuwanie koni':3, 'Kopanie studni':2, 'Łapanie koni':2,
         'Garbowanie':2, 'Eksploracja kontynentu':3, 'Łowca nagród':2, 'Służba w armii':1, 'Budowa rancza':2, 'Sprzedaż gazet':2, 'Wydobycie ropy':3, 'Zbieranie pomarańczy':3, 'Napad na powóz pocztowy':2, 'Wydobycie żelaza':4,'Sprzątanie stajni':3, 'Budowa trumien':1, 'Okradanie ludzi':2, 'Pony-Express':3, 'Rozwieszanie plakatów': 1, 'Czyszczenie butów':3, 'Przepędzanie ptaków z pola':1, 'Plądrowanie zwłok':2,
'Handel':1, 'Stawianie masztów telegraficznych':3, 'Ochrona powozu pocztowego':2, 'Ujeżdżanie koni':1,
         'Tartak':3, 'Transport więźniów':5, 'Pilotowanie parowców kołowych':3, 'Koszenie pastwiska':2,
         'Wydobycie srebra':2, 'Budowa mostów':2, 'Ściganie bandytów':1, 'Misjonarze':2, 'Kopanie grobów':1, 'Wyrównywanie koryta rzeki':2, 'Zbieranie trzciny cukrowej':1, 'Hodowla krów':3, 'Zbieranie agawy':1, 'Zrywanie liści tytoniu':2, 'Zbieranie pomidorów':2, 'Budowa wiatraków':5, 'Polowanie na wilki':1, 'Budowa stacji kolejowej':4, 'Polowanie na grizzly':2, 'Polowanie na indyki':1, 'Obserwacja fortecy':1, 'Pracuj jako żołdak':2, 'Wycinka drzew':2, 'Wypasanie owiec':2, 'Wykopki':4, 'Karmienie bydła':4, 'Zbieranie dyń':5, 'Zbieranie borówek':5, 'Sadzenie drzew':4, 'Zbieranie orlich piór':5, 'Zbieranie indygo':5, 'Zbieranie kwiatów lotosu':3, 'Połów krabów':4, 'Nauczanie':4, 'Pracuj jako szeryf':4, 'Wydobycie siarki':4, 'Hazardzista w trasie':2, 'Polowanie na grzechotniki':3, 'Kopanie saletry':5, 'Transport koni':4, 'Rodeo':3, 'Oszust matrymonialny':4, 'Polowanie na pumy':4, 'Transport alkoholu':5, 'Wydobycie ołowiu':6, 'Budowa domu misyjnego':3, 'Budowa kasyna':4, 'Pracuj jako Marshall':5, 'Napad na bank':4, 'Uwalnianie niewolników':4, 'Występ z Buffalo Billem':5, 'Wypasanie jagniąt':5, 'Łowienie oszczepem':5, 'Mielenie kawy': 5,'Wytapianie kul':2, 'Rekrutowanie żołnierzy':4, 'Przewódź nowicjuszom':1, 'Budowa osady':3, 'Eksploracja Zachodu':5, 'Budowa lazaretu':1, 'Pracuj jako pianista':1, 'Pracuj jako agent Pinkerton':5, 'Tropienie zwierząt':3, 'Dowodzenie wojskiem':5, 'Pracuj jako ochroniarz':2, 'Pracuj jako tłumacz':1, 'Kolonizowanie nowych obszarów':3, 'Pracuj jako ambasador':3, 'Planowanie rezerwatu':2, 'Pracuj jako traper':1, 'Pracuj jako rewolwerowiec':3, 'Zbieranie papryk':2, 'Pracuj dla loży':4, 'Pracuj jako aktor sceniczny':4, 'Siłowanie na rękę':2, 'Produkcja dynamitu':5, 'Pracuj jako grabarz':1, 'Pracuj jako funkcjonariusz pokoju':3, 'Pracuj jako kaznodzieja':2, 'Polowanie na aligatory':4, 'Destylacja alkoholu':5, 'Zakładanie ostróg': 4, 'Pracuj dla Wells Fargo':5, 'Prowadzenie ekspedycji':4}

def logowanie():
    login = ""  #enter your login
    senha = ""  #enter your password
    abas = 7
    driver.get("https://www.the-west.pl/")
    print(driver.title)
    user = driver.find_element_by_xpath("//input[@class='loginUsername'][@name='username']")
    user.send_keys(login)
    password = driver.find_element_by_xpath("//input[@class='loginPassword'][@name='userpassword']")
    password.send_keys(senha)
    password.submit()
    time.sleep(1)
    # driver.save_screenshot('screen1.png')
    try:
        driver.find_element_by_xpath("//A[@href='#'][text()='Muscotah']").click()
    except:
        print("Logowanie nie powiodlo sie")


def check_quests():
    product_list = []
    saloon = driver.find_element_by_xpath("//DIV[@class='border']")
    time.sleep(2)
    ActionChains(driver).move_to_element(saloon).click(saloon).perform()
    time.sleep(1)
    henry = driver.find_element_by_class_name("window-quest")
    boboiwindaws = henry.find_elements_by_tag_name("img")   #znajdz questgiverow
    for questgiver in range(len(boboiwindaws)):
        ActionChains(driver).move_to_element(boboiwindaws[questgiver]).click(boboiwindaws[questgiver]).perform()
        div1 = driver.find_element_by_class_name("tw2gui_window_content_pane")
        time.sleep(1)

        blok_do_petli = div1.find_element_by_class_name("tw2gui_scrollpane_clipper_contentpane")
        questy = blok_do_petli.find_elements_by_xpath("//A[@id]")
        time.sleep(1)
        for quest in questy:                                                                        #petla bioraca nazwy produktow ze wszystkich questow
            quest.click()
            reqs = driver.find_elements_by_css_selector(".quest_requirement")                           #produkty do zadan
            for req in reqs:
                try:
                    prod = get_product(req)
                    if prod != None:
                        product_list.append(prod)
                except:
                    pass
            time.sleep(2)
        try:
            driver.find_element_by_xpath("//div[@class='tw2gui_window tw2gui_win2 tw2gui_window_notabs window-quest_employer']/div[@class='tw2gui_window_buttons']/div[@class='tw2gui_window_buttons_close']").click()
        except:
            pass
        time.sleep(1)
    if(len(lista_produktow)) == 0:
        job = None
        position = None
    else:
        job = lista_produktow[product_list[0]]
        position = lista[job]
    driver.find_element_by_xpath("//div[@class='tw2gui_window tw2gui_win2 tw2gui_window_notabs building_quest']/div[@class='tw2gui_window_buttons']/div[@class='tw2gui_window_buttons_close']").click()
    return job,position


def get_product(req):
    if req.text == None:
        return None
    produkt = req.text[3:]
    for indeks in range(len(produkt)):
        if produkt[indeks].isdigit():
            produkt = produkt[:indeks - 1]
            return produkt
        else:
            indeks += 1
#wyciaga nazwe produktu z wymagan zadania


def praca(job, position):
    minimapa = driver.find_element_by_xpath("//div[@id='ui_minimap']")
    minimapa.click()
    time.sleep(1)
    wyszukiwanie = driver.find_element_by_xpath("//input[@type='text'][@class='tw2gui_jobsearch_string']")
    nazwa_pracy = job
    wyszukiwanie.send_keys(nazwa_pracy)             #wyszukiwanie lokalizacji wybranej pracy
    time.sleep(1)
    localisation = driver.find_element_by_xpath("(//IMG[@src='https://westpl.innogamescdn.com/images/map/minimap/icons/miniicon_jobs.png?2'])[1]")

    loc_data = localisation.get_attribute("class")
    garb, x, reszta = loc_data.partition("x-")
    x, spacja, reszta = reszta.partition(" ")
    y = reszta[2:]
    print(x)
    print(y)
    localisation.click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='tw2gui_window tw2gui_win2 tw2gui_window_notabs minimap empty_title']/div[@class='tw2gui_window_buttons']/div[@class='tw2gui_window_buttons_close']").click()



    liczba = position         #wykextractowac z klasy obiektu mlotka wspolrzedne skupiska prac
    driver.find_element_by_css_selector(".image.posx-%s.posy-%s" %(x,y)).click()
    time.sleep(1)
    driver.find_element_by_xpath("(//IMG[@class='jobimg'])[%s]" %liczba).click()
    time.sleep(2)

    element4 = driver.find_element_by_xpath("//div[@class='job-amount-plus']")              #rozkazy pracy
    element4.click()
    element3 = driver.find_element_by_xpath("//div[@class='job_durationbar job_durationbar_short']").click()


def pojedynek():
    pojedynek_blok = driver.find_element_by_xpath("//div[@class='dock-image duels']")
    ActionChains(driver).move_to_element(pojedynek_blok).click(pojedynek_blok).perform()
    time.sleep(2)

    poje2 = []
    for x in poje1:
        ajdi = x.get_attribute("id")
        poje2.append(ajdi)
    print(poje1)
    print(poje2)

    for i in range(3):
        poje1 = driver.find_element_by_xpath("(//div[@class='dl_fightbutton'])[2]")
        ActionChains(driver).move_to_element(poje1).click(poje1).perform()
        time.sleep(2)

def hotel():
    driver.find_element_by_css_selector(".dock-image.city").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='cities']/div[@class='city inlineblock']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//area[@class='imagemap_area imagemap_hotel']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='selectroom-bedroom']").click()
    driver.find_element_by_xpath("//div[contains(text(), 'Sen')]").click()


def main():
    logowanie()
    time.sleep(1)
    try:
        odbierz = driver.find_element_by_xpath("//*[contains(text(), 'Odbierz')]")                                          #pozbycie sie ekranow po logowaniu
        ActionChains(driver).move_to_element(odbierz).click(odbierz).perform()
        time.sleep(1)
        ok = driver.find_element_by_xpath("//div[@class='dialog-button']/div[@class='quest_reward_button normal']").click()
        time.sleep(1)
    except:
        pass


    hp = driver.find_element_by_css_selector(".status_bar.health_bar").text                                                 #sprawdzenie aktualnych zycia i energii
    #hp = hp_bar.text
    current_hp,bubu, whole_hp = hp.partition("/")
    energy = driver.find_element_by_css_selector(".status_bar.energy_bar").text
    current_energy,bububu, whole_energy = hp.partition("/")
    time.sleep(2)


    if int(current_energy) < 8:                                            #jezeli energia postaci jest zbyt niska by wykonywac prace, zostaje ona skierowana do hotelu
        hotel()
    else:                                                             #wpp idzie wykonywac prace
        job, position = check_quests()
        time.sleep(1)
        if job == None:
            job = "Wędkowanie"
            position = "1"
        praca(job,position)


main()

