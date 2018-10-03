allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
			 'Bob': {'ham sandwiches': 3, 'apples': 2},
			 'Carol': {'cups': 3, 'apple pies': 1}}


def total_bought(guest, item):
	count = 0
	for k, v in guest.items():
		count += v.get(item, 0)
	return count


apple_count = total_bought(allGuests, 'apples')
print(apple_count)
