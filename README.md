# Image Recommender Application

The Image Recommender Application is a web-based tool designed to provide personalized image recommendations to users based on their interactions with displayed images. The application leverages the epsilon-greedy bandit algorithm to dynamically adjust recommendations according to user preferences, making it a practical example of reinforcement learning in action.

## Features

- **User Interaction**: Users can view a selection of images presented on the web page. Each image is accompanied by "Like" and "Unlike" buttons to capture user feedback.
- **Image Source**: Images are fetched from the LoremFlickr service based on predefined tags such as "nature," "technology," "people," "food," and "travel." Multiple images are retrieved for each tag to populate the initial image pool.
- **Epsilon-Greedy Bandit Algorithm**: The algorithm maintains a balance between exploration and exploitation to optimize image recommendations. It starts with a set of initial values and updates its recommendations based on user interactions.
- **Dynamic Recommendations**: After a user has interacted with the displayed images and clicks the "Finish" button, the application processes the feedback. The epsilon-greedy bandit algorithm updates the reward values for the tags based on the feedback and provides new recommendations.
- **Flask Web Framework**: The application is built using Flask, a lightweight web framework for Python. The server handles requests for initial image sets and subsequent recommendations, sending JSON data back to the client-side script for rendering.
- **Client-Side Functionality**: The client-side, implemented in HTML and JavaScript, dynamically updates the displayed images based on server responses. It captures user interactions and sends them back to the server for processing.

## Technical Implementation

### Backend

- Powered by Flask, which serves the HTML page and handles AJAX requests for image recommendations.
- The `EpsilonGreedyBandit` class manages the recommendation logic, updating the values of each tag based on user feedback.

### Frontend

- A simple HTML page enhanced with JavaScript to handle dynamic content updates.
- JavaScript functions capture user interactions, send them to the backend, and update the displayed images based on the server's recommendations.

## Flow of the Application

1. **Initial Load**: When the user first loads the page, a set of images is fetched and displayed.
2. **User Interaction**: The user interacts with the images by liking or unliking them.
3. **Feedback Submission**: Upon clicking "Finish," the interactions are sent to the server.
4. **Recommendation Update**: The server processes the feedback using the epsilon-greedy bandit algorithm and updates the values associated with each tag.
5. **New Recommendations**: A new set of recommended images is fetched and sent back to the client for display.

## Installation and Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/image-recommender.git
    cd image-recommender
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Run the application**:
    ```sh
    python app.py
    ```

4. **Open the application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

### Note on Virtual Environment

The project was developed using a virtual environment to manage dependencies. However, due to the large number of files, the virtual environment directory (`venv`) is not included in the repository as GitHub restricts the upload of too many files. You can recreate the virtual environment using the instructions above.

## Dependencies

- Flask
- Requests (if fetching images from an API)

## Acknowledgments

- LoremFlickr for providing the images.


