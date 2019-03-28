"""Create a topic and a direct message."""
from . import topic_to_message_handler
from .. import pub
from ..address import Address
from ..constants import MessageFlagType
from ..topics import (ASSIGN_TO_ALL_LINK_GROUP, ASSIGN_TO_COMPANION_GROUP,
                      BRIGHTEN_ONE_STEP, 
                      DELETE_FROM_ALL_LINK_GROUP, DEVICE_TEXT_STRING_REQUEST,
                      DIM_ONE_STEP, DOOR_MOVE_CLOSE_DOOR, DOOR_MOVE_LOWER_DOOR,
                      DOOR_MOVE_OPEN_DOOR, DOOR_MOVE_RAISE_DOOR,
                      DOOR_MOVE_SINGLE_DOOR_CLOSE, DOOR_MOVE_SINGLE_DOOR_OPEN,
                      DOOR_MOVE_STOP_DOOR, DOOR_STATUS_REPORT_CLOSE_DOOR,
                      DOOR_STATUS_REPORT_LOWER_DOOR,
                      DOOR_STATUS_REPORT_OPEN_DOOR,
                      DOOR_STATUS_REPORT_RAISE_DOOR,
                      DOOR_STATUS_REPORT_SINGLE_DOOR_CLOSE,
                      DOOR_STATUS_REPORT_SINGLE_DOOR_OPEN,
                      DOOR_STATUS_REPORT_STOP_DOOR, ENTER_LINKING_MODE,
                      ENTER_UNLINKING_MODE, EXTENDED_GET_SET,
                      EXTENDED_READ_WRITE_ALDB, EXTENDED_TRIGGER_ALL_LINK,
                      FX_USERNAME, GET_INSTEON_ENGINE_VERSION,
                      GET_OPERATING_FLAGS,
                      ID_REQUEST, INSTANT_CHANGE, IO_ALARM_DATA_REQUEST,
                      IO_ALARM_DATA_RESPONSE, IO_GET_SENSOR_ALARM_DELTA,
                      IO_GET_SENSOR_VALUE, IO_MODULE_DIAGNOSTICS_OFF,
                      IO_MODULE_DIAGNOSTICS_ON,
                      IO_MODULE_DISABLE_STATUS_CHANGE_MESSAGE,
                      IO_MODULE_ENABLE_STATUS_CHANGE_MESSAGE,
                      IO_MODULE_LOAD_EEPROM_FROM_RAM,
                      IO_MODULE_LOAD_INITIALIZATION_VALUES,
                      IO_MODULE_LOAD_RAM_FROM_EEPROM,
                      IO_MODULE_READ_ANALOG_ALWAYS, IO_MODULE_READ_ANALOG_ONCE,
                      IO_MODULE_SENSOR_OFF, IO_MODULE_SENSOR_ON,
                      IO_MODULE_STATUS_REQUEST, IO_OUTPUT_OFF, IO_OUTPUT_ON,
                      IO_READ_CONFIGURATION_PORT, IO_READ_INPUT_PORT,
                      IO_SET_SENSOR_1_NOMINAL_VALUE,
                      IO_SET_SENSOR_NOMINAL_VALUE, IO_WRITE_CONFIGURATION_PORT,
                      IO_WRITE_OUTPUT_PORT, 
                      OFF, OFF_AT_RAMP_RATE, OFF_FAST,
                      ON, ON_AT_RAMP_RATE, ON_FAST, PEEK_ONE_BYTE,
                      PEEK_ONE_BYTE_INTERNAL, PING, POKE_ONE_BYTE,
                      POKE_ONE_BYTE_INTERNAL, POOL_DEVICE_OFF, POOL_DEVICE_ON,
                      POOL_GET_AMBIENT_TEMPERATURE, POOL_GET_PH,
                      POOL_GET_POOL_MODE, POOL_GET_WATER_TEMPERATURE,
                      POOL_LOAD_EEPROM_FROM_RAM,
                      POOL_LOAD_INITIALIZATION_VALUES,
                      POOL_SET_DEVICE_HYSTERESIS, POOL_SET_DEVICE_TEMPERATURE,
                      POOL_TEMPERATURE_DOWN, POOL_TEMPERATURE_UP,
                      PRODUCT_DATA_REQUEST,
                      SET_ADDRESS_MSB, SET_ALL_LINK,
                      SET_ALL_LINK_COMMAND_ALIAS, SET_DEVICE_TEXT_STRING,
                      SET_OPERATING_FLAGS,
                      SET_SPRINKLER_PROGRAM, SET_STATUS,
                      SPRINKLER_BROADCAST_OFF, SPRINKLER_BROADCAST_ON,
                      SPRINKLER_DIAGNOSTICS_OFF, SPRINKLER_DIAGNOSTICS_ON,
                      SPRINKLER_DISABLE_PUMP_ON_V8,
                      SPRINKLER_ENABLE_PUMP_ON_V8,
                      SPRINKLER_GET_PROGRAM_REQUEST,
                      SPRINKLER_GET_PROGRAM_RESPONSE,
                      SPRINKLER_GET_VALVE_STATUS,
                      SPRINKLER_INHIBIT_COMMAND_ACCEPTANCE,
                      SPRINKLER_LOAD_EEPROM_FROM_RAM,
                      SPRINKLER_LOAD_INITIALIZATION_VALUES,
                      SPRINKLER_LOAD_RAM_FROM_EEPROM, SPRINKLER_PROGRAM_OFF,
                      SPRINKLER_PROGRAM_ON,
                      SPRINKLER_RESUME_COMMAND_ACCEPTANCE,
                      SPRINKLER_SENSOR_OFF, SPRINKLER_SENSOR_ON,
                      SPRINKLER_SKIP_BACK, SPRINKLER_SKIP_FORWARD,
                      SPRINKLER_VALVE_OFF, SPRINKLER_VALVE_ON,
                      STATUS_REQUEST,
                      STATUS_REQUEST_ALTERNATE_1, STATUS_REQUEST_ALTERNATE_2,
                      STATUS_REQUEST_ALTERNATE_3,
                      THERMOSTAT_DISABLE_STATUS_CHANGE_MESSAGE,
                      THERMOSTAT_ENABLE_STATUS_CHANGE_MESSAGE,
                      THERMOSTAT_GET_AMBIENT_TEMPERATURE,
                      THERMOSTAT_GET_EQUIPMENT_STATE,
                      THERMOSTAT_GET_FAN_ON_SPEED, THERMOSTAT_GET_MODE,
                      THERMOSTAT_GET_TEMPERATURE_UNITS,
                      THERMOSTAT_GET_ZONE_INFORMATION,
                      THERMOSTAT_LOAD_EEPROM_FROM_RAM,
                      THERMOSTAT_LOAD_INITIALIZATION_VALUES,
                      THERMOSTAT_OFF_ALL, THERMOSTAT_OFF_FAN,
                      THERMOSTAT_ON_AUTO, THERMOSTAT_ON_COOL,
                      THERMOSTAT_ON_FAN, THERMOSTAT_ON_HEAT,
                      THERMOSTAT_PROGRAM_AUTO, THERMOSTAT_PROGRAM_COOL,
                      THERMOSTAT_PROGRAM_HEAT, THERMOSTAT_SET_CELSIUS,
                      THERMOSTAT_SET_COOL_SETPOINT,
                      THERMOSTAT_SET_EQUIPMENT_STATE,
                      THERMOSTAT_SET_FAHRENHEIT,
                      THERMOSTAT_SET_FAN_ON_SPEED_HIGH,
                      THERMOSTAT_SET_FAN_ON_SPEED_LOW,
                      THERMOSTAT_SET_FAN_ON_SPEED_MEDIUM,
                      THERMOSTAT_SET_HEAT_SETPOINT,
                      THERMOSTAT_SET_ZONE_COOL_SETPOINT,
                      THERMOSTAT_SET_ZONE_HEAT_SETPOINT,
                      THERMOSTAT_TEMPERATURE_DOWN, THERMOSTAT_TEMPERATURE_UP,
                      THERMOSTAT_ZONE_TEMPERATURE_DOWN,
                      THERMOSTAT_ZONE_TEMPERATURE_UP, WINDOW_COVERING_CLOSE,
                      WINDOW_COVERING_OPEN, WINDOW_COVERING_POSITION,
                      WINDOW_COVERING_PROGRAM, WINDOW_COVERING_STOP)
