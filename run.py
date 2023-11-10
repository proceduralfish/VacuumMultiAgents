from vacuums_model import VacuumsModel
import time

def test_simulation(M,N,num_agents,percentage_dirty_cells,max_execution_time):
    model = VacuumsModel(M,N,num_agents,percentage_dirty_cells,max_execution_time)

    start_time = time.time()
    time_passed = 0.0

    while (time_passed<=model.max_execution_time) and (not model.all_cells_clean()):
        model.step()
        time_passed = time.time() - start_time


    if (model.all_cells_clean()):
        print(f"Time required to clean all cells: {time_passed}")
    else:
        print(f"Time limited exceeded ({model.max_execution_time})")

    print(f"Clean cells -> {model.percentage_cells_clean()}%")

    print(f"Total movements of all agents: {model.total_movements}")


test_simulation(1000,1000,100,.30,20)