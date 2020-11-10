#Działa na Pythonie 3.8.X
class Password:
    def ValidPassword(self, given_string):
        """
        Return how many nucleotides are different on the same indexes.
        >>>
        """
        if not isinstance(given_string, str):
            raise ValueError('Your password must be a string')
        if len(given_string) < 8:
            raise ValueError('Your password must be at least 8 characters long')
        return 


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Odpalenie: python3 DocTestExample.py -v