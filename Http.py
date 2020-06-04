#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午11:05            
#                                           
import requests


class Http:

    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code == 200:
            if return_json:
                return res.json()
            return res.text

        if return_json:
            return {}
        return ''
