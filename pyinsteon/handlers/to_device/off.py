"""Manage outbound ON command to a device."""
from ...topics import OFF
from .. import direct_ack_handler
from .direct_command import DirectCommandHandlerBase


class OffCommand(DirectCommandHandlerBase):
    """Manage an outbound ON command to a device."""

    def __init__(self, address, group):
        """Init the OnLevelCommand class."""
        super().__init__(topic=OFF, address=address, group=group)

    # pylint: disable=arguments-differ
    async def async_send(self):
        """Send the OFF command async."""
        return await super().async_send(group=self._group)

    @direct_ack_handler
    def handle_direct_ack(self, cmd1, cmd2, target, user_data, hops_left):
        """Handle the OFF response direct ACK."""
        self._call_subscribers(on_level=0)
        super().handle_direct_ack(cmd1, cmd2, target, user_data, hops_left)