from .commands import commands
from .messages.message_flags import create as create_flags
from .messages.outbound import send_extended, send_standard
from .messages.user_data import UserData


# The following messages are all send_standard or send_extended messages
# The topis is based on the cmd1, cmd2 and extended message flags values

def _create_direct_message(topic, address, cmd2=None, user_data=None):
    cmd1, cmd2_std, extended = commands.get_cmd1_cmd2(topic)
    extended = True if user_data else extended
    cmd2 = cmd2_std if cmd2_std is not None else cmd2
    flags = create_flags(MessageFlagType.DIRECT, extended)
    if extended:
        user_data.set_checksum(cmd1, cmd2)
        msg = send_extended(address=address, cmd1=cmd1, cmd2=cmd2, flags=flags,
                            user_data=user_data)
    else:
        msg = send_standard(address=address, cmd1=cmd1, cmd2=cmd2, flags=flags)
    pub.sendMessage('send_message', msg=msg)


@topic_to_message_handler(topic=ASSIGN_TO_ALL_LINK_GROUP)
def assign_to_all_link_group(address: Address, group: int, topic=pub.AUTO_TOPIC):
    """Create a ASSIGN_TO_ALL_LINK_GROUP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=group)


@topic_to_message_handler(topic=DELETE_FROM_ALL_LINK_GROUP)
def delete_from_all_link_group(address: Address, group: int, topic=pub.AUTO_TOPIC):
    """Create a DELETE_FROM_ALL_LINK_GROUP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=group)


