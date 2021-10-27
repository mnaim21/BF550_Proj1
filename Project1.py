class array:
    '''
    This class imitates NumPy's array class
    '''
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
    
    # Caluclates a covariance matrix, assumes that data in initial matrix is
    # organized into variables by column
    def var(self):
        # Takes mean of columns
        mean_vector = self.mean()
        # Transpose mean to begin creation of mean matrix
        mean_vector = mean_vector.transpose()
        # Creates list of 1s that will be used to manipulate the mean_vector
        ones_list = []
        for x in range(0, self.shape[0]):
            ones_list.append(1)
        # Adapt ones list into ones vector
        ones_vector = array(ones_list)
        # Dot product of mean_vector and ones_vector to create matrix with
        # number of rows equal to initial matrix and column means for each
        # value
        mean_matrix = mean_vector.dot(ones_vector)
        # Transpose again to get mean_matrix in correct orientation
        mean_matrix = mean_matrix.transpose()
        # Initial matrix - mean
        temp_matrix = self - mean_matrix
        # Dot product of transposed temp_matrix and temp matrix
        temp_matrix = temp_matrix.transpose().dot(temp_matrix)
        # Divide temp_matrix by number of rows in initial matrix
        covariance_matrix = temp_matrix / self.shape[0]
        return covariance_matrix
    
    # Interactive prompt output overload - not required by the project
    # Sets the output in the interactive prompt to the data list, helpful for
    # testing and visualizing this class
    def __repr__(self):
        formatted_array = str(self.data).replace('],', '],\n')
        return formatted_array
    
    def transpose(self):
        A = []
        # Getting the number of rows and columns of the array object
        rows, cols = self.shape
        # Finding the transpose by first looping through the columns and then the rows
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(self.data[j][i])
            A.append(row)
        return A
    
    def __getitem__(self, key):
        # Getting the indices i,j from the key variable which is a tuple
        i,j = key
        try:
            return self.data[i][j]
        except Exception:
            print("Error accessing the required element. Please recheck the row and column index.")
            
    def dot(self,B):
        # If B is not an object of the array class then print an error statement and return
        if(type(B).__name__!='array'):
            print("Error : Please make sure the array is an object of the array class")
            return
        
        A_rows,A_cols = self.shape
        B_rows,B_cols = B.shape
        
        # Making sure the number of columns of the 1st matrix is not equal to the number of rows of the 2nd matrix
        if(A_cols!=B_rows):
            print("The number of columns of the 1st matrix is not equal to the number of rows of the 2nd matrix.")
            return
        
        # Initializing a variable that holds the dot product
        C = []
        
        for i in range(A_rows):
            # Initializing a variable that holds one computed row
            row = []
            for j in range(B_cols):
                # Initializing a variable that holds the sum of product of elements in the respective row and column of A and B
                total = 0
                # Computing the sum of product of elements in the respective row and column of A and B
                for k in range(A_cols):
                    total += self.data[i][k]*B[k,j]
                row.append(total)
            # Appending the computed row to the C matrix
            C.append(row)
        
        return C   
