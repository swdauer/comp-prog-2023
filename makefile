PROBLEM=knightpacking

c:
	mkdir --parents $(PROBLEM)
	touch $(PROBLEM)/main.c
	cp --no-clobber makefile-template-c $(PROBLEM)/makefile
	touch $(PROBLEM)/input1
