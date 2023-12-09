"""
*************************
@Purpose :: This module is an API to connect remote Linux host and get the repsonse

@Author         ::

@revision History

@DATE [ DD/MM/YYYY]               @Name                   @Remarks

10-06-2023                       winteck                 Adding New modules for testing product
"""
import datetime
import re
import sys
from os.path import dirname, abspath
from lib import logger
from lib.connect import exec_cmd

sys.path.append(dirname(dirname(abspath(__file__))))

log = logger.get_logger(__name__)


class Mainlub:
    """
    this class containes number of methods to validate the server components and features
    """
    def __init__(self):
        pass
    def get_server_uptime(self):
        """
        this method is used get all the server uptime
        :return: float
        """
        server_uptime = exec_cmd("uptime")
        out = re.search(r"up\s*(\d+)", server_uptime)
        if out:
            log.info("Server up %s", out)
            return out.group()
        else:
            log.info("Server not up %s", out)
            return "Not found!"


    def get_server_drives(self):
        """
        this method is used get all the drives list
        :return: list
        """
        server_drives = exec_cmd("lsblk")
        out1 = re.findall(r"(sd[a-z])\s+",server_drives)
        log.info("Listing the server drivers %s", out1)
        return out1


    def get_fw_version(self, drive_name):
        """
        this method is used to get firmware version for drives
        :return:
        """
        fw_version = exec_cmd(f"smartctl -a {drive_name}")
        drive_version = re.search(r"Revision:\s*(\w+)", fw_version)
        if drive_version:
            log.info("drive information %s", drive_version.group(1))
            return drive_version.group(1)
        else:
            log.info("drive information not found %s", drive_version)
            return "Not found"


    def create_raid(self, raid_name, raid_level, raid_devices, raid_drivers):
        """
        this method is used to create raid
        :return:
        """
        if raid_devices[0]:
            out = exec_cmd(f"echo 'y'|mdadm --create {raid_name} --level={raid_level} --force --raid-devices={raid_devices} {raid_drivers}")
            log.info("Raid Created")
            return out
        else:
            out = exec_cmd(f"echo 'y'|mdadm --create {raid_name} --level={raid_level} --raid-devices={raid_devices} {raid_drivers}")
            log.info("Raid Created")
            return out


    def delete_raid(self,raid_name):
        """
        this method is used to stop raid
        :return:
        """
        out = exec_cmd(f"echo 'd'|mdadm --stop {raid_name}")
        log.info("Raid Stop")
        return out


    def raid_controller(self):
        """
        this method is used to read the raid controller version
        :return:
        """
        out = exec_cmd("lspci|grep -i 'raid'")
        log.info("raid controller version %s", out)
        return out


    def check_bios(self):
        """
        this method is used to find the bios version
        :return: float
        """
        server_bios = exec_cmd("dmidecode -t 0")
        bios_version = re.search(r"BIOS Revision:\s*(\d+.\d+)", server_bios)
        if bios_version:
            log.info("bios information %s", bios_version)
            return bios_version.group()
        else:
            log.info("bios information not found %s", bios_version)
            return "Not found"


    def check_os_version(self):
        """
        this method is used to find the installed os version
        :return: string
        """
        os_release = exec_cmd("cat /etc/os-release")
        os_name_version = re.search(r"PRETTY_NAME=\"\w+\s*(.+)\"", os_release)
        if os_name_version:
            log.info("os information %s", os_name_version)
            return os_name_version.group()
        else:
            log.info("os information not found %s", os_name_version)
            return "Not Found"


    def check_bmc_version(self):
        """
        this method is used to find the BMC version
        :return: str
        """
        bmc_info = exec_cmd("dmidecode -t 2")
        bmc_version = re.search("Version:.+", bmc_info)
        if bmc_version:
            log.info("BMC version %s", bmc_version)
            return bmc_version.group()
        else:
            log.info("BMC version not found")
            return "Not found"


    def create_partition(self,drive_name,new,enter_number,enter_size):
        """
        this method is used to creating the partition on drive
        :return:
        """
        create = exec_cmd(f"echo -e '{new}\np\n{enter_number}\n\n{enter_size}\nw\n' | fdisk {drive_name}")
        log.info("Partition created successfully!")
        return create


    def delete_partition(self,drive_name,delete):
        """
        this method is used to delete the partition
        :return:
        """
        remove = exec_cmd(f"echo -e '{delete}\nw\n'| fdisk {drive_name}")
        log.info("Partition deleted Successfully!")
        return remove


    def check_fio_pac(self):
        """
        this method is used to check the fio package is installed or not
        :return:
        """
        fio_pac = exec_cmd("fio -v")
        fio_package = re.search(f".+", fio_pac)
        if fio_package:
            return fio_package.group()
        else:
            fio_inst = exec_cmd("apt install fio")
            return "Installed" if fio_inst else "Failed to install"


obj1 = Mainlub()
"""
# This values can be used for partition creation
drive_name = input("Enter full_drive_name:")
new = input("Enter new n:")
enter_number = input("Enter partition_number 1-4:")
enter_size = input("Enter partition size Ex=+10G:")
print(obj1.create_partition(drive_name,new,enter_number,enter_size))

delete = input("Enter delete d:")
print(obj1.delete_partition(drive_name,delete))
"""

# print(obj1.get_server_uptime())
# print(obj1.get_server_drives())
# # print(obj1.get_fw_version())
# print(obj1.check_os_version())
# print(obj1.check_bmc_version())
# print(obj1.raid_controller())
# print(obj1.check_bios())
# print(obj1.check_fio_pac())



"""

# This content is used to find the firmware version of components and current date and time to write a file in windows
data = obj1.get_server_drives()
output_file = "fwversion_currentdateandtime.bin"
for i in range(len(data)):
    out1 = "/dev/"+data[i]
    out = obj1.get_fw_version(out1)
    fw_version = out
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, "a") as output:
        output.write("Firmware Version of ")
        output.write(out1+" : " + fw_version + "\n")
        output.write("Current date and time: ")
        output.write(current_date + "\n")
        log.info(f"Firmware version and date/time saved to {output_file}.")


out2 = obj1.raid_controller()
with open(output_file, "a") as file1:
    file1.write("Raid Controller Information: ")
    file1.write(out2)

new = obj1.check_os_version()
with open(output_file, "a") as file2:
    file2.write("OS info: ")
    file2.write(new+"\n")


out3 = obj1.check_bios()
with open(output_file, "a") as file3:
    file3.write(out3 + "\n")


out4 = obj1.check_bmc_version()
with open(output_file, "a") as file4:
    file4.write("BMC Information: ")
    file4.write(out4 + "\n")

"""
# raid_name = input("Enter raid name: ")
# raid_level = input("Enter raid level: ")
# raid_devices = input("Enter no of raid devices: ")
# raid_drivers = input("Enter raid drivers: ")
# print(obj1.create_raid(raid_name, raid_level, raid_devices, raid_drivers))
# print(obj1.delete_raid(raid_name))
