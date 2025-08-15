from queue import PriorityQueue

# Create an empty priority queue
priority_queue = PriorityQueue()

# Add elements to the priority queue
priority_queue.put((1, 'task1'))  # (priority, task)
priority_queue.put((3, 'task3'))
priority_queue.put((2, 'task2'))

# Pop elements from the priority queue
while not priority_queue.empty():
    priority, task = priority_queue.get()
    print(f"Processing {task} with priority {priority}")

