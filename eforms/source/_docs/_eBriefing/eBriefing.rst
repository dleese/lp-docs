=========
eBriefing
=========
The *eBriefing*/*EFF* module enables work and collaboration on Electronic Flight Folder (EFF) packages. These packages represent the electronic version of the Flight-briefing documentation. They contain all the flight related documents and data such as OFP, weather, weather charts, NOTAMs in a standardized data structure. 
EFF packages are always assigned to a particular flight and to a particular crew. Pilots can enter data in specific areas of the flight plan and acquire last-minute updates and revisions.
In following the structure and the functions of the briefing module are described in detail.
When selecting the Briefing icon from the navigation tab-bar, Briefing packages assigned to the User’s role are shown.

Navigation
----------
Navigation elements of the Briefing module are organized as follows:

- Left-Hand side: UTC time
- Center: Module name
- Right-Hand side: Sort button, Views button, Connection to other devices and Brightness button

Sort
====
The sort popover contains the following sorting options: 

:.. figure:: 


    Sort options for eBriefing
    
- by Display Name
- by Flight ID
- STD (Scheduled Time of Departure)
  
  It is possible to sort the Briefings both in ascending and descending order.

Filter
======

The briefing packages are filtered according to specific filter settings, that can be changed in app settings. 

:.. figure:: 


    Select Settings icon

  To change the settings switch to Home-Tab and in the Navigation select Settings.

In the pop up, scroll to Briefings section and configure appropriately.

Briefing Home / Recent briefing packages overview
-------------------------------------------------

Briefing Roles
==============

Briefing State
==============

Briefing state can have one of four values:

- *Ready* this initial state is a read-only one. No data can be entered. 
- *Active* this state allows the user to enter the data.
- *Finalized* before submitting Briefing packages to the ground, the current active Briefing needs to be finalized. Only the the master 
user is allowed to send packages to the ground. Depending on a particular configuration, Briefing can only be finalized when all 
required input fields are filled. A check list of required fields can be found in the subsection Flight Summary of the Flight Plan Section.
- *Archived* Finalized briefings which were successfully synchronized back to the server get status “archived”