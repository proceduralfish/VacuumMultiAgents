import mesa  # type: ignore
import time



class VacuumAgent(mesa.Agent):
    """An agent that represent a vacuum"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.model.total_movements +=1

        

    def clean_current_cell(self):
        x, y = self.pos
        (current_cell_is_dirty) = self.model.bool_grid[y][x]

        if (current_cell_is_dirty):
            self.model.bool_grid[y][x] = False
            self.model.total_clean_cells +=1
        else:
            self.move()

    def step(self):
        self.clean_current_cell()


class VacuumsModel(mesa.Model):
    """A model with all the vacuums and grid with bool values"""

    def __init__(self, M, N, num_agents, percentage_dirty_cells, max_time):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(M, N, True)
        self.bool_grid = [[0 for j in range(M)] for i in range(N)]
        self.schedule = mesa.time.RandomActivation(self)
        self.total_movements = 0

        self.total_cells = M*N
        count_dirty_cells = int(self.total_cells*percentage_dirty_cells)

        self.total_clean_cells = 0
        self.max_execution_time = max_time

        # all cells are initially clean:
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                self.bool_grid[y][x] = False
                self.total_clean_cells +=1

        

        # random initial dirty cells
        for i in range(count_dirty_cells):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            if (self.bool_grid[y][x]==False):
                self.bool_grid[y][x] = True
                self.total_clean_cells-=1

        # Creating agents:
        for i in range(self.num_agents):
            a = VacuumAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (1, 1))

    def step(self):
        self.schedule.step()

    def all_cells_clean(self):
        return self.total_clean_cells==self.total_cells
    
    def percentage_cells_clean(self):
        return (self.total_clean_cells*100)/self.total_cells


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

    print()