Rimwork - Steam Workshop Mod Monitor for RimWorld
This Python script monitors the Steam Workshop directory for new mod folders created by RimWorld and copies them to a different directory while renaming them according to their name in their About.xml file.

Installation
Clone this repository or download the script.
Install Python 3.x or higher.
Install the xml.etree library by running pip install xml.etree.ElementTree in your command prompt or terminal.
Usage
Set the src_dir variable to the directory where RimWorld creates mod folders in the Steam Workshop folder.
Set the dst_dir variable to the directory where you want the mod folders to be copied and renamed.
Run the script in your command prompt or terminal using python <path-to-script>.
The script will run continuously, monitoring the src_dir for new mod folders and copying them to dst_dir while renaming them. The script will also ignore any folders starting with .temp_write_ and any mod folders that have already been processed.

Disclaimer
This script is provided as-is and without any warranties. The author is not responsible for any damage or loss resulting from the use of this script. Use at your own risk.
