import os
import json

class MetaApplication:

    def __init__(self) -> None:
        
        self.repo_dir = self.__get_repo_directory()

        self.src_directory = os.path.join(self.repo_dir, "src")

        self.__create_json_obj()

    
    def __get_repo_directory(self):
        curdir = os.path.abspath(os.curdir)

        index = curdir.find("RealTimeDashboard")

        return curdir[:index + len(curdir)]
    
    def __create_json_obj(self):

        json_path = os.path.join(self.repo_dir, ".config", "sensors.json")
        #print(json_path)

        with open(json_path, "r") as read_file:
            self.sensor_configuration_json = json.load(read_file)


    


        
m = MetaApplication()

print(m.src_directory)

