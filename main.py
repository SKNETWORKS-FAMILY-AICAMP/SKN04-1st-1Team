from crawling.company_crawling import company_crawling_start
from crawling.car365_crawling import car365_crawling_start
from crawling.hyundaimobis_2 import hyundai_crawling_start
from crawling.car_reg_info import car_reg_info_start

if __name__ == "__main__":
    # car365크롤링
    car365_crawling_start()
    # company크롤링
    company_crawling_start()
    # 현대모비스크롤링
    hyundai_crawling_start()
    # carRegInfo크롤링
    car_reg_info_start()
