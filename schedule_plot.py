
import matplotlib.pyplot as plt
from collections import OrderedDict

task1 = [0, 6, 3]
task2 = [2, 5, 7]
task3 = [6, 10, 4]

# task_profiles is a dict containing [start time, duration, resource usage] for each activity
task_profiles = {1:task1, 2:task2, 3:task3}

fig, ax = plt.subplots()
resource_usage = {}
for task in task_profiles:
    start = task_profiles[task][0]
    duration = task_profiles[task][1]
    finish = start + duration
    resource = task_profiles[task][2]
    ax.broken_barh([(start, duration)], (0, resource), edgecolor='black', alpha=0.3)
    ax.text(start + duration/2, resource/2, '%d' %task, color='black')
    # updating resource usage
    try:
        resource_usage[start] += resource
    except:
        resource_usage[start] = resource
    try: 
        resource_usage[finish] += -resource
    except:
        resource_usage[finish] = -resource
# getting overall resource usage
resource_usage = dict(sorted(resource_usage.items()))
cumsum = 0
for time in resource_usage:
    cumsum += resource_usage[time]
    resource_usage[time] =  cumsum
# adding resource usage as step function
ax.step([x for x in resource_usage.keys()], [y for y in resource_usage.values()], where = 'post')

ax.set_xlim(0, max(resource_usage.keys())+5)
ax.set_ylim(0, max(resource_usage.values())+2)
ax.set_xlabel('time')
ax.set_ylabel('resource usage')
ax.set_xticks(range(0,max(resource_usage.keys())+5,2))

plt.savefig('myexampleschedule.png')

