from collections import deque

# Step 1: Initialize queue and stack
inbox_queue = deque()
history_stack = []

# Step 2: Ingest messy startup names
startup_list = [" FinTechX ", "Green-energy ", " CloudNet", "AI-start "]

# Clean the names and store them in the queue
for startup in startup_list:
    cleaned = startup.strip().lower()
    inbox_queue.append(cleaned)

# Step 3: Process applications (FIFO)
while len(inbox_queue) > 0:
    current = inbox_queue.popleft()
    print("Approving:", current)
    history_stack.append(current)

# Step 4: Undo last approval (LIFO)
if history_stack:
    removed = history_stack.pop()
    print("Reverting approval for:", removed)
