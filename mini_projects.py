from random import randint

class A(object):
    device_counter = 0
    def __init__(self, event_id:int = None):
         self._cpu = [1, 2, 3]
         self.event_id = event_id
         if self.event_id is not None:
            self.event_id = ['Active']
            A.device_counter += 1
         
    def set_ip(self):
        if self.event_id:
            a, b = 1000, 40000000000
            self._ip = randint(a, b)
        else:
            print("No Event id given")
            return
    
    def __repr__(self) -> str:
        if self.event_id:
            print(f"The cpu is connected with ip of {self._ip} and it is {self.event_id}")
        return
    
    def __del__(self):
        pass
        
class B(A):
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
            A.__repr__(self)
            #Represent all the devices added to cpu(s) information
        
    def add_device_strictly(self, ip:int, critical:float, cpu_type: dict[int, str]):
        # set the ip of critical device
        while isinstance(critical, float):
            critical += 0.2
            if critical % 2:
                critical = int(critical)
                _ip = ip
                return _ip, critical, cpu_type
            else:
               ip = self.ip 
        else:
                
            for keys in cpu_type.keys():
                if keys not in self._cpu:
                    print('Not found in cpu types')
                else:
                    self._other_cpu = cpu_type.values()
            _critical = critical
            return ip, _critical
    
    
    def critical_devices(self):
        pass
    
       
    @critical_devices
    def add_critical(self):
        ip, critical_level, cpu_type = self.add_device_strictly(self._ip, 5.2, cpu_type={1:"Xeon"})
        return ip, critical_level, cpu_type
    
    def check_crediblity(self, name, credit):
            cpu_name = ["Xeon", "i5", "i7"]
            self._cpu = {self._cpu[index]: cpu_name[index] for index in range(len(cpu_name))}
            if name not in self._cpu:
                print('name not in category')
                return
            else:
                return self.unkown_device_handler(name)
            
if __name__ == "__main__":  
    device_A = A() 
    device_B = B(0)
   
