import warnings

from lib.baseaction import BaseAction
from lib.phpipam.controllers import VlansApi


class ListVlans(BaseAction):
    """ Stackstorm Python Runner """
    def run(self):
        """ Stackstorm Run Method  """
        warnings.filterwarnings('ignore')

        self.ipam.login(auth=(self.api_username, self.api_password))

        vlans_api = VlansApi(phpipam=self.ipam)

        vlanlist = vlans_api.list_vlans()

        self.ipam.logout()

        return vlanlist
