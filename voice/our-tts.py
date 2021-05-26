from espeak import espeak

espeak.set_voice("ru")

espeak.pitch =150
espeak.amplitude = 15000


espeak.rate = 300

espeak.synth("где хакер aaaa aaa aaa")

while espeak.is_playing:
	pass    