
# No of lanes = 4
class Intersection:
    def __init__(self):
        self.no_lanes = 4;
        self.inflow = []
        self.open_time = []
        self.cycle_len = 75*self.no_lanes
        self.max_len = 150
        self.min_len = 15

    # Update the inflows for each cycle
    def update_inflow(self, l:list):
        self.no_lanes = len(l);
        self.cycle_len = 75*self.no_lanes

        self.inflow = l

        # Fraction of total inflow
        fracs = [x/sum(l) for x in l]

        # Time for each direction
        times = []

        # Number of times min is reasdjusted
        min_count = 0

        # Update the times
        for f in fracs:
            times.append(int(f*self.cycle_len))
            if times[-1] < self.min_len:
                times[-1] = self.min_len
                min_count += 1
            elif times[-1] > self.max_len:
                times[-1] = self.max_len
        
        
        if sum(times) > self.cycle_len:
            #print('Exceeded by', sum(times) - self.cycle_len)
            n_fracs = [x/sum(times) for x in times]
            lanes = [f*self.cycle_len for f in n_fracs]
            #print(lanes, times, sum(times))
            self.update_inflow(lanes)

        elif sum(times) <= self.cycle_len:
            # Output time for each signal
            #print(l, times, sum(times))
            self.open_time = times




in1 = Intersection()
in1.update_inflow([2, 2, 234, 21])
print(in1.open_time, sum(in1.open_time))
            