@topic_to_message_handler(topic=PRODUCT_DATA_REQUEST)
def product_data_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a PRODUCT_DATA_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=FX_USERNAME)
def fx_username(address: Address, topic=pub.AUTO_TOPIC):
    """Create a FX_USERNAME command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DEVICE_TEXT_STRING_REQUEST)
def device_text_string_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DEVICE_TEXT_STRING_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SET_DEVICE_TEXT_STRING)
def set_device_text_string(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a SET_DEVICE_TEXT_STRING command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=SET_ALL_LINK_COMMAND_ALIAS)
def set_all_link_command_alias(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a SET_ALL_LINK_COMMAND_ALIAS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=SET_ALL_LINK)
def set_all_link(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a SET_ALL_LINK command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=ENTER_LINKING_MODE)
def enter_linking_mode(address: Address, group: int, topic=pub.AUTO_TOPIC):
    """Create a ENTER_LINKING_MODE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=group)


@topic_to_message_handler(topic=ENTER_UNLINKING_MODE)
def enter_unlinking_mode(address: Address, group: int, topic=pub.AUTO_TOPIC):
    """Create a ENTER_UNLINKING_MODE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=group)


@topic_to_message_handler(topic=GET_INSTEON_ENGINE_VERSION)
def get_insteon_engine_version(address: Address, topic=pub.AUTO_TOPIC):
    """Create a GET_INSTEON_ENGINE_VERSION command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=PING)
def ping(address: Address, topic=pub.AUTO_TOPIC):
    """Create a PING command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=ID_REQUEST)
def id_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a ID_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=ON)
def on(address: Address, on_level: int, topic=pub.AUTO_TOPIC):
    """Create a ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=on_level)


@topic_to_message_handler(topic=ON_FAST)
def on_fast(address: Address, on_level: int, topic=pub.AUTO_TOPIC):
    """Create a ON_FAST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=on_level)


@topic_to_message_handler(topic=OFF)
def off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=OFF_FAST)
def off_fast(address: Address, topic=pub.AUTO_TOPIC):
    """Create a OFF_FAST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=BRIGHTEN_ONE_STEP)
def brighten_one_step(address: Address, topic=pub.AUTO_TOPIC):
    """Create a BRIGHTEN_ONE_STEP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DIM_ONE_STEP)
def dim_one_step(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DIM_ONE_STEP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=STATUS_REQUEST)
def status_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a STATUS_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=STATUS_REQUEST_ALTERNATE_1)
def status_request_alternate_1(address: Address, topic=pub.AUTO_TOPIC):
    """Create a STATUS_REQUEST_ALTERNATE_1 command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=STATUS_REQUEST_ALTERNATE_2)
def status_request_alternate_2(address: Address, topic=pub.AUTO_TOPIC):
    """Create a STATUS_REQUEST_ALTERNATE_2 command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=STATUS_REQUEST_ALTERNATE_3)
def status_request_alternate_3(address: Address, topic=pub.AUTO_TOPIC):
    """Create a STATUS_REQUEST_ALTERNATE_3 command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=GET_OPERATING_FLAGS)
