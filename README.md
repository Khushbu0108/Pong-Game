# Pong-Game
This is a simple and fun recreation of the classic Pong game using Python's turtle module. The game includes basic mechanics such as paddle control, ball bouncing, collision detection, and score tracking. It's a great beginner project for anyone learning object-oriented programming in Python!

# How to Play
- **Left Paddle:**  
  - Move up → `W`  
  - Move down → `S`

- **Right Paddle:**  
  - Move up → `Up Arrow`  
  - Move down → `Down Arrow`

- Keep the ball from passing your paddle.
- A point is scored when your opponent misses the ball.
- The ball speeds up each time it hits a paddle!

# Project Structure
pong-game/
│
├── main.py # Game loop and setup
├── paddle.py # Paddle class (movement & setup)
├── ball.py # Ball class (movement, bounce, reset)
└── scoreboard.py # Score display and updates

# Key Concepts Used

- Python OOP (Object-Oriented Programming)
- `turtle` module for graphics
- Collision detection
- Keyboard event handling
- Game loop and animation with `tracer()` and `update()`
