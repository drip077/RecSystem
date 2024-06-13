import random
import torch
import torch.nn as nn
import torch.optim as optim

input_size = 5
hidden_size = 10
output_size = 5
learning_rate = 0.01


class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out


model = SimpleNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

tags = ['cat', 'dog', 'nature', 'food', 'car']
tag_scores = {tag: 0.0 for tag in tags}
epsilon = 0.5

def fetch_images():
    images = []
    selected_tags = []
    for _ in range(5):
        tag = select_tag()
        url = f"https://loremflickr.com/320/240/{tag}?random={random.randint(1, 10000)}"
        images.append((url, tag))
        selected_tags.append(tag)
        print(f"Selected tag: {tag}, URL: {url}")
    return images


def select_tag():
    global epsilon
    scores = torch.tensor([tag_scores[tag] for tag in tags], dtype=torch.float)
    with torch.no_grad():
        predictions = model(scores.unsqueeze(0))

    if random.random() < epsilon:
        tag = random.choice(tags)
    else:
        tag = tags[torch.argmax(predictions).item()]

    epsilon = max(0.1, epsilon * 0.99)

    return tag

def update_model(chosen_tag, reward):
    tag_index = tags.index(chosen_tag)
    inputs = torch.tensor([tag_scores[tag] for tag in tags], dtype=torch.float).unsqueeze(0)
    target = torch.zeros(output_size)
    target[tag_index] = reward
    output = model(inputs)

    loss = criterion(output, target.unsqueeze(0))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    tag_scores[chosen_tag] += reward if reward == 1 else -1
    print(f"Updated tag_scores: {tag_scores}")
