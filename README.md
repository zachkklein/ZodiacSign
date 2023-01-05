# ZodiacSign
This app allows users to input their birth date, month, and year and displays their Astrological Sign and Chinese Zodiac Sign

##Code Snippets
'''python
def sign():
    def zodiac():
        months_new = month.get().lower()
        num = int(day.get())
        message = 'Your sign is '
        while months_new in months_list:
            if months_new == 'january':
                if num <= 19:
                    return message + 'Capricorn'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Aquarius'
            elif months_new == 'february':
                if num <= 18:
                    return message + 'Aquarius'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Pisces'
            elif months_new == 'march':
                if num <= 21:
                    return message + 'Pisces'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Aries'
            elif months_new == 'april':
                if num <= 20:
                    return message + 'Aries'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Taurus'
            elif months_new == 'may':
                if num <= 21:
                    return message + 'Taurus'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Gemini'
            elif months_new == 'june':
                if num <= 20:
                    return message + 'Gemini'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Cancer'
            elif months_new == 'july':
                if num <= 22:
                    return message + 'Cancer'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Leo'
            elif months_new == 'august':
                if num <= 22:
                    return message + 'Leo'
                elif num > 31:
                    return 'Error, please try again.'
                else:
                    return message + 'Virgo''''
