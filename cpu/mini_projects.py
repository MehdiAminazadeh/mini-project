# import other libraries as needed 

from random import randint
import psutil
import platform
import os


class Device(object):
    # intiate the primitave vars 
    device_counter = 0
    def __init__(self, event_id: int = None, termin:bool=False):
         self._cpu = [1, 2, 3]
         self.event_id = event_id
         if self.event_id is not None:
            self.event_id = ['Active']
            Device.device_counter += 1
         self.termin = termin

    # set a random ip to process
    def set_ip(self):
        if self.event_id:
            a, b = 1000, 40000000000
            self._ip = randint(a, b)
        else:
            print("No Event id given")
            return

    # get info of the current cpu connected to the device
    def get_info(self):
        cpu_info = {
        'CPU Type': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical CPUs': psutil.cpu_count(logical=True),
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
    }
        return cpu_info
        
    # if terminate is called, finish the process and eliminate total number of devices 
    def terminate(self):
        from logging import info
        if self.termin == True and self.event_id is not None and Device.device_counter > 1:
            while Device.device_counter != 0:
                Device.device_counter -= 1
                self.event_id.pop()
            else:
                pass
                
            for process in psutil.process_iter(['pid', 'name']):
                process.info['name'] == "q" if self.termin else None
                process.terminate()
                print("Terminated")
                return True
            print("The key entered is wrong. Should be 'q' ")
            return False
            
        # terminate is called, store the last cpu data to the text file 
        with open("cpu_info.txt", mode='w', encoding='utf-8', newline='\r\n') as cpu_info:
            for key, val in self.get_info():
                cpu_info.write(f"{key}: {val}")
        info("Complete SAVE")   
                
    def __repr__(self) -> str:
        if self.event_id:
            print(f"The cpu is connected with ip of {self._ip} and it is {self.event_id}")
        return
    

class DeciceCheck(Device):
    def __init__(self, event_id):
        super().__init__(event_id)
        self.ip = super().set_ip() 
        
    def unkown_device_handler(self, device_name:int):
        from time import sleep
        if device_name not in self._cpu:
            print('No such device found')
            sleep(100)
            self.event_id.append('Semi-Active')
            print(f'Current state of event_id is: {self.event_id}')
        else:
            Device.__repr__(self)
            #Represent all the devices added to cpu(s) information
        

"""Logic given for further Operation!
___coding in different modules perplexes the implementation process
___GHEP Electronics --> Check  
"""
