
def calculate_time_difference(device, frame):
    device.attributes.time_difference = device.attributes.calc_time_difference(frame)

def calculate_num_of_deauth_frames(device, frame):
    device.attributes.num_of_deauth_frames = device.attributes.calc_num_of_deauth_frames(frame)

def calculate_num_of_frame_exchange(device, frame):
    device.attributes.num_of_frame_exchange = device.attributes.calc_num_of_frame_exchange(frame)

def calculate_num_of_auth_frames(device, frame):
    device.attributes.num_of_auth_frames = device.attributes.calc_num_of_auth_frames(frame)

def calculate_num_of_tcp_frames(device, frame):
    device.attributes.num_of_tcp_frames = None  # Your calculation logic here

def calculate_num_of_association_frames(device, frame):
    device.attributes.num_of_association_frames = None  # Your calculation logic here

def calculate_num_of_udp_frames(device, frame):
    device.attributes.num_of_udp_frames = None  # Your calculation logic here

# List of functions to call for each attribute calculation
attribute_functions = [
    calculate_time_difference,
    calculate_num_of_deauth_frames,
    calculate_num_of_frame_exchange,
    calculate_num_of_auth_frames,
    calculate_num_of_tcp_frames,
    calculate_num_of_association_frames,
    calculate_num_of_udp_frames
]

