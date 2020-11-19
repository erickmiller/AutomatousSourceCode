# AutomatousSourceCode
Stanford CS221 Final Project (grade received 105% out of 100%)
By Erick Miller

## Abstract
Inductive programming is a unique area of Artificial Intelligence focused on the task of Automatic Programming; it covers broad areas of Ai and software architecture to accomplish the creation of logical programs from incomplete specifications. Automatic Programming has been an elusive dream since the founding days of Ai with many sub-fields emerging proposed solutions, including statistical optimization methods, evolution inspired methods, and grammar based methods. Inductive synthesis of finite-state automata started in the 1970's and many early innovative works in programming were fueled by the desire for Automatic Programming. Interpreted languages, the preprocessor, automatic compiler optimizations, object oriented programming, shared dynamic libraries and modern IDEs are all descendants of the desire to automate computer programming. In this regard we are already standing on the shoulders of giants. The audacious goal of this work is to explore “completing the loop” – to posit an intelligent system that, given a short description of input and desired output, can automatically author usable software functions in a high-level programming language.

### How does it work?

This is clearly a computationally intractable problem.  So how does it acheive it's impressive results?  The pre-trained Neural Networks are serving a dual purpose: both as intelligent symbolic logic sequence predictors, as well as effectively limiting the dimensionality of the Abstract Syntax Tree's potentially otherwise very very large  (unknowably and possibly infinitely large; provably NP Hard) logic tree search space (the powerset space).

![Diagram To Accompany Explanation of Recurrent Model / Algorithm](https://github.com/erickmiller/AutomatousSourceCode/blob/master/asc.png)

### Results
To review and derive meaning from the results achieved, browse the Addendum data included. The first two most interesting and encouraging results accomplished are that first, in all cases the model was able to predict an answer that is equivalent to the Oracle and second the model was able to generalize to create new, related functional programs as complete python functions including simple mathematical logic, without needing new training data (ie the model for “Square Root” was used to generalize squared, divide by two, and a doubling function).

By far, the most impressive result can be seen in Addendum 6a – the neural network appears to have learned Newton's method for finding the square root of any number!  

For more, read the full paper available in this repo https://github.com/erickmiller/AutomatousSourceCode/blob/master/AutomatousSourceCode.pdf

Or mirrored here https://www.erickmiller.com/ErickMiller-AutomatousSourceCode-CS229.pdf

