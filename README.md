This is an archived project i had completed in my time at University.
The files available to me were incomplete. The original main.py file was in the Raspberry Pi provided by the university which is lost to me.
there are individual sections on how the project would have worked.

How it would have worked:
1. There are switches that would activate a "mode", usually between a passive and active mode.
2. passive mode is the HC-SR04 ultrasonic sensor. It takes multiple readings in a second and provide audio via speaker or the headphone jack to inform the user of what's ahead.
3. The active mode is the OpenCV Image recognition mode. It uses COCO to figure out objects using the PiCamera's video feed. This mode is not recommended as it is very resource intensive and unoptimised. The Pi camera is also really slow and functions at leass than 10 frames per second.
4. Finally the last switch just opens and closes the entire system.

The project is meant to be an attachment a person with vision difficulties would strap onto their walking stick and plug into their ear via the headphone jack. The module would have come with a replacable battery.

Note: Also, the main.py provided does not belong to this project. it is from bitBybit and was misplaced into this repository. It might be an explanation as to why the main.py file that would have controlled the entire project is missing in the first place,
maybe i just replaced it accidentally with one from another project
