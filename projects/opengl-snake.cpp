#include <GL/glut.h>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <sstream>

using namespace std;

// ==========================================
// GAME SETTINGS
// ==========================================

const int GRID_WIDTH = 30;
const int GRID_HEIGHT = 20;
const int CELL_SIZE = 25;

const int WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE;
const int WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE;

// Bigger number = slower
int gameSpeed = 130;

// ==========================================
// POSITION STRUCTURE
// ==========================================

struct Position
{
    int x;
    int y;

    Position(int px, int py)
    {
        x = px;
        y = py;
    }
};

// ==========================================
// GAME VARIABLES
// ==========================================

vector<Position> snake;

int foodX;
int foodY;

int directionX = 1;
int directionY = 0;

int nextDirectionX = 1;
int nextDirectionY = 0;

int score = 0;

bool gameStarted = false;
bool gameOver = false;


// ==========================================
// NUMBER TO STRING
// ==========================================

string numberToString(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}


// ==========================================
// DRAW TEXT
// ==========================================

void drawText(float x, float y, string text)
{
    glRasterPos2f(x, y);

    for (unsigned int i = 0; i < text.length(); i++)
    {
        glutBitmapCharacter(
            GLUT_BITMAP_9_BY_15,
            text[i]
        );
    }
}


// ==========================================
// CHECK IF POSITION IS ON SNAKE
// ==========================================

bool positionOnSnake(int x, int y)
{
    for (unsigned int i = 0; i < snake.size(); i++)
    {
        if (snake[i].x == x &&
            snake[i].y == y)
        {
            return true;
        }
    }

    return false;
}


// ==========================================
// SPAWN FOOD
// ==========================================

void spawnFood()
{
    do
    {
        foodX = rand() % GRID_WIDTH;
        foodY = rand() % GRID_HEIGHT;

    } while (positionOnSnake(foodX, foodY));
}


// ==========================================
// RESET GAME
// ==========================================

void resetGame()
{
    snake.clear();

    // Starting snake
    snake.push_back(Position(10, 10));
    snake.push_back(Position(9, 10));
    snake.push_back(Position(8, 10));
    snake.push_back(Position(7, 10));

    directionX = 1;
    directionY = 0;

    nextDirectionX = 1;
    nextDirectionY = 0;

    score = 0;

    gameStarted = false;
    gameOver = false;

    spawnFood();

    glutPostRedisplay();
}


// ==========================================
// DRAW SQUARE
// ==========================================

void drawSquare(int x, int y)
{
    float left = x * CELL_SIZE;
    float bottom = y * CELL_SIZE;

    float padding = 2.0f;

    glBegin(GL_QUADS);

        glVertex2f(
            left + padding,
            bottom + padding
        );

        glVertex2f(
            left + CELL_SIZE - padding,
            bottom + padding
        );

        glVertex2f(
            left + CELL_SIZE - padding,
            bottom + CELL_SIZE - padding
        );

        glVertex2f(
            left + padding,
            bottom + CELL_SIZE - padding
        );

    glEnd();
}


// ==========================================
// DRAW GRID
// ==========================================

void drawGrid()
{
    glColor3f(
        0.12f,
        0.12f,
        0.12f
    );

    glBegin(GL_LINES);

    int i;

    for (i = 0; i <= GRID_WIDTH; i++)
    {
        glVertex2f(
            i * CELL_SIZE,
            0
        );

        glVertex2f(
            i * CELL_SIZE,
            WINDOW_HEIGHT
        );
    }

    for (i = 0; i <= GRID_HEIGHT; i++)
    {
        glVertex2f(
            0,
            i * CELL_SIZE
        );

        glVertex2f(
            WINDOW_WIDTH,
            i * CELL_SIZE
        );
    }

    glEnd();
}


// ==========================================
// DRAW FOOD
// ==========================================

void drawFood()
{
    // Red food
    glColor3f(
        1.0f,
        0.1f,
        0.1f
    );

    drawSquare(
        foodX,
        foodY
    );
}


// ==========================================
// DRAW SNAKE
// ==========================================

void drawSnake()
{
    for (unsigned int i = 0; i < snake.size(); i++)
    {
        if (i == 0)
        {
            // Snake head
            glColor3f(
                0.2f,
                1.0f,
                0.2f
            );
        }
        else
        {
            // Snake body
            glColor3f(
                0.0f,
                0.65f,
                0.0f
            );
        }

        drawSquare(
            snake[i].x,
            snake[i].y
        );
    }
}


// ==========================================
// DISPLAY
// ==========================================

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glLoadIdentity();

    drawGrid();

    drawFood();

    drawSnake();


    // --------------------------------------
    // SCORE
    // --------------------------------------

    glColor3f(
        1.0f,
        1.0f,
        1.0f
    );

    string scoreText =
        "SCORE: " + numberToString(score);

    drawText(
        10,
        WINDOW_HEIGHT - 20,
        scoreText
    );


    // --------------------------------------
    // START SCREEN
    // --------------------------------------

    if (!gameStarted && !gameOver)
    {
        glColor3f(
            0.2f,
            1.0f,
            0.2f
        );

        drawText(
            WINDOW_WIDTH / 2 - 60,
            WINDOW_HEIGHT / 2 + 25,
            "CLASSIC SNAKE"
        );

        glColor3f(
            1.0f,
            1.0f,
            1.0f
        );

        drawText(
            WINDOW_WIDTH / 2 - 120,
            WINDOW_HEIGHT / 2,
            "PRESS ARROW KEY TO START"
        );
    }


    // --------------------------------------
    // GAME OVER
    // --------------------------------------

    if (gameOver)
    {
        glColor3f(
            1.0f,
            0.2f,
            0.2f
        );

        drawText(
            WINDOW_WIDTH / 2 - 45,
            WINDOW_HEIGHT / 2 + 30,
            "GAME OVER"
        );


        glColor3f(
            1.0f,
            1.0f,
            1.0f
        );

        string finalScore =
            "FINAL SCORE: " +
            numberToString(score);

        drawText(
            WINDOW_WIDTH / 2 - 70,
            WINDOW_HEIGHT / 2,
            finalScore
        );


        drawText(
            WINDOW_WIDTH / 2 - 90,
            WINDOW_HEIGHT / 2 - 30,
            "PRESS R TO RESTART"
        );
    }


    glutSwapBuffers();
}


