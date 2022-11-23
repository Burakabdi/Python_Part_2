# Write a program that:
# take a keyboard input string, representing a nucleotide (A, C, G, T)
# print the complementary nucleotide on screenthe complementary nucleotide are (A,T) and
# (C,G) (in both ways)
# Make sure the program works correctly with both uppercase and
# lowercase input.

nucleotide = input("enter a nucleotide: ")

if nucleotide.upper() == "A":
    print("complementary nucleotide is: T")
elif nucleotide.upper() == "T":
    print("complementary nucleotide is: A")
elif nucleotide.upper() == "C":
    print("complementary nucleotide is: G")
elif nucleotide.upper() == "G":
    print("complementary nucleotide is: C")
else:
    print("It isn't a nucleotide!")
