#Specifikation:

##Inledning:

Jag ska göra ett spel med hjälp av modulen pygame. Spelet kommer vara en kopia (ish) på spelet Eskiv, se länk(http://www.fetchfido.co.uk/games/eskiv/eskiv.htm) men med mer rymdkänsla. Det som kommer ta tid är konstructioner av miljön och de klasser jag behöver för att kontrollera objekten. Jag kommer även behöva göra programmet i python2 vilket kommer leda till en del syntaxfel(troligtvis) då jag är van vi python3. Förutom det tror jag det kommer vara svårt att hantera kollisioner mellan spelaren och resterande spelobjekt.
Spelet rör sig i två dimensioner och det finns tre olika typer av objekt. Den ena typen av objekt är spelaren som är en fyrkant som rör sig i planet, styrd av pilknapparna. Den andra objekttypen är studsbollar i planet, de kommer röra sig med en konstant fart men riktningen ändras i samband med att de studsar på väggar. Dessa studsbollar är farliga för spelaren och om spelaren kommer i kontakt med dem så dör hen. Det sista objektet är målobjektet, vilket spelaren ska försöka ta sig till utan att kollidera med studsbollarna. När spelaren lyckas ta sig till målobjektet får spelaren en poäng och ett nytt mål genereras någonstans på spelplanen.

##Användarscenarier:

###1: 
Johanna har fått spelet av en kompis och kör spelet från terminalen i python2. Det kommer upp ett fönster till spelplan där spelaren genereras tillsammans med ett grönt mål och en röd studsboll som Johanna måste undvika för att inte förlora. Johanna ska manövrera spelaren med piltangentarna för att ta sig till det gröna målobjektet, varje gång hon tar sig till målobjektet kommer en ny fiende genereras på planen. Om spelarobjektet kolliderar med en fiende kommer spelet stängas ner och spelarens totala poäng kommer printas i terminalen. 

###2: 
När Nisse spelar spelet kommer han se en fyrkantig spelplan med en bakgrundsbild från rymden med rörliga "stjärnor" i bakgrunden, dessa kommer inte växelverka med spelaren utan är bara där för visual effects. Nisse kommer sedan använda piltangenerna för att styra spelarobjektet för att ta sig till målobjektet utan att kollidera med de rörande studsbollarna. Studsbollarna, spelaren och målet kommer nisse kunna urskilja från varandra genom färger och form. Varje gång Nisse tar sig till målet blir det svårare och svårare att överleva eftersom fler och fler fiendeobjekt populerar skärmen.

##Programskellet(två filer):

###classesEskiv.py:


	#SpriteObjects kommer ha all gemensam kod för alla spelets klasser. Resterande klasser kommer ärva från SpriteObjects.
	
	class SpriteObjects(pygame.sprite.Sprite):
	    def __init__(self,  x_pos=0, y_pos=0, size=25):
		pygame.sprite.Sprite.__init__(self)
	
	#spelarklass för att styra spelarobjektets position, score och rörelser.

	class Spelare(SpriteObjects):
		def __init__(self):
			pass
		def move(self):
			x+=dx
			y+=dy


	#Studsbollklassen representerar alla fiendeobjekt i spelet.
	class Studsboll(SpriteObjects):
		def __init__(self):
			"""velocity=random"""

			pass

	#Målobjekt som spelaren ska jaga/ta sig till.
	class Target(SpriteObjects):
		def __init__(self):
			pass

		def generateNew(self):
			"""remove current target"""
			"""add new target elsewhere"""

	#rendrar bakgrunden med rörliga "genomskinliga" bilder (ett försök i att imitera en rörlig stjärnhimmel)

	class MovingBackgrounds(SpriteObjects):
		def __init__(self, image, screensize):
			pass
		def move():
			pass


###Eskiv 2:

	#imports the class-module
	import classesEskiv.py

	#mainprogram 
	def main():
		# This is a list of sprites.
		objects = pygame.sprite.Group()

		# This is a list of every sprite.
		all_sprites_list = pygame.sprite.Group()

		#creates a bunch of initial objects and adds them to the spritegroups.
		player=classes.Spelare()
		add player do all_sprites_list

		target= classes.Target()
		add target to all_sprites_list and objects

		studsboll=classes.Studsboll()
		add studsboll to all_sprites_list and objects

		#generates all backgroundimages
		for picture in PICTURELIST:
			background=MovingBackgrounds(picture)
			add background to all_sprites_list

		while not done:
			#checks keyboard-actions
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					break
				pass

			#checks colisions the player has done with all other sprites
			if check_kollision:
				if self.objecttype==1:
					add_points
					target.generateNew()
					new_studsboll=Studsboll(LEVEL)
				elif self.objecttype==2:
					pass
		
			#moves the player accordingly with it's velocity
			player.move()
		
			#Blits the background images onto the screen, (this is the bottom layer of the screen)
			screen.blit (background_image)

			#draws all sprites from all spriteslist group
			all_sprites_list.draw(screen)

			screen.flip

	main()
	print("gg")


##Flöde: 
Programmet kommer bestå av två filer. Den ena kommer innehålla de klasser och functioner jag behöver. Den andra filen kommer bestå av en main-function innehållande en while-loop som körs till spelaren stänger ner fönstret. Jag kommer ha 4 sorters objekt, ett par metoder för att kontrollera dessa och några variabler för att räkna poäng och dylikt. Alla klasser kommer få ärva från en föräldraklass som i sin tur kommer ärva från pygame.sprite.Sprite klassen för att enkelt kunna rita alla objekt och undersöka kollisioner. Sprites är rektangulära objekt med x och y koordinater. Jag kommer ha två group-listor för att kolla kollisioner mellan alla sprites(objekt), object-gruppen är till för att kolla kollisioner mellan spelaren och resterande objekt, all_sprites_list är till för att rita alla object på skärmen. Den fjärde sortens objekt kommer vara bakgrundsbilder, dessa kommer tillhöra all_sprites_list men inte objects(eftersom kollisioner med bakgrunden inte är relevant). Bakgrunds-objekten kommer att studsa runt på planet med hjälp av en move-metod

