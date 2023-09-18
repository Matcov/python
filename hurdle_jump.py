# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json 

#######  MY CODE STARTS HERE:  #########

##### In Python, you can indeed define one function inside another function. This is known as nested functions::: 

##### Attention: Intentation!

def jump_over():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for _ in range (6): ## Symbol _ could be a word: for step in range (6)
    jump_over()