// ==========================================
// UPDATE GAME
// ==========================================

void updateGame()
{
    if (!gameStarted || gameOver)
    {
        return;
    }


    // Apply requested direction
    directionX = nextDirectionX;
    directionY = nextDirectionY;


    // Calculate new head position
    int newX =
        snake[0].x + directionX;

    int newY =
        snake[0].y + directionY;


    // ======================================
    // WALL COLLISION
    // ======================================

    if (newX < 0 ||
        newX >= GRID_WIDTH ||
        newY < 0 ||
        newY >= GRID_HEIGHT)
    {
        gameOver = true;
        return;
    }


    // ======================================
    // CHECK FOOD
    // ======================================

    bool ateFood = false;

    if (newX == foodX &&
        newY == foodY)
    {
        ateFood = true;
    }


    // ======================================
    // SELF COLLISION
    // ======================================

    /*
       If we are NOT eating food, the tail
       will disappear this turn.

       Because of that, we don't need to
       check the final tail segment.
    */

    unsigned int checkLength = snake.size();

    if (!ateFood && checkLength > 0)
    {
        checkLength--;
    }


    for (unsigned int i = 0; i < checkLength; i++)
    {
        if (snake[i].x == newX &&
            snake[i].y == newY)
        {
            gameOver = true;
            return;
        }
    }


    // ======================================
    // MOVE SNAKE
    // ======================================

    snake.insert(
        snake.begin(),
        Position(newX, newY)
    );


    // ======================================
    // EAT FOOD
    // ======================================

    if (ateFood)
    {
        score = score + 10;

        spawnFood();
    }
    else
    {
        // Remove last segment
        snake.pop_back();
    }
}


// ==========================================
// TIMER
// ==========================================

void timer(int)
{
    updateGame();

    glutPostRedisplay();

    glutTimerFunc(
        gameSpeed,
        timer,
        0
    );
}


// ==========================================
// ARROW KEYS
// ==========================================

void specialKeys(int key, int, int)
{
    if (gameOver)
    {
        return;
    }


    if (key == GLUT_KEY_UP)
    {
        // Prevent reversing directly downward
        if (directionY != -1)
        {
            nextDirectionX = 0;
            nextDirectionY = 1;

            gameStarted = true;
        }
    }


    else if (key == GLUT_KEY_DOWN)
    {
        // Prevent reversing directly upward
        if (directionY != 1)
        {
            nextDirectionX = 0;
            nextDirectionY = -1;

            gameStarted = true;
        }
    }


    else if (key == GLUT_KEY_LEFT)
    {
        // Prevent reversing directly right
        if (directionX != 1)
        {
            nextDirectionX = -1;
            nextDirectionY = 0;

            gameStarted = true;
        }
    }


    else if (key == GLUT_KEY_RIGHT)
    {
        // Prevent reversing directly left
        if (directionX != -1)
        {
            nextDirectionX = 1;
            nextDirectionY = 0;

            gameStarted = true;
        }
    }
}


// ==========================================
// NORMAL KEYBOARD
// ==========================================

void keyboard(
    unsigned char key,
    int,
    int
)
{
    // R = restart
    if (key == 'r' || key == 'R')
    {
        if (gameOver)
        {
            resetGame();
        }
    }


    // ESC = quit
    if (key == 27)
    {
        exit(0);
    }
}


// ==========================================
// OPENGL INITIALIZATION
// ==========================================

void initOpenGL()
{
    // Background
    glClearColor(
        0.03f,
        0.03f,
        0.03f,
        1.0f
    );


    // Projection
    glMatrixMode(GL_PROJECTION);

    glLoadIdentity();

    gluOrtho2D(
        0,
        WINDOW_WIDTH,
        0,
        WINDOW_HEIGHT
    );


    glMatrixMode(GL_MODELVIEW);

    glLoadIdentity();
}


// ==========================================
// MAIN
// ==========================================

int main(int argc, char **argv)
{
    srand(
        (unsigned int)time(NULL)
    );


    // Initialize GLUT
    glutInit(
        &argc,
        argv
    );


    // Double buffering + RGB
    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGB
    );


    // Window size
    glutInitWindowSize(
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    );


    // Window position
    glutInitWindowPosition(
        100,
        100
    );


    // Create window
    glutCreateWindow(
        "Classic Snake - OpenGL GLUT"
    );


    // Initialize OpenGL
    initOpenGL();


    // Initialize game
    resetGame();


    // GLUT functions
    glutDisplayFunc(display);

    glutSpecialFunc(specialKeys);

    glutKeyboardFunc(keyboard);


    // Start game timer
    glutTimerFunc(
        gameSpeed,
        timer,
        0
    );


    // Start GLUT
    glutMainLoop();


    return 0;
}
