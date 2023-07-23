from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pymongo
class kitapyurdu():
    "That class entering kitapyurdu website and taking all book infos."
     
    def Browser(self):
        "That fonk. only returning browser driver not taking any object"

        return webdriver.Chrome()
    
    def Url_Adress(self):
        
        return "https://www.kitapyurdu.com"
        
    
    def Go_to_url(self,browser,url):
        "That fonk. only going to url"

        return browser.get(url)
    
    
    def Books_Publisher(self,browser)->None:
        "That fonk. taking book publisher name"

        books_publisher = []
        for i in range(20):
            jsCommend_publisher = f"""
            sayfa = sayfa = document.querySelectorAll("div.publisher > span > a > span")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_publisher_JSS = browser.execute_script(jsCommend_publisher)
            books_publisher.append(books_publisher_JSS)
        return books_publisher
    
    def Books_Info(self,browser)->None:
        "That fonk. taking book physical infos"

        books_info = []
        for i in range(20):
            jsCommend_info = f"""
            sayfa = sayfa = document.querySelectorAll("div.product-info")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_info_JSS = browser.execute_script(jsCommend_info)
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_info.append(books_info_JSS)
        return books_info
    
    def Book_Raiting(self,browser):
        "That fonk. taking book vote infos"
        books_rating=[]
        for i in range(20):
            jsCommend_raiting = f"""
            sayfa = sayfa = document.querySelectorAll("div.price > div.price-old.price-passive > span.value")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_raiting_JSS = browser.execute_script(jsCommend_raiting).split(",")[0] +" times votes" #dataya uygun diziliyor.
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_rating.append(books_raiting_JSS)
        return books_rating
    
    def Book_Producer_Price(self,browser)->None:
        "That fonk. taking book producer price"

        books_producer_price = []
        for i in range(20):
            jsCommend_producer_price = f"""
            sayfa = sayfa = document.querySelectorAll("div.price > div.price-old.price-passive > span.value")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_producer_price_JSS = browser.execute_script(jsCommend_producer_price) + " ₺"
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_producer_price.append(books_producer_price_JSS)
        return books_producer_price
    
    
    
    def Page_Number(self,browser):
        "That Fonk. taking page number "
        results = browser.find_element(By.CLASS_NAME,"results").text
        print(results)
        return results.split("(")[-1].split(")")[0].split(" ")[0]

    def Book_Name(self,browser):
        books_name = []
        for i in range(20):
            jsCommend_books_name = f"""
            sayfa = sayfa = document.querySelectorAll(".name.ellipsis")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_name_JSS = browser.execute_script(jsCommend_books_name)
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_name.append(books_name_JSS)
        return books_name
    
    
    def Books_Writer(self,browser)-> webdriver: 
        "That fonk. taking book writer name"

        books_writers = []
        for i in range(20):
            jsCommend_books_writers = f"""
            sayfa = sayfa = document.querySelectorAll(".author.compact.ellipsis")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_writers_JSS = browser.execute_script(jsCommend_books_writers)
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_writers.append(books_writers_JSS)
        return books_writers
    
    def Books_Website_Price(self,browser):
        "That fonk. taking book website price"

        books_website_price = []
        for i in range(20):
            jsCommend_website_price = f"""
            sayfa = sayfa = document.querySelectorAll(".price-new")[{i}].textContent;
            var yazar = sayfa;
            return yazar
            """
            books_website_price_JSS = browser.execute_script(jsCommend_website_price)
            # books_info_JSS = str(books_info_JSS)
            # books_info_JSS.split(" ")
            books_website_price_JSS= books_website_price_JSS.split(" ")[-1] + " ₺" # website price i istenen değerlere ceviriyorum.
            books_website_price.append(books_website_price_JSS) # 20 li listeye ekliyorum.

        return books_website_price
    
    #*********************************************************************************************************
    # FABRİKA METODU KULLANMAK İÇİN SADELEŞTİRMEYE ÇALIŞTIM AMA SON NUMARAYI ALAMADIĞIM İÇİN KODU BOZMAK İSTEMEDİM 
    #*********************************************************************************************************
    
    # def Data_Mane(self,last_number,page_number,browser):
    #     " that fonk. is taking website datas"
    #     print(f"son numara {last_number} sayfa sayısı {int(page_number)}")
    #     for j in range(last_number,int(page_number)):
    #         #print("Hata yok 174")

           
    #         book_names = self.Book_Name(browser)
    #         book_publishers = self.Books_Publisher(browser)
    #         book_writers =  self.Books_Writer(browser)
    #         book_infos = self.Books_Info(browser)
    #            #print("hata yok 179")
    #         book_pruducer_prices = self.Book_Producer_Price(browser)
    #         book_website_price = self.Books_Website_Price(browser)
                                   
    #         book_votes = self.Book_Raiting(browser)
    #         time.sleep(1)
    #         #self.Data_Save()
    #                 #print(f"""
    #                             #             {book_names}
    #                             #             {book_publishers}
    #                             #             {book_writers}
    #                             #             {book_infos}
    #                             #             {book_pruducer_prices}
    #                             #             {book_website_price}
    #                         #             {book_votes}
    #                             #         """)
    #         time.sleep(3)
    #         browser.get(f"https://www.kitapyurdu.com/index.php?route=product/category&page={j}&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC")
    #         #browser.find_element(By.CLASS_NAME,"next").click()
    #         time.sleep(3)
    #         print(f"Şuan bulunan sayfa {j}")
            
    
    #         # except:
    #         #     browser.get(f"https://www.kitapyurdu.com/index.php?route=product/category&page={last_number}&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC")
    #         # #return book_names,book_publishers,book_writers,book_infos,book_pruducer_prices,book_website_price,book_votes
    
    def Data_Save(self):
        "That fonk. saving data in MongoDB data base"

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["smartmaple"]
        mycol = mydb["kitapyurdu"]
        
        book_data = {"Page Number": last_number, "title": book_names, "publisher": book_publishers, "writers": book_writers, "infos": book_infos, "Producer Prices": book_pruducer_prices , "Website Price": book_website_price, "Rating": book_votes}
        return mycol.insert_one(book_data)
    
    def Mining(self)-> None:
        "That fonk. going to website and mine all data"
        global book_names, book_publishers, book_writers, book_infos, book_pruducer_prices, book_website_price, book_votes, last_number
        last_number = 1
        url = self.Url_Adress()
        browser = self.Browser()

        while True:

            try:

                time.sleep(2)
                browser.get(url)
                time.sleep(2)
                main_window = browser.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[1]/ul/li[1]/div[2]/ul/li[1]/span") #kayan pencere aktifleşmesi için konumu
                time.sleep(1)
                action_main_window = ActionChains(browser) # menu algoritmasının etkileşmesi için action kullanıyorum
                action_main_window.move_to_element(main_window).perform() # action kullanıyorum
                time.sleep(2)
                browser.find_element(By.XPATH,"//a[@href='kategori/kitap/1.html']").click() #kitaplara tıklyıorum
                time.sleep(2)
                browser.find_element(By.ID,"list_product_carousel_best_sell-view-all").click() #tüm kitaplara tıklıyor
                time.sleep(2)
                browser.find_element(By.XPATH,"/html/body/div[5]/div/div[3]/div/div[1]/div/label[2]/span").click() # stoktaki kitaplara tıklanıyor
                time.sleep(2)

                try:

                    page_number = self.Page_Number(browser) # sayfa numarası alınıyor
                    print(page_number)
                    print("satır 129 hata yok ")
                    for j in range(last_number,int(page_number)): #sayfalar arasında gezinmek son numarayı bulmak için e
                        last_number = j
                        book_names = self.Book_Name(browser)
                        book_publishers = self.Books_Publisher(browser)
                        book_writers =  self.Books_Writer(browser)
                        book_infos = self.Books_Info(browser)
                        book_pruducer_prices = self.Book_Producer_Price(browser)
                        book_website_price = self.Books_Website_Price(browser)
                        book_votes = self.Book_Raiting(browser)
                        
                        time.sleep(1)
                        self.Data_Save()
                        time.sleep(3)
                        #bir önceki sayfadan verileri aldıktan sonra, sonraki sayfaya gidiyor.
                        browser.get(f"https://www.kitapyurdu.com/index.php?route=product/category&page={last_number}&filter_category_all=true&path=1&filter_in_stock=1&filter_in_shelf=1&sort=purchased_365&order=DESC")
                        time.sleep(3)
                        #print(f"Şuan bulunan sayfa {last_number}")

                    #self.Data_Mane(last_number=last_number, browser=browser, page_number=page_number)                     
                except:
                    "Sayfadan veriler çekilirken ki oluşacak herhangi bir hatada tekrar kaldiği yerden devam etmesi için."
                    #print("expect sondan 2")
                    if last_number==0:
                        url = self.Url_Adress()
                    else:
                        #last_number = self.Data_Mane(last_number=last_number, browser=browser, page_number=page_number)
                        last_number = last_number
                        url = f"https://www.kitapyurdu.com/index.php?route=product/category&page={last_number}&filter_category_all=true&path=1&filter_in_stock=1&filter_in_shelf=1&sort=purchased_365&order=DESC"
            except:
                " sayfa verilerinin olduğu sayfaya giderkenki olasi hatalarda yada browser hatalarinda tekrar çalişmasi için yapilan blok "
                #print("expect sondan 1")
                url = self.Url_Adress()
                browser = self.Browser()
                if last_number==0:
                    url = self.Url_Adress()
                else:
                    last_number = last_number
                    #last_number = self.Data_Mane(last_number=last_number, browser=browser, page_number=page_number)
                    url = f"https://www.kitapyurdu.com/index.php?route=product/category&page={last_number}&filter_category_all=true&path=1&filter_in_stock=1&filter_in_shelf=1&sort=purchased_365&order=DESC"
    

kitapyurdu().Mining()