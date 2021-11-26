####################################
### This modules works with file ###
####################################


# Aibek
# 8. Get maximum length word
# - input: dictionary - aynimalyga at beru kerek
# - output: maximum length word   
def find_longest_word(dict1): 
    print('find_longest_word function') 
    lendict1 = len(dict1)
    return lendict1 

# Test all functions here
if __name__ == "__main__":
   print("Testing module ...")
   
   content = data_loader('brown_short.txt')
   dict1 = get_word_counts(content)
   print()  # dictionary uzyndygyn wigaru kerek
   print(count_average(dict1))

  
