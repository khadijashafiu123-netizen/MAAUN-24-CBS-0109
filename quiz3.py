from collections import deque

# Initialize queue and stack
application_inbox = deque()
processed_history = []

# List of messy startup application names
applications = [" TechCorp ", "Bio-gen ", " FinTech ", " HealthTech "]

# Ingest and clean data
for app in applications:
    cleaned_app = app.strip().lower()
    application_inbox.append(cleaned_app)

# Process applications (FIFO)
while application_inbox:
    name = application_inbox.popleft()
    print(f"Approving: {name}")
    processed_history.append(name)

# Undo last approval (LIFO)
if processed_history:
    last_approved = processed_history.pop()
    print(f"Reverting approval for: {last_approved}")