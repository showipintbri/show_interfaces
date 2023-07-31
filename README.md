# `show interfaces` command output
Explanation of Cisco's `show interfaces` command output.

Using the below example command output we assign a unique "ID" to each element we want to describe.
```
TenGigabitEthernet1/5/4 is up, line protocol is up (connected)
  Hardware is C6k 10000Mb 802.3, address is 0000.0000.fd90 (bia 0008.ef4a.fd90)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 100 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, media type is 10Gbase-SR
  input flow-control is on, output flow-control is off
  Clock mode is auto
  ARP type: ARPA, ARP Timeout 04:00:00
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

!! the above show output is from: https://www.ciscozine.com/show-interface-in-depth/ I'm using as a template
!! until I can replace it with my own from our particular IOS version and platform.
```

### Repo Structure
```
Repo:
  |--build_site/
  |      (scripts to build the site)
  |
  |--show_interfaces/ # Folder Name == Command
       |
       |--ios_xe.id   # Annotated file, using HTML/XML-like styled ID tags. This is the file
       |              #   the build scripts use to setup the folder structure and files
       |--ios_xe.raw  # Raw Command Output scraped from the CLI
       |
- - - -|- - - - <[Everything from here up is manually created. From here Down is automated]> - - - - -
       |
       |--ios_xe/     # Folder Name is determined by the *.id filename. Build scripts buld this folder.
            |
            |--[tag_name]/  # Folder name is dtermined by the ID tags in the *.id file. The build script sets this up.
                 |
                 |--summary.md       # Short blurb about the elements purpose.
                 |--configuration.md # If the element can be configured, how?
                 |--details.md       # Detailed explanation, including diagrams or any content necessary.
                 |--links.md         # List of links to external resources, to explain further.
```

1. Each element inside the `[os_name].id` file has a tag. I call this tag the "ID" tag.
2. Each ID has a folder.
3. Inside each folder are description documents written in Markdown.
4. Common documents inside each folder are:
   - Summary: `summary.md` - Short blurb about the elements purpose.
   - Configuration: `configuration.md` - If the element can be configured, how?
   - Detailed Explanation: `details.md` - Detailed explanation, including diagrams or any content necessary.
   - Links: `links.md` - List of links to external resources, to explain further. Good place to link to vendor documentation.

## How can I add a new command or missing OS output?
1. Add folder to the root dir of repo. Folder name should be the generalized command using lowercase and underscores.
2. In the new folder make 2 new files each named with the OS the output is from. Examples: "nx_os", "ios_xr", "ios", "ios_xe". One file extension should end in: ".raw" and the other ".id".
3. Start marking up the *.id file you just created making sure to use unique ID names.
4. When finished, run the build script:
   ```
   cd [repo_root]
   python3 build_site/main.py
   ```
   This will setup all the folders and Markdown file placeholders for you based on the ID tags you marked up your *.id file with.
