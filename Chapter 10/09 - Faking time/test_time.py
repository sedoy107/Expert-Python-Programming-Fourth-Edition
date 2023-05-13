import time
from datetime import timedelta, datetime

from freezegun import freeze_time


@freeze_time("1988-02-05 05:10:00")
def test_time():
    '''Using decorator'''
    assert(datetime.now() == datetime(1988, 2, 5, 5, 10, 0))

def test_with_time():
    '''Using context manager'''
    with freeze_time("1988-02-04 05:11:00") as frozen:
        assert(datetime.now() == datetime(1988, 2, 4, 5, 11, 0))
        frozen.move_to("1988-02-05 05:11:00")
        frozen.tick()
        frozen.tick(timedelta(hours=1))
        assert(datetime.now() == datetime(1988, 2, 5, 6, 11, 1))

def test_freeze():
    '''Using start and stop'''
    freezer = freeze_time("2015-12-09 23:33:01")
    freezer.start()
    assert(datetime.now() == datetime(2015, 12, 9, 23, 33, 1))
    freezer.stop()
    assert(datetime.now() != datetime(2015, 12, 9, 23, 33, 1))
