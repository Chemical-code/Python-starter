# Import module
import sys

# Print commend parameter
print(sys.argv)
print("---")

# Print computer environment and the information
print("platform:", sys.platform)
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# Forced quit the system
sys.exit()