def get_operating_flags(address: Address, flags_requested: int, topic=pub.AUTO_TOPIC):
    """Create a GET_OPERATING_FLAGS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=flags_requested)


@topic_to_message_handler(topic=SET_OPERATING_FLAGS)
def set_operating_flags(address: Address, flags_to_alter: int, topic=pub.AUTO_TOPIC):
    """Create a SET_OPERATING_FLAGS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=flags_to_alter)


@topic_to_message_handler(topic=INSTANT_CHANGE)
def instant_change(address: Address, on_level: int, topic=pub.AUTO_TOPIC):
    """Create a INSTANT_CHANGE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=on_level)


@topic_to_message_handler(topic=SET_STATUS)
def set_status(address: Address, on_level: int, topic=pub.AUTO_TOPIC):
    """Create a SET_STATUS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=on_level)


@topic_to_message_handler(topic=SET_ADDRESS_MSB)
def set_address_msb(address: Address, high_byte: int, topic=pub.AUTO_TOPIC):
    """Create a SET_ADDRESS_MSB command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=high_byte)


@topic_to_message_handler(topic=POKE_ONE_BYTE)
def poke_one_byte(address: Address, byte_to_write: int, topic=pub.AUTO_TOPIC):
    """Create a POKE_ONE_BYTE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=byte_to_write)


@topic_to_message_handler(topic=PEEK_ONE_BYTE)
def peek_one_byte(address: Address, lsb: int, topic=pub.AUTO_TOPIC):
    """Create a PEEK_ONE_BYTE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=lsb)


@topic_to_message_handler(topic=PEEK_ONE_BYTE_INTERNAL)
def peek_one_byte_internal(address: Address, lsb: int, topic=pub.AUTO_TOPIC):
    """Create a PEEK_ONE_BYTE_INTERNAL command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=lsb)


@topic_to_message_handler(topic=POKE_ONE_BYTE_INTERNAL)
def poke_one_byte_internal(address: Address, byte_to_write: int, topic=pub.AUTO_TOPIC):
    """Create a POKE_ONE_BYTE_INTERNAL command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=byte_to_write)


@topic_to_message_handler(topic=ON_AT_RAMP_RATE)
def on_at_ramp_rate(address: Address, on_level: int, ramp_rate: int, topic=pub.AUTO_TOPIC):
    """Create a ON_AT_RAMP_RATE command."""
    topic = topic.name.split('.')[1]
    on_level = on_level & 0x0f << 4
    ramp_rate = int(ramp_rate / 2 + 1)
    on_level_and_ramp_rate = on_level + ramp_rate
    _create_direct_message(topic=topic, address=address, cmd2=on_level_and_ramp_rate)


@topic_to_message_handler(topic=EXTENDED_GET_SET)
def extended_get_set(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a EXTENDED_GET_SET command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=OFF_AT_RAMP_RATE)
def off_at_ramp_rate(address: Address, ramp_rate: int, topic=pub.AUTO_TOPIC):
    """Create a OFF_AT_RAMP_RATE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=ramp_rate)


@topic_to_message_handler(topic=EXTENDED_READ_WRITE_ALDB)
def extended_read_write_aldb(address: Address, action: int, mem_addr: int, num_recs: int,
                             topic=pub.AUTO_TOPIC):
    """Create a EXTENDED_READ_WRITE_ALDB command."""
    topic = topic.name.split('.')[1]
    num_recs = 0 if mem_addr == 0x0000 else 1
    mem_hi = mem_addr >> 8
    mem_lo = mem_addr & 0xff
    user_data = UserData({'d2': action, 'd3': mem_hi, 'd4': mem_lo, 'd5': num_recs})
    _create_direct_message(topic=topic, address=address, user_data=user_data)


