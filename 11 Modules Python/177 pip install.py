# REQUIRED: pip install pyjokes
import pyjokes

jokes = pyjokes.get_jokes()
print(*jokes, sep='\n')