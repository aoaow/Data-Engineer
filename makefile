$ make
echo "int main() { return 0; }" > blah.c
cc -c blah.c -o blah.o
cc blah.o -o blah
