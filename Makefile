# Default target (runs the game)
.PHONY: default
default: run

# Run the game
.PHONY: run
run:
	python ./anim/game.py
