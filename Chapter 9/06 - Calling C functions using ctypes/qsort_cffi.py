from random import shuffle
from cffi import FFI

ffi = FFI()

# Declare the signature of the C function we'll use from the C library
ffi.cdef("""
    typedef int (*cmpfunc_t)(const void *, const void *);
    void qsort(void *base, size_t nmemb, size_t size, cmpfunc_t compar);
""")

# Load the C library
libc = ffi.dlopen(None)  # None means the standard C library


# Define the comparison function in Python
@ffi.callback("int(const void *, const void *)")
def cffi_int_compare(a, b):
    a, b = ffi.cast("int *", a)[0], ffi.cast("int *", b)[0]
    print(" %s cmp %s" % (a, b))
    return a - b


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)

    # Create a new C array using the numbers list
    c_array = ffi.new("int[]", numbers)

    libc.qsort(
        # pointer to the sorted array
        c_array,
        # length of the array
        len(c_array),
        # size of single array element
        ffi.sizeof("int"),
        # callback (pointer to the C comparison function)
        cffi_int_compare,
    )
    print("sorted:   ", [c_array[i] for i in range(len(c_array))])


if __name__ == "__main__":
    main()