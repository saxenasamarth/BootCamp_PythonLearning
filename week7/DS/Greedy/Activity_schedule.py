def sort_activities(activity_list, start_time, end_time):
	activites = zip(activity_list, start_time, end_time)
	activites = sorted(activites, key=lambda x: x[2])
	chosen = [activites[0][0]]
	end_time = activites[0][2]
	for act in activites[1:]:
		if act[1] > end_time:
			chosen.append(act[0])
			end_time = act[2]
	return chosen
	
activity_list = [0, 1, 2, 3, 4, 5, 6]
start_time = [4, 1, 9, 5, 12, 18, 6]
end_time = [12, 7, 14, 6, 13, 20, 10]
print(sort_activities(activity_list, start_time, end_time))	