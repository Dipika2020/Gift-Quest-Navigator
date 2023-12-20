# Gift-Quest-Navigator
A Python-powered software tool aiding Santa's gift delivery which uses various pathfinding algorithms and visuals for efficient sleigh routes.


It provides a suite of pathfinding algorithms and visualization tools to determine the most efficient path for Santa's sleigh, ensuring timely gift deliveries during the holiday season.

This project aims to solve the challenge of guiding Santa's sleigh through diverse maps, avoiding obstacles, and efficiently reaching all gift locations to ensure a seamless gift-giving experience.

Key Features
1. Pathfinding Algorithms
Uniform Cost Search (UCS)
Breadth-First Search (BFS)
A Algorithm (A-Star)*
Iterative Deepening Search (IDS)
2. Bidirectional Search
The software employs bidirectional search techniques to find optimal routes efficiently, reducing traversal time and ensuring timely deliveries.

3. Visualization
Utilizes Pygame for visual representation, displaying the movement and navigation of Santa's sleigh across the maps.

4. User Interface
Offers a user-friendly interface for inputting map configurations and observing the pathfinding process visually.

Installation Prerequisites
- Python 3.x
- Pygame library
  
Steps
- Clone the repository: git clone <repository_url>
- Install required dependencies: pip install -r requirements.txt
- Run the program: python main.py <algorithm_type>
- Replace <algorithm_type> with one of the following: ids, a_star, bd_bfs, ucs

Usage
- Launching the Program: Run main.py with the chosen algorithm type.
- Interface Interaction: Follow on-screen prompts to observe Santa's sleigh navigating the map.
