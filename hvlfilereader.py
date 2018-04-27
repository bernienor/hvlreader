# Samleklasse for import av datafiler inn i Python. 
#
# The idea is to make a general importer to easy the work involved in setting
# up new programs for post processing of test data.
#
# Main attributes:
# * data ( the data set)
# * sample_interval
# * timestamp_of_first_sample (default 0)
#
#
# Nice to have attributes:
# * scale (default 1)
# * unit (default "")
# * source_file_type (subclass of reader)
# * file_timestamp (timestamp in the filesystem of the file)
# * data_timestamp (time and date read from the file)


    class hvlfilereader:

    


    data = np.loadtxt(file_name, delimiter=',', skiprows=16)