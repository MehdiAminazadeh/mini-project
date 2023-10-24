from mini_projects import B
class C(B):
    def __init__(self, device_name , credibility:bool= True,event_id: int = None):
        super().__init__(event_id)
        self.device = device_name
        if credibility:
            self.components = {"I/O":True, "BUS":True}
        else:
            # manual
            self.check_crediblity(1)

def main():
    while True:
        try:
            device_name, credit, event_id = str(input('DEVICE, CREDIT, EVENT_ID: ').split())
            
        except ValueError:
            print('Error while entering!')
        
        else:
            C(device_name, credit, event_id)


# ----------------------- Correct the partially initialized module 'mini-projects'-------------------------------