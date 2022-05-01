.PHONY: clean

# define compiler, compiler flag variables -g for generating all debugging info, java virtual machine
JC = javac
JFLAGS = -g
JVM = java

# MAIN is a variable name with name of the file containing the main method
MAIN = Main

# clear any default targets for building .class files from .java
.SUFFIXES: .java .class

# target entery for creating .class from .java files
# This is a target entry that uses the suffix rule syntax:
#	DSTS:
#		rule
# 'TS' is the suffix of the target file, 'DS' is the suffix of the
# dependency file, and 'rule' is the rule for building target
# $* is a built in macro that gets the basename of the current target

.java.class:
	$(JC) $(JFLAGS) $*.java

# CLASSES is a macro consisting of 4 words (one for each java source file)
CLASSES = BodyPart.java HandWashingTechnique.java Person.java Main.java

# the default make target entry, here it is target classes
default: classes


# This target entry uses Suffix Replacesment within a macro:
# $(name:string1=string2)
classes: $(CLASSES:.java=.class)

# Running the program
run: $(MAIN).class
	$(JVM) $(MAIN)


# RM is a predefined macro in make (RM = rm -f )
clean:
	@echo "Removing .class files..."
	$(RM) *.class