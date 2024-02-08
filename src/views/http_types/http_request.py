'''
    module docstring
'''
from typing import Dict


class HttpRequest:
    '''
        class docstring
    '''
    def __init__(
            self, 
            header: Dict = None, 
            body: Dict = None, 
            query_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params