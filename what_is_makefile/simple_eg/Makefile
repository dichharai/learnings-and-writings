.PHONY: all say_hello generate_files clean

all: say_hello generate_files
#.DEFAULT_GOAL := generate_files

say_hello:
	@echo "Hello Maker World"

generate_files:
	@echo "Creating empty text files..."
	touch file-{0..9}.txt

clean:
	@echo "Cleaning up..."
	rm *.txt