import socket
import platform

print("================================")
print(" NETWORK INFORMATION ANALYZER")
print("================================")

hostname = socket.gethostname()

try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address = "Unable to detect"

print("\nDevice Information")
print("----------------------------")

print("Device Name:", hostname)
print("IP Address:", ip_address)
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Machine Type:", platform.machine())

print("\n================================")
print(" NETWORK ANALYSIS COMPLETED")
print("================================")
