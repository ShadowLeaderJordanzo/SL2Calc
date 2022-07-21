# SL2Calc
    remake of https://neus-projects.net/forums/showthread.php?tid=6498

# TO DO 
    make classes for resistance
    make classes for Health/FP
    make a 'Person' class, probably hold things like SWA, hit, evade maybe health/fp res
        i could probably just have everything under person but that'd make it more of like a global storage for stuff
    
    make stats influence their respective things
        have aptitude increase invested by 1 for everything
        make shift click open an input value box
            add feature to let overflow stas so you can have -
    add race selection that changes bases
        add class/sub class
            add food
        

    perosn class seems like the best idea, if there's the head of everything that is handled and that updates, it will be easier to update the calculator every update
        person class has stat handler, also def handler for resistances/evade, then attack handler for hit, ele atk, etc

# FEATURES
    folder that parse text files and auto adds weapons to it when initialized
        this could work for races/classes and weapons, as it is currently a database handles all of this stuff, although i've never packaged things so im unsure how that'd work

# Refactors
    redo balloons, its deprecated and ugly
