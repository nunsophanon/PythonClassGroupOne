# interest_rate.py

def get_rate(pri, r, t):

	rate_amount = (pri * r * t)/100

	return (rate_amount)

principle = 10000
rate = 0.5

rate_of_six = get_rate(principle, rate, 6)
print("Six month = ", rate_of_six)