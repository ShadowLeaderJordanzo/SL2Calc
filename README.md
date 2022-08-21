# SL2Calc
remake of https://neus-projects.net/forums/showthread.php?tid=6498

# Preview
![preview](https://media.discordapp.net/attachments/865819034838237187/1010909362195284128/unknown.png)

# TO DO 
make classes for resistance

~~make classes for Health/FP~~

~~make a 'Person' class, probably hold things like SWA, hit, evade maybe health/fp res~~

~~stats~~

~~elements~~

~~eleATK~~

eleRES

~~vitals~~

~~HP~~

~~FP~~

~~MODIFIERS~~

CHECKBOXES

defenses

    
make stats influence their respective things

~~have aptitude increase invested by 1 for everything~~

make shift click open an input value box

add feature to let overflow stas so you can have -

~~add race selection that changes bases~~

make it functional

~~add class/sub class~~

add main / sub class passive spinbox

make it functional 

~~add food~~

make it functional

# FEATURES
	folder that parse text files and auto adds weapons to it when initialized

	this could work for races/classes and weapons, as it is currently a database handles all of this stuff, although i've never packaged things so im unsure how that'd work

# Refactors
redo balloons, its deprecated and ugly

~~wrap stats around a frame so they  aren't forced to be randomly BIG~~

stat plus and minus should call back to person class and update everything, other updates should not.

this way when something like skill goes up it can update hit, ice atk, etc, but when a custom modifier for like ice atk goes up it wont

