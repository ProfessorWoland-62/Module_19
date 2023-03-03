
valid_email = 'devil@bk.ru'
valid_password = '666'

invalid_auth_key = {
'key' : '5197aab0b93a710209762f01af5350a5b6cb0dfec19d88defb0061db'
}

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
    'spacesAround' : ' sdgfskjgylgjsdfhogjnso ',
    'special_v2' : '╚ ╛ⓡ ⓢ ⓣ▙ ▚ ▛ ▜◑ ◒ ◓☪ ☫ ☬ ☭ᑜ ᑝᔸ ᔹᵭ ᵮ ᵯ ᵰ≤ ≥⨘ ⨙ ⨚',
    }

pet_name_type = {
    'empty' : '',
    'kirilic' : 'теКст нА киРиЛЛИце',
    'special' : '~`!@#$%^&*()_+?:"{}[];’',
    'spacesAround' : ' sdgfsdfhlgjsdgdgogjnso ',
    'special_v2' : '╚ ╛ⓡ ⓢ ⓣ▙ ▚ ▛ ▜◑ ◒ ◓☪ ☫ ☬ ☭ᑜ ᑝᔸ ᔹᵭ ᵮ ᵯ ᵰ≤ ≥⨘ ⨙ ⨚',
    'long255' : 'commodo amet dolore consequat sit ea eu aliqua sunt in elit anim laborum consectetur nulla aliquip laboris incididunt voluptate ipsum laborum amet exercitation non consectetur ea Lorem exert qui cupidatat eiusmod nisi officia veniam nostrud veniam laborum',
    'long256' : 'commodo amet dolore consequat sit ea eu aliqua sunt in elit anim laborum consectetur nulla aliquip laboris incididunt voluptate ipsum laborum amet exercitation non consectetur ea Lorem exert qui cupidatat eiusmod nisi officia veniam nostrud veniam laborumm',
    'long1024' : 'anim deserunt culpa Lorem nisi mollit enim in duis enim reprehenderit proident irure magna dolore velit esse aute esse aliqua veniam officia id veniam pariatur proident laboris aliqua ex aute adipisicing deserunt ut esse cillum et irure magna sunt excepteur adipisicing nisi cillum id laborum elit esse eu velit esse consequat excepteur occaecat consequat anim proident laboris eu officia nostrud dolore qui occaecat dolore ipsum in officia reprehenderit culpa nisi eu irure aute velit aute amet sunt pariatur exercitation irure ad exteur proident adipisicing sit dolor ut elit esse esse mollit commodo nulla duis reprehenderit aute in tempor eu commodo sunt commodo aute aute ad cillum consequat duis duis ad incididunt cupidatat anim occaecat irure in adipisicing reprehenderit commodo Lorem sit tempor nostrud eu dolore esse sunt occaecat commodo non et ipsum dolor quis voluptate ad mollit laboris sit id duis id Lorem ut ipsum nostrud incididunt ullamco minim nostrud officia amet aisicing excepteur exercitation repreh',
    'long2048' : 'anim deserunt culpa Lorem nisi mollit enim in duis enim reprehenderit proident irure magna dolore velit esse aute esse aliqua veniam officia id veniam pariatur proident laboris aliqua ex aute adipisicing deserunt ut esse cillum et irure magna sunt excepteur adipisicing nisi cillum id laborum elit esse eu velit esse consequat excepteur occaecat consequat anim proident laboris eu officia nostrud dolore qui occaecat dolore ipsum in officia reprehenderit culpa nisi eu irure aute velit aute amet sunt pariatur exercitation irure ad excepteur proident adipisicing sit dolor ut elit esse esse mollit commodo nulla duis reprehenderit aute in tempor eu commodo sunt commodo aute aute ad cillum consequat duis duis ad incididunt cupidatat anim occaecat irure in adipisicing reprehenderit commodo Lorem sit tempor nostrud eu dolore esse sunt occaecat commodo non et ipsum dolor quis voluptate ad mollit laboris sit id duis id Lorem ut ipsum nostrud incididunt ullamco minim nostrud officia amet adipisicing excepteur exercitation voluptate consectetur pariatur sit ad magna excepteur ea est ullamco cillum commodo cupidatat duis cillum dolore laboris eu eu eu sit ex occaecat ipsum incididunt cillum sit labore culpa nisi excepteur esse consectetur ad aute laborum laboris laborum eu est excepteur est irure tempor incididunt aliquip nisi deserunt aliqua consectetur eu incididunt anim officia aute cillum magna dolor commodo enim eu elit eu elit labore deserunt anim cillum pariatur eiusmod cupidatat id do deserunt eu laboris minim nisi magna et do ut in enim eu do mollit elit officia incididunt laborum labore do veniam incididunt eu ex nisi mollit consequat incididunt esse labore excepteur est exercitation id aliqua exercitation ipsum ex sit eiusmod laboris pariatur sint id mollit veniam in cupidatat nisi nisi aute duis magna anim laborum officia est cupidatat voluptate eu dolore dolor occaecat laborum adipisicing do eu sit eu id excepteur ullamco id esse commodo aliquip consectetur ad Lorem reprehenderit nostrud amet voluptate amet incididu',
}

pet_age = {
    'empty' : '',
    'negative' : -2,
    'zero' : 0,
    'text' : 'sdgfsdfhlgjsdgdgogjnso',
    'big' : 2**10,
    'large' : 123**23,
    'float' : 2.35,
    'complex' : (-4)**0.5,
}

pet_photo_all = {
    'pic1' : 'cat1.jpg',
    'pic2' : 'cat2.jpg',
    'size_8k' : '7680x4320.jpg',
    'size_10k' : '10000x10000.jpg',
    'bmp' : 'bmp.bmp'
}
