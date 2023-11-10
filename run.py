from vacuums_model import test_simulation


"""NOTE THAT THE NUMBER OF AGENTS IS DIRECLTY 
PROPORTIONAL TO THE TIME REQUIRED TO CLEAN ALL CELLS """


"""One single agent is most likely to clean all the grid than 10000 agents"""

test_simulation(500,500,10000,.50,20)

test_simulation(500,500,100,.50,20)

test_simulation(500,500,100,.50,20)

test_simulation(500,500,1,.50,20)