@topic_to_message_handler(topic=EXTENDED_TRIGGER_ALL_LINK)
def extended_trigger_all_link(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a EXTENDED_TRIGGER_ALL_LINK command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=SET_SPRINKLER_PROGRAM)
def set_sprinkler_program(address: Address, program: int, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a SET_SPRINKLER_PROGRAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=program, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=SPRINKLER_VALVE_ON)
def sprinkler_valve_on(address: Address, valve: int, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_VALVE_ON command.""" 
    _create_direct_message(topic=topic, address=address, cmd2=valve)


@topic_to_message_handler(topic=SPRINKLER_GET_PROGRAM_RESPONSE)
def sprinkler_get_program_response(address: Address, program: int,
                                   OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_GET_PROGRAM_RESPONSE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=program, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=SPRINKLER_VALVE_OFF)
def sprinkler_valve_off(address: Address, valve: int, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_VALVE_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=valve)


@topic_to_message_handler(topic=SPRINKLER_PROGRAM_ON)
def sprinkler_program_on(address: Address, program: int, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_PROGRAM_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=program)


@topic_to_message_handler(topic=SPRINKLER_PROGRAM_OFF)
def sprinkler_program_off(address: Address, program: int, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_PROGRAM_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=program)


@topic_to_message_handler(topic=SPRINKLER_LOAD_INITIALIZATION_VALUES)
def sprinkler_load_initialization_values(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_LOAD_INITIALIZATION_VALUES command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_LOAD_EEPROM_FROM_RAM)
def sprinkler_load_eeprom_from_ram(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_LOAD_EEPROM_FROM_RAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_GET_VALVE_STATUS)
def sprinkler_get_valve_status(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_GET_VALVE_STATUS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_INHIBIT_COMMAND_ACCEPTANCE)
def sprinkler_inhibit_command_acceptance(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_INHIBIT_COMMAND_ACCEPTANCE command."""
    topic = topic.name.split('.')[1]
    user_data=UserData({'d1': 0x03})
    _create_direct_message(topic=topic, address=address, cmd2=0x44, user_data=user_data)


@topic_to_message_handler(topic=SPRINKLER_RESUME_COMMAND_ACCEPTANCE)
def sprinkler_resume_command_acceptance(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_RESUME_COMMAND_ACCEPTANCE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_SKIP_FORWARD)
def sprinkler_skip_forward(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_SKIP_FORWARD command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_SKIP_BACK)
def sprinkler_skip_back(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_SKIP_BACK command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_ENABLE_PUMP_ON_V8)
def sprinkler_enable_pump_on_v8(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_ENABLE_PUMP_ON_V8 command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_DISABLE_PUMP_ON_V8)
def sprinkler_disable_pump_on_v8(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_DISABLE_PUMP_ON_V8 command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_BROADCAST_ON)
def sprinkler_broadcast_on(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_BROADCAST_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_BROADCAST_OFF)
def sprinkler_broadcast_off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_BROADCAST_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_LOAD_RAM_FROM_EEPROM)
def sprinkler_load_ram_from_eeprom(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_LOAD_RAM_FROM_EEPROM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_SENSOR_ON)
def sprinkler_sensor_on(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_SENSOR_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_SENSOR_OFF)
def sprinkler_sensor_off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_SENSOR_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_DIAGNOSTICS_ON)
def sprinkler_diagnostics_on(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_DIAGNOSTICS_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_DIAGNOSTICS_OFF)
def sprinkler_diagnostics_off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_DIAGNOSTICS_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=SPRINKLER_GET_PROGRAM_REQUEST)
def sprinkler_get_program_request(address: Address, program: int, topic=pub.AUTO_TOPIC):
    """Create a SPRINKLER_GET_PROGRAM_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=program)


@topic_to_message_handler(topic=IO_OUTPUT_ON)
def io_output_on(address: Address, output_num: int, topic=pub.AUTO_TOPIC):
    """Create a IO_OUTPUT_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=output_num)


@topic_to_message_handler(topic=IO_OUTPUT_OFF)
def io_output_off(address: Address, output_num: int, topic=pub.AUTO_TOPIC):
    """Create a IO_OUTPUT_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=output_num)


@topic_to_message_handler(topic=IO_ALARM_DATA_REQUEST)
def io_alarm_data_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_ALARM_DATA_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)

@topic_to_message_handler(topic=IO_WRITE_OUTPUT_PORT)
def io_write_output_port(address: Address, value: int, topic=pub.AUTO_TOPIC):
    """Create a IO_WRITE_OUTPUT_PORT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_READ_INPUT_PORT)
def io_read_input_port(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_READ_INPUT_PORT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_GET_SENSOR_VALUE)
def io_get_sensor_value(address: Address, sensor: int, topic=pub.AUTO_TOPIC):
    """Create a IO_GET_SENSOR_VALUE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=sensor)


@topic_to_message_handler(topic=IO_SET_SENSOR_1_NOMINAL_VALUE)
def io_set_sensor_1_nominal_value(address: Address, value: int, topic=pub.AUTO_TOPIC):
    """Create a IO_SET_SENSOR_1_NOMINAL_VALUE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=value)


