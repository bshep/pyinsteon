"""Switched Lighting Control devices (CATEGORY 0x02)."""
from ..handlers.to_device.off import OffCommand
from ..handlers.to_device.on_level import OnLevelCommand
from ..handlers.to_device.on_fast import OnFastCommand
from ..handlers.to_device.off_fast import OffFastCommand
from .commands import OFF_COMMAND, ON_COMMAND, OFF_FAST_COMMAND, ON_FAST_COMMAND
from .on_off_controller_base import OnOffControllerBase


class OnOffResponderBase(OnOffControllerBase):
    """Switched Lighting Control device."""

    def __init__(self, address, cat, subcat, firmware=0x00,
                 description='', model='', buttons=None, state_name=None,
                 on_event_name=None, off_event_name=None,
                 on_fast_event_name=None, off_fast_event_name=None):
        """Init the OnOffResponderBase class."""
        if buttons is None:
            buttons = [1]
        super().__init__(address, cat, subcat, firmware, description, model, buttons, state_name,
                         on_event_name, off_event_name, on_fast_event_name, off_fast_event_name)

    def on(self, group: int = 0):
        """Turn on the device."""
        group = 1 if not group else group
        self._handlers[group][ON_COMMAND].send(on_level=0xff)

    async def async_on(self, group: int = 0):
        """Turn on the device."""
        group = 1 if not group else group
        return await self._handlers[group][ON_COMMAND].async_send(on_level=0xff)

    def off(self, group: int = 0):
        """Turn off the device."""
        group = 1 if not group else group
        self._handlers[group][OFF_COMMAND].send()

    async def async_off(self, group: int = 0):
        """Turn off the device."""
        group = 1 if not group else group
        return await self._handlers[group][OFF_COMMAND].async_send()

    def _register_handlers_and_managers(self):
        super()._register_handlers_and_managers()
        for group in self._buttons:
            if self._state_name is not None:
                if self._handlers.get(group) is None:
                    self._handlers[group] = {}
                self._handlers[group][ON_COMMAND] = OnLevelCommand(self._address, group)
                self._handlers[group][OFF_COMMAND] = OffCommand(self._address, group)
                self._handlers[group][ON_FAST_COMMAND] = OnFastCommand(self._address, group)
                self._handlers[group][OFF_FAST_COMMAND] = OffFastCommand(self._address, group)

    def _subscribe_to_handelers_and_managers(self):
        super()._subscribe_to_handelers_and_managers()
        for group in self._buttons:
            if self._state_name:
                self._handlers[group][ON_COMMAND].subscribe(self._states[group].set_value)
                self._handlers[group][OFF_COMMAND].subscribe(self._states[group].set_value)
                self._handlers[group][ON_FAST_COMMAND].subscribe(self._states[group].set_value)
                self._handlers[group][OFF_FAST_COMMAND].subscribe(self._states[group].set_value)


            if self._on_event_name:
                event = self._events[group][self._on_event_name]
                self._handlers[group][ON_COMMAND].subscribe(event.trigger)

            if self._off_event_name:
                event = self._events[group][self._off_event_name]
                self._handlers[group][OFF_COMMAND].subscribe(event.trigger)

            if self._on_fast_event_name:
                event = self._events[group][self._on_fast_event_name]
                self._handlers[group][ON_FAST_COMMAND].subscribe(event.trigger)

            if self._off_fast_event_name:
                event = self._events[group][self._off_fast_event_name]
                self._handlers[group][OFF_FAST_COMMAND].subscribe(event.trigger)

    def _register_default_links(self):
        pass