# exception_handling.py

def show_index(i):
	try:

		lis = [99.0, 85.0, 75.0, 73.0, 70.0, 69.0, 66.0, 60.0, 55.0]

		print("Role Number", lis[i])
		return None
	except TypeError:
		print("Please make sure your index is an integer!")

	except IndexError:
		print("Please make sure you are trying to print in range of 0 to ", len(lis))

	except Exception as e:
		print("Please check: ", e)

		return False

ind = int(input("Index:"))
show_index(ind)
# print(score)
