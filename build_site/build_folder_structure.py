# This file can build the template folder structure and placeholder *.md files based on a single 'tagged'/'annotated'  show interfaces output
# Simply execute this script and supply the filename of the annotated file: 
# "build_folder_structure.py show_interfaces.id"


import re
import os

# Example "id" string below. Ideally we want to open the file *.id in the OS folder and load it as a string to be parsed
id = """<physical_status>TenGigabitEthernet1/5/4 is up</physical_status>, <line_protocol>line protocol is up (connected)</line_protocol>
  <hardware_is>Hardware is C6k 10000Mb 802.3</hardware_is>, <mac_addr_is>address is 0000.0000.fd90</mac_addr_is> <bia>(bia 0008.ef4a.fd90)</bia>
  <mtu>MTU 1500 bytes</mtu>, <bandwidth>BW 10000 Kbit/sec</bandwidth>, <delay>DLY 100 usec</delay>,
     <reliability>reliability 255/255, txload 1/255, rxload 1/255</reliability>
  <encapsulation>Encapsulation ARPA</encapsulation>, <loopback>loopback not set</loopback>
  <keepalive>Keepalive set (10 sec)</keepalive>
  <duplex>Full-duplex</duplex>, <speed>10Gb/s</speed>, <media_type>media type is 10Gbase-SR</media_type>
  <flow_control>input flow-control is on, output flow-control is off</flow_control>
  <clock_mode>Clock mode is auto</clock_mode>
  <arp_type>ARP type: ARPA</arp_type>, <arp_timeout>ARP Timeout 04:00:00</arp_timeout>
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 7000 bits/sec, 8 packets/sec
  5 minute output rate 10000 bits/sec, 11 packets/sec
  L2 Switched: ucast: 0 pkt, 0 bytes - mcast: 0 pkt, 0 bytes
  L3 in Switched: ucast: 0 pkt, 0 bytes - mcast: 0 pkt, 0 bytes mcast
  L3 out Switched: ucast: 0 pkt, 0 bytes mcast: 0 pkt, 0 bytes
     4495527 packets input, 488522378 bytes, 0 no buffer
     Received 4460539 broadcasts (1153347 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     6925984 packets output, 825456963 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
"""

def find_all_tags(string):
    # re.findall(pattern, string, flags=0)
    list = re.findall('</*\w+>', string)
    return list

all_tags = find_all_tags(id)

# print(all_tags)

def find_all_start_tags(string):
    import re
    # re.findall(pattern, string, flags=0)
    list = re.findall('<\w+>', string)
    start_tags = [tag for tag in list if tag[1] != '/']
    return start_tags

start_tags = find_all_start_tags(id)

# print(start_tags)

def extract_tag_text(tag):
    remove_first_char = tag[1:]
    remove_last_char = remove_first_char[:-1]
    return remove_last_char

def extract_all_tag_text(list):
    new_list = []
    for i in list:
        just_text = extract_tag_text(i)
        new_list.append(just_text)
    return new_list

just_tag_text = extract_all_tag_text(start_tags)

# print(just_tag_text)
        

def get_tag_and_element(string: str, all_raw_tag_text: list) -> list:
    list_of_dicts = []
    for tag in all_raw_tag_text:
        w = re.search(f'<{tag}>(?P<element>.+)</{tag}>', string)
        elem = w.group('element')
        d = {'tag': tag, 'element': elem}
        list_of_dicts.append(d)
    return list_of_dicts
        
        
list_of_dicts = get_tag_and_element(id, just_tag_text)

print(list_of_dicts)

for dict in list_of_dicts:
    foldername = dict['tag']
    print(foldername)
    if not os.path.exists(foldername):
        os.makedirs(foldername)