
valid_email = 'devil@bk.ru'
valid_password = '666'

invalid_email = {
    'empty' : '',
    'kirilic' : 'кириллический@имэйл.ру',
    'unknown' : 'some.mail@domain.com',
    'wrong' : 'domain.domain.do',
}

invalid_password = {
    'empty' : '',
    'kirilic' : 'теКст нА киРиЛЛИце',
    'special' : '~`!@#$%^&*()_+?:"{}[];’',
    'spacesAround' : ' sd;gfs;lgjs;ogjnso ',
    'special_v2' : '╚ ╛ⓡ ⓢ ⓣ▙ ▚ ▛ ▜◑ ◒ ◓☪ ☫ ☬ ☭ᑜ ᑝᔸ ᔹᵭ ᵮ ᵯ ᵰ≤ ≥⨘ ⨙ ⨚',
    }



# for email in invalid_email:
#     print(email, '    ', invalid_email[email])

# print(type(invalid_email.items()), type(invalid_email.keys()))
# for email in invalid_email.items():
#     print(email[0])

# for i in range(len(invalid_email.items())):
#     print(invalid_email.items())

# print(*invalid_email.items())