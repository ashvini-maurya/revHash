letters = "acdegilmnoprstuw"
letters_list = list(letters)

class ReverseHash(object):
	def rev_hash(self, _hash):
		hash_type = (int)	
		if isinstance(_hash, hash_type):
			arr = []
			for i in range(7, 0, -1):
				remainder = _hash % 37
				char_in_letter = letters_list[remainder]
				arr.append(char_in_letter)
				_hash = (_hash)/37
		

			final_str =  ''.join(arr)
			return final_str[::-1]

		else: 
			raise ValueError


#hash_value = input("Please enter hash: ")
#result = ReverseHash().rev_hash(hash_value)
#print result
