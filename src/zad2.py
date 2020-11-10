#Działa na Pythonie 3.8.X
class Checker:
    def ValidPassword(self, given_string):
        """
        Checks if given_string (password) has meets the requirements.
        >>> c = Checker()
        >>> c.ValidPassword("halibutZZiemniakamimmmmmmPycha!!!111oneone")
        True
        >>> c.ValidPassword("HumanistaBeletrysta2137()")
        True
        >>> c.ValidPassword("HassaN0)")
        True
        >>> c.ValidPassword("HASLo!23")
        True
        >>> c.ValidPassword("Haslo123@")
        True
        >>> c.ValidPassword("haaaaaaaaaaaaaaaa)")
        False
        >>> c.ValidPassword("!!!!!!!!!!!!!!!!")
        False
        >>> c.ValidPassword("237942789374892738")
        False
        >>> c.ValidPassword("haslomalarskie128e")
        False
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