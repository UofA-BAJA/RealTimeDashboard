import os
import json

class MetaApplication:

    def __init__(self) -> None:
        
        self.repo_dir = self.__get_repo_directory()

        self.src_directory = os.path.join(self.repo_dir, "src")

        self.app_configuration_json = self.__create_json_obj("app")

    
    def __get_repo_directory(self):
        curdir = os.path.abspath(os.curdir)

        index = curdir.find("RealTimeDashboard")

        return curdir[:index + len(curdir)]
    
    def __create_json_obj(self, json_filename):

        data = None
       
        json_file = json_filename + ".json"
        json_path = os.path.join(self.repo_dir, ".config", json_file)

        with open(json_path, "r") as read_file:
            data = json.load(read_file)

        return data