@topic_to_message_handler(topic=IO_SET_SENSOR_NOMINAL_VALUE)
def io_set_sensor_nominal_value(address: Address, value: int,
                                OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a IO_SET_SENSOR_NOMINAL_VALUE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=value, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=IO_GET_SENSOR_ALARM_DELTA)
def io_get_sensor_alarm_delta(address: Address, sensor: int, delta: int,
                              direction: int, topic=pub.AUTO_TOPIC):
    """Create a IO_GET_SENSOR_ALARM_DELTA command."""
    topic = topic.name.split('.')[1]
    sensor = sensor & 0x0f
    delta = delta & 0x07 << 4
    direction = 8 if bool(direction) else 0
    cmd2 = (sensor + delta + direction)
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=IO_ALARM_DATA_RESPONSE)
def io_alarm_data_response(address: Address, OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a IO_ALARM_DATA_RESPONSE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=IO_WRITE_CONFIGURATION_PORT)
def io_write_configuration_port(address: Address, bits_0_1: bool,
                                bit_2: bool, bit_3: bool, bit_4: bool,
                                bit_5: bool, bit_6: bool, bit_7: bool
                                , topic=pub.AUTO_TOPIC):
    """Create a IO_WRITE_CONFIGURATION_PORT command."""
    topic = topic.name.split('.')[1]
    cmd2 = (bit_7 << 7 + bit_6 << 6 + bit_5 << 5 + bit_4 << 4 + bit_3 << 3 +
            bit_2 << 2 + bits_0_1 << 0)
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=IO_READ_CONFIGURATION_PORT)
def io_read_configuration_port(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_READ_CONFIGURATION_PORT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_LOAD_INITIALIZATION_VALUES)
def io_module_load_initialization_values(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_LOAD_INITIALIZATION_VALUES command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_LOAD_EEPROM_FROM_RAM)
def io_module_load_eeprom_from_ram(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_LOAD_EEPROM_FROM_RAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_STATUS_REQUEST)
def io_module_status_request(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_STATUS_REQUEST command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_READ_ANALOG_ONCE)
def io_module_read_analog_once(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_READ_ANALOG_ONCE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_READ_ANALOG_ALWAYS)
def io_module_read_analog_always(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_READ_ANALOG_ALWAYS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_ENABLE_STATUS_CHANGE_MESSAGE)
def io_module_enable_status_change_message(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_ENABLE_STATUS_CHANGE_MESSAGE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_DISABLE_STATUS_CHANGE_MESSAGE)
def io_module_disable_status_change_message(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_DISABLE_STATUS_CHANGE_MESSAGE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_LOAD_RAM_FROM_EEPROM)
def io_module_load_ram_from_eeprom(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_LOAD_RAM_FROM_EEPROM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_SENSOR_ON)
def io_module_sensor_on(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_SENSOR_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_SENSOR_OFF)
def io_module_sensor_off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_SENSOR_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_DIAGNOSTICS_ON)
def io_module_diagnostics_on(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_DIAGNOSTICS_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=IO_MODULE_DIAGNOSTICS_OFF)
def io_module_diagnostics_off(address: Address, topic=pub.AUTO_TOPIC):
    """Create a IO_MODULE_DIAGNOSTICS_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_DEVICE_ON)
def pool_device_on(address: Address, device_num: int, topic=pub.AUTO_TOPIC):
    """Create a POOL_DEVICE_ON command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=device_num)


@topic_to_message_handler(topic=POOL_SET_DEVICE_TEMPERATURE)
def pool_set_device_temperature(address: Address, device_num: int,
                                OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a POOL_SET_DEVICE_TEMPERATURE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=device_num, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=POOL_DEVICE_OFF)
def pool_device_off(address: Address, device_num: int, topic=pub.AUTO_TOPIC):
    """Create a POOL_DEVICE_OFF command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=device_num)


@topic_to_message_handler(topic=POOL_SET_DEVICE_HYSTERESIS)
def pool_set_device_hysteresis(address: Address, device_num: int,
                               OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a POOL_SET_DEVICE_HYSTERESIS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=device_num, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=POOL_TEMPERATURE_UP)
def pool_temperature_up(address: Address, degrees: int, topic=pub.AUTO_TOPIC):
    """Create a POOL_TEMPERATURE_UP command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=POOL_TEMPERATURE_DOWN)
