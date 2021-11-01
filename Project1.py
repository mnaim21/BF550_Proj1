#########

# Project 1
# Group 7
# Group members:
    # Meghana Saradchandra Peshwa
    # Dylan Beeber
    # Vishwa Talati
    # Maha Naim

#########

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
    
    
    # Interactive prompt output overload - not required by the project
    # Sets the output in the interactive prompt to the data list, helpful for
    # testing and visualizing this class
    def __repr__(self):
        formatted_array = str(self.data).replace('],', '],\n')
        return formatted_array
    
    
    # Transpose method
    def transpose(self):
        """This method finds the transpose of a matrix"""
        A = []
        # Getting the number of rows and columns of the matrix
        rows, cols = self.shape
        # Finding the transpose by first looping through the columns and then the rows
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(self.data[j][i])
            A.append(row)
        return array(A)
    
    
    # Get item method
    def __getitem__(self, key):
        """This method returns a element of the matrix at indices i and j"""
        # Getting the indices i,j from the key variable which is a tuple
        i,j = key
        try:
            return self.data[i][j]
        except Exception:
            print("Error accessing the required element. Please recheck the row and column index.")
    
    
    # Dot product method        
    def dot(self,B):
        """This method computes the dot product of 2 matrices"""
        
        # If B is not a list and not an object of the array class then print an error statement and return
        if(type(B).__name__!='list' and type(B).__name__!='array'):
            print("Error : wrong input type")
            return
            
        # Converting B into an object of the array class if it is a nested list 
        if(type(B).__name__=='list'):
            B = array(B)
        # Making sure B is of the right format
        if(B.flag==True):
            return
        
        # Getting the number of rows and columns of the matrices
        A_rows,A_cols = self.shape
        B_rows,B_cols = B.shape
        
        # Making sure B is non empty
        if(B_rows==0 or B_cols==0 or A_rows==0 or A_cols==0):
            print("Error: the arrays should be non empty")
            return
        
        # Making sure the number of columns in A is not equal to the number of rows in B
        if(A_cols!=B_rows):
            print("Error : the number of columns in the 1st matrix is not equal to the number of rows in the 2nd matrix.")
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

        return array(C)
    
    
    # Sum method
    def sums(self, dim = None):
        """to calculate the sum of the array for all elements as default, row wise and column wise as optional arguments"""
        b = []
        if (dim == 0):
        #row wise (dim == 1) works
            for i in self.data :
                rSum = 0;
                for j in i: 
                #sum += self.data[i][j];
                    rSum = rSum + j;
                b.append([rSum])   
            return array(b)    
    #column wise (dim == 0)
        elif (dim == 1):        
            csum = 0
            a = [[]]
            for i in range(self.shape[1]):
                csum = 0
                for j in range(self.shape[0]):
                    csum += self.data[j][i]
                a[0].append(csum)
            return array(a)    
        elif (dim == None):
            s = 0
        #sum of all elements (default) works
            for row in self.data:
                for elem in row:
                    s += elem
            return s 


    # Add method  
    def __add__(self, B):
        """ Adding two arrays element-wise """
        C = []
        if (type(B) == float) or (type(B) == int):
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Add i and j from arrays A and B
                    c = self.data[i][j] + B
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        else:
            # Turns B into an array if needed
            if type(B) == list:
                B = array(B)
            # Checks if dimensions of arrays are equal
            if self.size != B.size:
                print("Error : array dimensions must be equal")
                return
            # For every row starting with i in A
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Add i and j from arrays A and B
                    c = self.data[i][j] + B.data[i][j]
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        return array(C)
    

    # Multiplication method            
    def __mul__(self, B):
        """ Multiplying two arrays element-wise """
        C = []
        if (type(B) == float) or (type(B) == int):
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Multiplying i and j from arrays A and B
                    c = self.data[i][j] * B
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        else:
            # Turns B into an array if needed
            if type(B) == list:
                B = array(B)
            # Checks if dimensions of arrays are equal
            if self.size != B.size:
                print("Error : array dimensions must be equal")
                return
            # For every row starting with i in A
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Multiplying i and j from arrays A and B
                    c = self.data[i][j] * B.data[i][j]
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        return array(C)
    
    
    # Subtraction method        
    def __sub__(self, B):
        """ Subtracting two arrays element-wise """
        C = []
        if (type(B) == float) or (type(B) == int):
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Subtracting i and j from arrays A and B
                    c = self.data[i][j] - B
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        else:
            # Turns B into an array if needed
            if type(B) == list:
                B = array(B)
            # Checks if dimensions of arrays are equal
            if self.size != B.size:
                print("Error : array dimensions must be equal")
                return
            # For every row starting with i in A
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Subtracting i and j from arrays A and B
                    c = self.data[i][j] - B.data[i][j]
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        return array(C)
    
    
    # Division method
    def __truediv__(self, B):
        """ Dividing two arrays element-wise """
        C = []
        if (type(B) == float) or (type(B) == int):
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Dividing i and j from arrays A and B
                    c = self.data[i][j] / B
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        else:
            # Turns B into an array if needed
            if type(B) == list:
                B = array(B)
            # Checks if dimensions of arrays are equal
            if self.size != B.size:
                print("Error : array dimensions must be equal")
                return
            # For every row starting with i in A
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Dividing i and j from arrays A and B
                    c = self.data[i][j] / B.data[i][j]
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        return array(C)
    
    
    # Negation method
    def __neg__(self):
        A = []
        """ Negating a single array element-wise """
        # For every row starting with i in A
        for i in range(len(self.data)):
            # Initialized list to store the values for the C array
            temp = []
            # Storing the length of each row
            l = len(self.data[i])
            # For every value (j) in row i, column l
            for j in range(l):
                # Negate (aka multiple -1) to every i and j value
                self.data[i][j] = self.data[i][j] * -1
                temp.append(self.data[i][j])
            A.append(temp)
        return array(A)


    # Exponentiation method
    def __pow__(self, B):
        """ Exponentiating two arrays element-wise """
        C = []
        if (type(B) == float) or (type(B) == int):
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Exponentiating i and j from arrays A and B
                    c = self.data[i][j] ** B
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        else:
            # For every row starting with i in A
            for i in range(len(self.data)):
                # Initialized list to store the values for the C array
                temp = []
                # Storing the length of each row
                l = len(self.data[i])
                # For every value (j) in row i, column l
                for j in range(l):
                    # Exponentiating i and j from arrays A and B
                    c = self.data[i][j] ** B.data[i][j]
                    # Append the array values into the initialized list
                    temp.append(c)
                # Appending the array values into the initialized array
                C.append(temp)
        return array(C)
    
    
    # Mean method    
    def mean(self, dim):
        """To calculate the mean of the elements taking optional arguments from sum"""    
        if dim == 0:  #column wise
            mean = self.sum(dim)/self.shape[1]
        elif dim == 1: #row wise      
            mean = self.sum(dim)/self.shape[0]
        return mean
    
    
    # Caluclates a covariance matrix, assumes that data in initial matrix is
    # organized into variables by column
    # Uses the n-1 covariance method and treats columns as variables and
    # rows as samples (opposite from numpy)
    def var(self):
        """Generates covariance matrix"""
        # Takes mean of columns
        mean_vector = self.mean(1)
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
        covariance_matrix = temp_matrix / (self.shape[0]-1)
        return covariance_matrix
