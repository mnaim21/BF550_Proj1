    def __init__(self, dt):
        # Initialize error flag
        self.flag = False
        # Checks if list parameter is two dimmensional, if not, converts list
        # into two dimmensions (nested list)
        if any(isinstance(x, list) for x in dt) == False:
            dt = [dt]
        # Checks if rows are consistent in length
        n_cols = len(dt[0]) # Length of rows/number of columns
        for x in dt:
            if len(x) != n_cols:
                print("Error: row length must be consistent")
                self.flag = True
        if self.flag == False:
            # self.data contains array as a nested list
            self.data = dt
            # self.size returns the total number of entries in the array
            self.size = len(dt)*len(dt[0])
            # self.shape returns a tuple containing the number of rows
            # followed by the number of columns
            self.shape = (len(dt), len(dt[0]))
        # Checks if error has been detected, if so, sets class data to None
        if self.flag == True:
            self.data = None
            self.size = None
            self.shape = None