def pool_temperature_down(address: Address, degrees: int, topic=pub.AUTO_TOPIC):
    """Create a POOL_TEMPERATURE_DOWN command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=POOL_LOAD_INITIALIZATION_VALUES)
def pool_load_initialization_values(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_LOAD_INITIALIZATION_VALUES command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_LOAD_EEPROM_FROM_RAM)
def pool_load_eeprom_from_ram(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_LOAD_EEPROM_FROM_RAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_GET_POOL_MODE)
def pool_get_pool_mode(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_GET_POOL_MODE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_GET_AMBIENT_TEMPERATURE)
def pool_get_ambient_temperature(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_GET_AMBIENT_TEMPERATURE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_GET_WATER_TEMPERATURE)
def pool_get_water_temperature(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_GET_WATER_TEMPERATURE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=POOL_GET_PH)
def pool_get_ph(address: Address, topic=pub.AUTO_TOPIC):
    """Create a POOL_GET_PH command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_RAISE_DOOR)
def door_move_raise_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_RAISE_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_LOWER_DOOR)
def door_move_lower_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_LOWER_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_OPEN_DOOR)
def door_move_open_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_OPEN_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_CLOSE_DOOR)
def door_move_close_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_CLOSE_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_STOP_DOOR)
def door_move_stop_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_STOP_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_SINGLE_DOOR_OPEN)
def door_move_single_door_open(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_SINGLE_DOOR_OPEN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_MOVE_SINGLE_DOOR_CLOSE)
def door_move_single_door_close(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_MOVE_SINGLE_DOOR_CLOSE command."""
    topic = topic.name.split('.')[1]
    user_data = UserData({'d1': 0x06})
    _create_direct_message(topic=topic, address=address, cmd2=0x58, user_data=user_data)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_RAISE_DOOR)
def door_status_report_raise_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_RAISE_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_LOWER_DOOR)
def door_status_reportlower_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_LOWER_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_OPEN_DOOR)
def door_status_report_open_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_OPEN_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_CLOSE_DOOR)
def door_status_report_close_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_CLOSE_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_STOP_DOOR)
def door_status_report_stop_door(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_STOP_DOOR command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_SINGLE_DOOR_OPEN)
def door_status_report_single_door_open(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_SINGLE_DOOR_OPEN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=DOOR_STATUS_REPORT_SINGLE_DOOR_CLOSE)
def door_status_report_single_door_close(address: Address, topic=pub.AUTO_TOPIC):
    """Create a DOOR_STATUS_REPORT_SINGLE_DOOR_CLOSE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=WINDOW_COVERING_OPEN)
def window_covering_open(address: Address, topic=pub.AUTO_TOPIC):
    """Create a WINDOW_COVERING_OPEN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=WINDOW_COVERING_CLOSE)
def window_covering_close(address: Address, topic=pub.AUTO_TOPIC):
    """Create a WINDOW_COVERING_CLOSE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=WINDOW_COVERING_STOP)
def window_covering_stop(address: Address, topic=pub.AUTO_TOPIC):
    """Create a WINDOW_COVERING_STOP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=WINDOW_COVERING_PROGRAM)
def window_covering_program(address: Address, topic=pub.AUTO_TOPIC):
    """Create a WINDOW_COVERING_PROGRAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=WINDOW_COVERING_POSITION)
