print('N12.1_050723.py')

# HOLY, THIS CHAPTER IS ALOT. LOL
# Crying rn
# I wonder how long this will take me to learn
# T-T

# --- --- --- Network and Packets --- --- ---

# -- -- -- (TCP) Transport Control Protocol -- -- --
# Built on top of Internet Protocol

# Assumes IP might lose some data
# - stores and retransmits data if it seems to be lost

# Handles 'flow control' using a transmit window

# Provides a nice reliable pipe

# -- -- -- TCP Connections / Sockets -- -- --
# An Internet socket or network socket is an endpoint of a bidirectional inter-process
# communication flow across an Internet Protocol-based computer network, such as the Internet.

# -- -- -- TCP Port Numbers -- -- --
# A port is an application-specific or process-specific software communications endpoint

# It allows multiple networked applications to coexist on the same server.

# There is a list of well-known TCP port numbers.

# --- --- --- Sockets in Python --- --- ---
# Python has built-in support for TCP Sockets
import socket                                               # To use sockets
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET is making a socket that connects to the Internet
mysock.connect( ('data.pr4e.org', 80) )