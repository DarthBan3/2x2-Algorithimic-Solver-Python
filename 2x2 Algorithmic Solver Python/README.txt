This is a 2x2 Rubik's cube solver I programmed in Python. 
It's generates A solution, but it's needlessly long and inefficient.
I wanted to try something fun for a project and this is what I ended up with. 
I used the Quarter Turn Metric, which I replicated as a seperate file, 
so you can implement it in any other projects of yours. Or if you want to use 
half turn metric, it significantly reduces work, as you only have to add 6 more 
functions.

HOW TO USE:
1. I have included an Image. See it once before running the program.
2. Choose one side and then input the sides with respect to that.
3. Side colour Inputs are in the order Top Right, Bottom Right, Bottom Left, Top Left
   If you look at the image, that order also corresponds to the indexing of the pieces on
   the list.
4. The output generated is in Signmaster Notation. R means Right Clockwise.Ri means Right Anticlockwise
5. Execute the given moves, and the cube should be solved.