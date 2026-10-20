# OpenGL Snake Game

A C++ desktop Snake project by Xander Kyle Solancho, using OpenGL and FreeGLUT.
The published `opengl-snake.cpp` is an unchanged copy of the supplied project source.

## Features shown in the source

- 30 × 20 grid, rendered in a 750 × 500 window.
- Snake and food drawn with OpenGL quads, plus a line grid and bitmap text.
- Arrow-key input, timer-driven updates, and double-buffered rendering.
- Food adds 10 points and grows the snake.
- Wall and self-collision checks, with start and game-over screens.
- R restarts after game over; Esc quits.

This version does not implement WASD controls or a pause key.

## Build on Windows with MSYS2 UCRT64

Requirements: a C++17 compiler, FreeGLUT headers/libraries, OpenGL, and GLU.
With MSYS2 UCRT64 GCC and FreeGLUT installed, run from a UCRT64 terminal:

```sh
g++ -std=c++17 -Wall -Wextra opengl-snake.cpp -lfreeglut -lopengl32 -lglu32 -o opengl-snake.exe
./opengl-snake.exe
```

Keep the FreeGLUT runtime library available on PATH when running the executable.
This is a native desktop project, not a browser-playable game.

The portfolio description was checked against the source. Gameplay was not newly tested as part of adding this portfolio entry.
