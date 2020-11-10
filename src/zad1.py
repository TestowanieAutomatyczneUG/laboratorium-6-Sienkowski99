#Działa na Pythonie 3.8.X
class Hamming:
    def distance(self, a, b):
        """
        Return how many nucleotides are different on the same indexes.
        >>> h = Hamming()
        >>> h.distance("","")
        0
        >>> h.distance("A", "A")
        0
        >>> h.distance("G", "T")
        1
        >>> h.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> h.distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> h.distance("AATG", "AAA")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance("ATA", "AGTG")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance("", "G")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance("G", "")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance(6, "")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance("G", None)
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance(3, 33)
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        >>> h.distance(True, "")
        Traceback (most recent call last):
          File "C:\Python\lib\doctest.py", line 1337, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            h.distance("AATG", "AAA")
          File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad1.py", line 21, in distance
            raise ValueError('err')
        ValueError: err
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError('err')
        if len(a) != len(b):
            raise ValueError('err')
        result = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                result += 1
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Odpalenie: python3 DocTestExample.py -v