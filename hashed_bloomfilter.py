from helper_function import * 
import pickle 

def spam_data(filename):     # Makes a list of spam data from  data base stored in mail_data.csv
    spam_data = []
    with open(filename) as f:
        lines = f.readlines()
    lines = lines[1:]

    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        tokens = line.split(",")  # Split the line into tokens
        if tokens[0] == "spam":
            spam_message = ' '.join(tokens[1:])
            spam_message=format_input(spam_message)
            spam_data.append(spam_message)

    return spam_data

spam_data_ = spam_data("mail_data.csv")     # list of spam emails

def bloom_filter(spam_data_):    # create bloom filter with a suitable size using spam data
    size=bloom_size(spam_data_)
    bloomfilter=initialize_bloom (size)

    for email in spam_data_:
        # Each spam email will be hashed 
        hash_value_1 = hash_fun_01(email,size)
        hash_value_2 = hash_fun_02(email,size)
        hash_value_3 = hash_fun_03(email,size)
        # setting the corresponding bits in the Bloom filter to 1.
        bloomfilter[hash_value_1] = 1
        bloomfilter[hash_value_2] = 1
        bloomfilter[hash_value_3] = 1
  
    return bloomfilter

# serializing
# created bloom filter pickle file

f = open("bloom_filter_serialized2", 'wb') #write bytes
pickle.dump(bloom_filter, f)
f.close()

# deserializing
# load bloom filter

f= open("bloom_filter_serialized2", 'rb')
bloom_filter_deserialized = pickle.load(f)

bloom=bloom_filter_deserialized(spam_data_)   # The serilized bloom filter