def job_sequencing(activities, deadlines, profits):
	chosen_deadlines = {}
	activity_list = zip(activities, deadlines, profits)
	activity_list = sorted(activity_list, key=lambda x:-x[2])
	chosen_activies = []
	total_profit = 0
	for act in activity_list:
		if act[1]-1 not in chosen_deadlines:
			chosen_deadlines[act[1]-1] = True
			chosen_activies.append(act[0])			
			total_profit+=act[2]
		else:
			for i in range(act[1]-2, -1, -1):
				if i not in chosen_deadlines:
					chosen_deadlines[i] = True
					chosen_activies.append(act[0])
					total_profit+=act[2]
					break
	return chosen_activies, total_profit		

activities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deadlines = [9, 2, 5, 7, 4, 2, 5, 7, 4, 3]
profits = [15, 2, 18, 1, 25, 20, 8, 10, 12, 5]
print(job_sequencing(activities, deadlines, profits))