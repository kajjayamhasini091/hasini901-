#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

const int GRID_SIZE = 4;       // 4x4 grid
const int SQUARE_SIZE = 100;   // Each square size in pixels

// Random color generator
sf::Color randomColor() {
    int r = rand() % 256;
    int g = rand() % 256;
    int b = rand() % 256;
    return sf::Color(r, g, b);
}

int main() {
    srand(time(0));

    sf::RenderWindow window(sf::VideoMode(GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE), "Colored Squares Game");

    // Create grid of squares
    vector<sf::RectangleShape> squares;
    for (int row = 0; row < GRID_SIZE; row++) {
        for (int col = 0; col < GRID_SIZE; col++) {
            sf::RectangleShape square(sf::Vector2f(SQUARE_SIZE - 2, SQUARE_SIZE - 2));
            square.setPosition(col * SQUARE_SIZE, row * SQUARE_SIZE);
            square.setFillColor(randomColor());
            squares.push_back(square);
        }
    }

    // Target color
    sf::Color targetColor = sf::Color::Red;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();

            if (event.type == sf::Event::MouseButtonPressed) {
                if (event.mouseButton.button == sf::Mouse::Left) {
                    int x = event.mouseButton.x / SQUARE_SIZE;
                    int y = event.mouseButton.y / SQUARE_SIZE;
                    int index = y * GRID_SIZE + x;
                    squares[index].setFillColor(targetColor);
                }
            }
        }

        window.clear(sf::Color::Black);

        // Draw all squares
        for (auto &sq : squares) {
            window.draw(sq);
        }

