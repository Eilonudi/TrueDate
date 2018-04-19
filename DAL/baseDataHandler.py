# constants
FILE_PREFIX = ".csv"


class baseDataHandler():
    '''Basi Data handler class.
    Abstract.'''

    def appendRowToFile(object):
        '''generic writing to file through simply running on all the instance variables'''

        try:
            # open the file for writing
            with open(object.__class__.__name__ + FILE_PREFIX, 'w') as dataFile:
                # iterate the values
                for currObjectValue in object.__dict__.items():
                    # write a single value, put a semi-colon for next column
                    dataFile.write(currObjectValue + ",")

                # end line
                dataFile.write("\n")

            return True

        except:
            return False
