from binascii import unhexlify
import logging
import unittest
import sys

from pyinsteon.constants import MessageId
from tests.utils import hex_to_inbound_message

_LOGGER = logging.getLogger(__name__)
_INSTEON_LOGGER = logging.getLogger('pyinsteon')


class TestUserResetDetected(unittest.TestCase):

    def setUp(self):
        self.hex = '0255'
        self.message_id = MessageId(0x55)

        self.msg, self.msg_bytes = hex_to_inbound_message(self.hex)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        _LOGGER.addHandler(stream_handler)

    def test_id(self):
        assert self.msg.message_id == self.message_id

    def test_bytes(self):
        assert bytes(self.msg) == unhexlify(self.hex)