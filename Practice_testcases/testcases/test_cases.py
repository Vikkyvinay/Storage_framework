import sys
sys.path.append("D:\\Practice_testcases")
from lib import main
from lib import logger
import pytest

log = logger.get_logger(__name__)



def test_get_up_time():
        main_instance = main.Mainlub()
        result = main_instance.get_server_uptime()
        if "up" in result:
            log.info("Setup is up")
            assert True
        else:
            log.error("Fail")
            assert False


def test_get_server_drives():
    main_instance = main.Mainlub()
    result = main_instance.get_server_drives()
    expected = ['sda', 'sdb', 'sdc', 'sdd', 'sde', 'sdf', 'sdg', 'sdh']
    if result == expected:
        log.info("test pass")
        assert True
    else:
        log.error("test fail")
        assert False
    # for drive in result:
    #     if drive in expect:
    #         log.info("Passed")
    #         assert True
    #     else:
    #         log.info("Fail")
    #         assert False


def test_raid_controller():
    main_instance = main.Mainlub()
    result = main_instance.raid_controller()
    if "LSI" not in result:
        assert False


def test_bios_version():
    main_instance = main.Mainlub()
    result = main_instance.check_bios()
    if "1.2" in result:
        assert True
    else:
        assert False


def test_os_version():
    main_instance = main.Mainlub()
    result = main_instance.check_os_version()
    if "Ubuntu" in result:
        assert True
    else:
        assert False
