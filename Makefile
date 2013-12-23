SHELL = /bin/bash

all:

new: template.py
ifndef PROBLEM
	$(error use "make new PROBLEM=<problem-name>")
endif
	@cat $< | sed 's/PROBLEM/$(PROBLEM)/g' > $(PROBLEM).py
	@echo "Initialized new program '$(PROBLEM)' from template in $(PROBLEM).py"

clean:
	rm -rf __pycache__ *.pyc *.pyo
