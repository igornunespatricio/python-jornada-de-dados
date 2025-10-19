import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource
from lib.classes.JsonSource import JsonSource

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()


def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    json_source.check_for_new_files()


schedule.every(10).seconds.do(check_for_new_files)


while True:
    schedule.run_pending()
    time.sleep(1)