def window_covering_position(address: Address, position: int, topic=pub.AUTO_TOPIC):
    """Create a WINDOW_COVERING_POSITION command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=position)


@topic_to_message_handler(topic=THERMOSTAT_TEMPERATURE_UP)
def thermostat_temperature_up(address: Address, degrees: int, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_TEMPERATURE_UP command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=THERMOSTAT_ZONE_TEMPERATURE_UP)
def thermostat_zone_temperature_up(address: Address, zone: int,
                                   OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ZONE_TEMPERATURE_UP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=zone, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=THERMOSTAT_TEMPERATURE_DOWN)
def thermostat_temperature_down(address: Address,
                                degrees: int, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_TEMPERATURE_DOWN command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=THERMOSTAT_ZONE_TEMPERATURE_DOWN)
def thermostat_zone_temperature_down(address: Address, zone: int,
                                     OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ZONE_TEMPERATURE_DOWN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=zone, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=THERMOSTAT_GET_ZONE_INFORMATION)
def thermostat_get_zone_information(address: Address, zone: int,
                                    info: int, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_ZONE_INFORMATION command.

    zone: (int) 0 to 31

    info: (int)
        0 = Temperature
        1 = Setpoint
        2 = Deadband
        3 = Humidity
    """
    topic = topic.name.split('.')[1]
    zone = zone & 0x0f
    info = info & 0x03 << 5
    cmd2 = info + zone
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=THERMOSTAT_LOAD_INITIALIZATION_VALUES)
def thermostat_load_initialization_values(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_LOAD_INITIALIZATION_VALUES command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_LOAD_EEPROM_FROM_RAM)
def thermostat_load_eeprom_from_ram(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_LOAD_EEPROM_FROM_RAM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_GET_MODE)
def thermostat_get_mode(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_MODE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_GET_AMBIENT_TEMPERATURE)
def thermostat_get_ambient_temperature(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_AMBIENT_TEMPERATURE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_ON_HEAT)
def thermostat_on_heat(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ON_HEAT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_ON_COOL)
def thermostat_on_cool(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ON_COOL command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_ON_AUTO)
def thermostat_on_auto(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ON_AUTO command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_ON_FAN)
def thermostat_on_fan(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ON_FAN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_OFF_FAN)
def thermostat_off_fan(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_OFF_FAN command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_OFF_ALL)
def thermostat_off_all(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_OFF_ALL command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_PROGRAM_HEAT)
def thermostat_program_heat(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_PROGRAM_HEAT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_PROGRAM_COOL)
def thermostat_program_cool(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_PROGRAM_COOL command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_PROGRAM_AUTO)
def thermostat_program_auto(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_PROGRAM_AUTO command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_GET_EQUIPMENT_STATE)
def thermostat_get_equipment_state(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_EQUIPMENT_STATE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_EQUIPMENT_STATE)
def thermostat_set_equipment_state(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_EQUIPMENT_STATE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_GET_TEMPERATURE_UNITS)
def thermostat_get_temperature_units(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_TEMPERATURE_UNITS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_FAHRENHEIT)
def thermostat_set_fahrenheit(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_FAHRENHEIT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_CELSIUS)
def thermostat_set_celsius(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_CELSIUS command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_GET_FAN_ON_SPEED)
def thermostat_get_fan_on_speed(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_GET_FAN_ON_SPEED command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_FAN_ON_SPEED_LOW)
def thermostat_set_fan_on_speed_low(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_FAN_ON_SPEED_LOW command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_FAN_ON_SPEED_MEDIUM)
def thermostat_set_fan_on_speed_medium(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_FAN_ON_SPEED_MEDIUM command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_FAN_ON_SPEED_HIGH)
def thermostat_set_fan_on_speed_high(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_FAN_ON_SPEED_HIGH command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_ENABLE_STATUS_CHANGE_MESSAGE)
def thermostat_enable_status_change_message(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_ENABLE_STATUS_CHANGE_MESSAGE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_DISABLE_STATUS_CHANGE_MESSAGE)
def thermostat_disable_status_change_message(address: Address, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_DISABLE_STATUS_CHANGE_MESSAGE command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)


@topic_to_message_handler(topic=THERMOSTAT_SET_COOL_SETPOINT)
def thermostat_set_cool_setpoint(address: Address, degrees: int, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_COOL_SETPOINT command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=THERMOSTAT_SET_ZONE_COOL_SETPOINT)
def thermostat_set_zone_cool_setpoint(address: Address, zone: int,
                                      OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_ZONE_COOL_SETPOINT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=zone, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=THERMOSTAT_SET_HEAT_SETPOINT)
def thermostat_set_heat_setpoint(address: Address,
                                 degrees: int, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_HEAT_SETPOINT command."""
    topic = topic.name.split('.')[1]
    cmd2 = degrees * 2
    _create_direct_message(topic=topic, address=address, cmd2=cmd2)


@topic_to_message_handler(topic=THERMOSTAT_SET_ZONE_HEAT_SETPOINT)
def thermostat_set_zone_heat_setpoint(address: Address, zone: int,
                                      OTHER_EXT_DATA, topic=pub.AUTO_TOPIC):
    """Create a THERMOSTAT_SET_ZONE_HEAT_SETPOINT command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address, cmd2=zone, user_data=OTHER_EXT_DATA)


@topic_to_message_handler(topic=ASSIGN_TO_COMPANION_GROUP)
def assign_to_companion_group(address: Address, topic=pub.AUTO_TOPIC):
    """Create a ASSIGN_TO_COMPANION_GROUP command."""
    topic = topic.name.split('.')[1]
    _create_direct_message(topic=topic, address=address)