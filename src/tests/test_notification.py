#  Copyright (c) 2021 Roger Muñoz
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License, or (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
""" TeSLA CE Keystroke test notifiction module """
import pytest


def test_notification_not_implemented(tks_provider):
    '''
    Test notification not implemented
    :param tks_provider:
    :return:
    '''
    try:
        tks_provider.on_notification('key', {})
        pytest.fail("Notification is not used by TKS, should raise an exception")
    except NotImplementedError:
        # Is the expected behaviour
        pass
