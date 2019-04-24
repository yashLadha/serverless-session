import json
import random

# https://github.com/yashLadha/cRaxYnM/blob/master/lib/craxy.dart
symbols = {
    'a': ['α', 'Á', 'ค', 'ä', 'á', 'Λ', 'ⓐ', 'ﾑ'],
    'b': ['в', 'ß', 'b', '乃', 'ⓑ', '8', '๒', '𝓫'],
    'c': ['🅒', 'ƈ', '₵', 'ḉ', '🄲', '૮', 'ς', 'c̷'],
    'd': ['d̶', '∂', 'Ꮄ', '🅳', '🄳', '🌛', '𝔡', '𝕕'],
    'e': ['ǝ', 'є', '€', 'პ', '🇪​', '乇', '🅴', 'e҉'],
    'f': ['f҉', '🅵', '千', 'ƒ', 'ꎇ', '🄵', '🎏', '𝓯'],
    'g': ['₲', '𝕘', '🅖', '𝓰', '🌀', '9', 'ƃ', 'Ꮆ'],
    'h': ['卄', 'h҉', '🄷', '♓', 'ɦ', 'ԋ', '𝓱', '𝕙'],
    'i': ['🅘', '♗', 'ɨ', '🎐', '!', '🄸', 'ι', '🇮​'],
    'j': ['🇯​', 'ʝ', 'Ĵ', 'ʝ', 'ʆ', 'ว', 'ქ', '🎷'],
    'k': ['🎋', 'k', 'ӄ', '𝙠', 'ƙ', '🅚', '𝕜', 'ⓚ', 'ᴋ'],
    'l': ['ⓛ', 'Ⱡ', 'ℓ', '↳', '𝘭', '👢', 'Ꮭ', '🄻', 'ㄥ'],
    'm': ['ɱ', '๓', '🇲​', 'ʍ', 'ᙢ', 'ℳ', '爪', '〽️'],
    'n': ['🎵', 'n', 'ᑎ', 'ռ', '𝙣', '♫', 'ɳ', 'и', 'ⓝ'],
    'o': ['Ꮎ', 'ø', '๏', 'Ő', '🅾', '🄾', 'Ꭷ', '⚽'],
    'p': ['🅿️', 'Ꭾ', 'ｐ', 'Ꮲ', '卩', 'Ƥ', 'ρ', 'ק', 'ᖘ'],
    'q': ['զ', 'Ƣ', 'ᕴ', 'q̶', 'Ǫ', 'q҉', '🆀', '🅀'],
    'r': ['Ꮢ', '🅁', 'ᖇ', '☈', '𝓻', 'Ɽ', '🌱', 'r', 'r҉'],
    's': ['s', 'ら', '丂', '§', 'ş', 'ֆ', 'ꌗ', 'Ƨ', 'ʂ'],
    't': ['ᖶ', 't̶', 't̲', 'Ե', 'Ƭ', '✞', 't҉', '🌴', '🅃'],
    'u': ['🅄', '⛎', 'ʊ', '☋', '𝓾', '𝖚', 'ⓤ', 'Ꮼ'],
    'v': ['Ꮙ', 'ש', 'v', 'ง', 'v̶', '✅', '✓', '𝖛', '🆅'],
    'w': ['Ꮃ', 'щ', 'Ŵ', 'Ꮗ', 'Ꮗ', 'ᗯ', '𝚠', '𝐰', '🅦'],
    'x': ['ⓧ', 'χ', '𝔁', '⌘', '❎', '🅇', 'ж', '乂', 'א'],
    'y': ['ყ', 'Ƴ', '🇾​', '¥', 'ᖻ', 'Ў', 'Ꮍ', 'ꌩ', 'Ƴ'],
    'z': ['Հ', 'Z', 'ɀ', '乙', 'ፚ', '🆉', 'z҉', '🅉', '💤', 'ᘔ'],
};


def test_service(event, context):
    """
    Test service function 
    All the business logic needs to written inside this function.
    Params for this function should not be altered or changed as this is
    specific to the cloud service provider.
    """
    if 'body' not in event:
        return dict(
            statusCode=500,
            body='No body param founded'
        )
    payload = json.loads(event['body'])
    ugly = "".join([ symbols[char][random.randint(0, len(symbols[char])-1)] for char in payload['data'] ])
    return dict(
        statusCode=200,
        body=json.dumps({'ugly': ugly})
    )