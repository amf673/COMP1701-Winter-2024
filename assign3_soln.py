# Assignment3.py
# 
# COMP 1701 
# 
# A. Fedoruk
# 

SAFE_CUTOFF     = 0
MONITOR_CUTOFF  = 20
PREPARE_CUTOFF  = 70
EVACUATE_CUTOFF = 90

SAFE_MESSAGE     = 'Emissions levels are safe'
MONITOR_MESSAGE  = 'Keep monitoring situation'
PREPARE_MESSAGE  = 'Warning, prepare for action'
EVACUATE_MESSAGE = 'Evacuate Production Enclosure'
FLEE_MESSAGE     = 'Evacuate Facility'

def get_message_for_gases(co_enabled: bool, ch4_enabled: bool) -> str:
    """
    Returns the MESSAGE defined by the gas_detector.
    Arguments:
    co_enabled -- Boolean. True if co_detector is enabled.
    ch4_enabled -- Boolean. True if ch4_detector is enabled.
    returns name as a string. Example: "CO is being released"
    """
    
    if co_enabled and ch4_enabled:
        reply = 'CO and CH4 are being released'
    elif co_enabled and not(ch4_enabled):
        reply = 'CO is being released'
    elif not(co_enabled) and ch4_enabled:
        reply = 'CH4 is being released'
    elif not(co_enabled) and not(ch4_enabled):
        reply = 'No gases are being released'
    else:
        reply = None

    return reply
   

def get_volume_desc(gauge_value: int) -> str:
    """
    Returns the MESSAGE description defined by the volume-gauge value.
    Arguments:
    gaguge_value -- integer gauge value. Assumed to be between 0 and 100 (inclusive).
    returns the ACTION description. Example: "Keep monitoring situation"
    """

    if gauge_value <= SAFE_CUTOFF:
        reply = SAFE_MESSAGE
    elif gauge_value <= MONITOR_CUTOFF:
        reply = MONITOR_MESSAGE
    elif gauge_value <= PREPARE_CUTOFF:
        reply = PREPARE_MESSAGE
    elif gauge_value <= EVACUATE_CUTOFF:
        reply = EVACUATE_MESSAGE
    else:
        reply = FLEE_MESSAGE
        
    return reply


def get_detector_value(detector_name: str) -> bool:
    """
    Generates input request for either the co_detector or the ch4_detector, then returns either True or False

    Arguments:
    detector_name-- a string, either 'CO' or ' CH4'.
    returns True or False, if the detector associated to the name passed as argument is ON; otherwise it
    returns False
    """
   
    response =  input(f'Is {detector_name}-detector enabled? (y/n): ').lower()

    return response == "y"
 

def main() -> None:
    
    co_detector = get_detector_value('CO')
    ch4_detector = get_detector_value('CH4')

    if not co_detector and not ch4_detector:                             
        gauge_value = 0
    else:
        gauge_value = int(input('What is the gauge value? (0-100): '))
    
    gases_presence = get_message_for_gases(co_detector, ch4_detector)
    volume = get_volume_desc(gauge_value)
    
    assembled_message = f"Current Status is [{gases_presence}: {volume}]"

    print(assembled_message)
    

main()
