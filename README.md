# Asteroid Game(WIP) started 01/01/2026

A fast-paced space shooter game built using Python and the Pygame library

**Controls**: WASD - movement, SPACE - shoot

**Status:** This project is currently in development. A basic prototype, features on the way include: see roadmap

## Getting Started

The easiest way to run the game is using **uv**. You don't need Python installed, **uv** handles everything.

### Prerequisites

First, install **uv**

### Installation & Run

1. **Clone the repository:**
   git clone github.com/SpoopyBlob/Asteroid_game
   cd Asteroid_game
   
2. **Run the game:**
   uv run main.py

   This command will automatically install **pygame**, create a virtual environment and launch the game for you

## 🗺️ Project Roadmap

Features marked with `[ ]` are planned for future updates.

-   [x] Player movement (Rotation & Thrust) + Shooting mechanics (Bullets) 
-   [x] Asteroid sprites + spawn behaviour
-   [x] Collision system + behaviour
-   [x] Optimisation (pre-cache assets, sprite_lookup(dict/hashmap), soft_collision_check) 
-   [ ] Unit tests for "functional core" (logic.py, collisions.py, state.py) due 11/01/2026
-   [ ] Sprite_fx animation for world events
-   [ ] High score/points system
-   [ ] Main menu and Game Over screens

## Technical notes:

1. Experimenting with implementing concepts from functional programming into OOP. 
2. Functional Core/ Imperative Shell: I am working to separate the games' "pure logic" from the imperative side effects, allowing for easier debugging and unit testing
3. Performance Optimisation:
   1. Implementing a sprite_lookup hashmap to optimise collision detection
   2. Pre-caching assets to reduce overhead by managing resources in a dedicated module

      





