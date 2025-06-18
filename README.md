# Space Shooter Game (From Hack 110 Spring 2022)

A simple arcade-style space shooter built with Pygame where you defend against incoming asteroids.

## 🚀 Features

- Mouse-controlled spaceship
- Shoot projectiles to destroy asteroids
- Life system with 3 hearts
- Score based on survival time
- Smooth gameplay at 60 FPS

## 📋 Prerequisites

- Python 3.x
- Pygame

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/rikhilf/hack110.git
cd hack110
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 How to Play

Start the game from the `src` directory:
```bash
cd src
python game.py
```

### Controls
- **Mouse Movement**: Control spaceship position
- **Left Click**: Shoot bullets
- **Close Window**: Quit game

### Rules
- You start with 3 lives
- Each asteroid collision costs 1 life
- Shoot asteroids to survive
- Game ends when all lives are lost
- Final score is your survival time

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
