import math

# Library for change volume pc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

def calculate_distance_between_points(point1, point2):
    """Calculate the Euclidean distance between two landmarks."""
    
    return math.sqrt((point2.x - point1.x) ** 2 + 
                     (point2.y - point1.y) ** 2 + 
                     (point2.z - point1.z) ** 2)
    

def set_system_volume(volume_level):
    """
    Set the system-wide volume to the specified level.
    :param volume_level: The volume level to set (between 0.0 and 1.0)
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Set the volume to the desired level
    volume.SetMasterVolumeLevelScalar(volume_level, None)
    print(f"Volume set to {volume_level * 100}%")


def get_system_volume():
    """
    Get the current system-wide volume.
    :return: The current volume level (between 0.0 and 1.0)
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()
    print(f"Current volume: {current_volume * 100}%")
    return current_volume